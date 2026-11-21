import pymupdf, sys, re, os, json
SRC="/mnt/user-data/uploads/2do Ciencia/"
OUT="/home/claude/work/figs/"
targets=json.load(open(sys.argv[1]))
docs={}
res=[]
for key,(path,label,pmin,pmax) in targets.items():
    d=docs.setdefault(path,pymupdf.open(SRC+path))
    found=None
    for i in range(pmin-1, min(pmax,len(d))):
        p=d[i]
        for b in p.get_text("blocks"):
            txt=b[4].strip()
            head=txt[:len(label)+25]
            if (re.match(re.escape(label)+r"[\.:]", txt) or re.match(re.escape(label)+r" [A-Z]", txt) or txt==label) and (re.match(re.escape(label)+r"\.", txt) or not re.search(r"shows|summarizes|highlights|depicts|illustrates|compares|lists|is a |represents", head)):
                found=(i,b); break
        if found: break
    if not found:
        res.append((key,"NOTFOUND")); continue
    i,b=found; p=d[i]; cap_top=b[1]
    imgs=[r for r in p.get_image_info() if r["bbox"][3]<=cap_top+5 and (r["bbox"][2]-r["bbox"][0])>80]
    if not imgs and i>0:
        pp=d[i-1]; pim=[r for r in pp.get_image_info() if (r["bbox"][2]-r["bbox"][0])>80]
        if pim and cap_top<p.rect.y0+120:
            p=pp; imgs=pim; cap_top=p.rect.y1
    if imgs:
        bb=max(imgs,key=lambda r:r["bbox"][3])["bbox"]
        # union images close vertically
        rect=pymupdf.Rect(bb)
        for r in imgs:
            R=pymupdf.Rect(r["bbox"])
            if R.y1>rect.y0-15 and R.y0<rect.y1: rect|=R
        clip=rect
    else:
        # vector: region between previous text block bottom and caption
        prev=[bl for bl in p.get_text("blocks") if bl[3]<cap_top-2 and bl[6]==0 and len(bl[4].strip())>60]
        top=max([bl[3] for bl in prev],default=p.rect.y0+20)
        clip=pymupdf.Rect(p.rect.x0+20,top+2,p.rect.x1-20,cap_top-1)
    if clip.height<30:
        # caption at top -> figure maybe on previous page bottom
        res.append((key,f"SMALL p{i+1}")); 
    pix=p.get_pixmap(clip=clip,dpi=170)
    fn=OUT+key+".png"; pix.save(fn)
    res.append((key,f"p{i+1} {int(clip.width)}x{int(clip.height)} {'img' if imgs else 'vec'}"))
for r in res: print(*r)
