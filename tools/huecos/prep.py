import cv2,json,sys
from regions import regions
ocr=json.load(open('ocr2.json'))
def merge(rs):
    rs=sorted(rs,key=lambda r:(r[1],r[0])); groups=[[r] for r in rs]
    changed=True
    def box(g):
        x0=min(r[0] for r in g);y0=min(r[1] for r in g);x1=max(r[0]+r[2] for r in g);y1=max(r[1]+r[3] for r in g);return x0,y0,x1,y1
    while changed:
        changed=False
        for i in range(len(groups)):
            for j in range(i+1,len(groups)):
                a=box(groups[i]);b=box(groups[j])
                la=groups[i][-1]; # last line height
                hh=min(max(r[3] for r in groups[i]),max(r[3] for r in groups[j]))
                gap=b[1]-a[3] if b[1]>=a[3] else a[1]-b[3]
                ovx=min(a[2],b[2])-max(a[0],b[0])
                ca=(a[0]+a[2])/2; cb=(b[0]+b[2])/2
                if -hh*0.3<=gap<=hh*0.45 and ovx>0.35*min(a[2]-a[0],b[2]-b[0]) and abs(ca-cb)<0.5*max(a[2]-a[0],b[2]-b[0]):
                    groups[i]+=groups[j]; del groups[j]; changed=True; break
            if changed: break
    out=[]
    for g in groups:
        g=sorted(g,key=lambda r:r[1])
        out.append(dict(box=list(box(g)),lines=[r for r in g]))
    out.sort(key=lambda d:(d['box'][1]//40,d['box'][0]))
    return out
def guess(fid,lines):
    ws=ocr[fid]['words']; txt=[]
    for (x,y,w,h) in lines:
        inl=[q for q in ws if x-4<=q['x']+q['w']/2<=x+w+4 and y-6<=q['y']+q['h']/2<=y+h+6]
        inl.sort(key=lambda q:q['x']); txt.append(' '.join(q['t'] for q in inl))
    return ' / '.join(txt)
res={}
for fid in sorted(ocr):
    rs,(W,H)=regions(f'hi/{fid}.png')
    g=merge(rs)
    im=cv2.imread(f'hi/{fid}.png')
    for i,d in enumerate(g):
        x0,y0,x1,y1=d['box']; d['ocr']=guess(fid,d['lines'])
        cv2.rectangle(im,(x0,y0),(x1,y1),(0,0,255),3)
        cv2.putText(im,str(i),(x0-2,max(y0-6,22)),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0),3)
    # downscale review image to max 1600 wide
    s=min(1.0,1600/im.shape[1]); im=cv2.resize(im,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
    cv2.imwrite(f'rev/{fid}.png',im)
    res[fid]=dict(W=W,H=H,regions=g)
    print(fid,len(g),end=' ')
json.dump(res,open('regions.json','w'))
