import sys,json,pymupdf,pytesseract
from PIL import Image
sys.path.insert(0,'.')
meta=json.load(open('figmeta.json'))
SRC="/mnt/user-data/uploads/2do Ciencia/"
T=json.load(open('/home/claude/site/cdsite/tools/figuras/objetivos.json'))
DPI=400; K=DPI/170
docs={}
res={}
for fid,m in meta.items():
    path=T[m['png']][0]
    d=docs.setdefault(path,pymupdf.open(SRC+path))
    p=d[m['page']]; clip=pymupdf.Rect(m['clip'])
    pix=p.get_pixmap(clip=clip,dpi=DPI)
    im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
    im.save(f'hi/{fid}.png')
    data=pytesseract.image_to_data(im,lang='eng',config='--psm 11',output_type=pytesseract.Output.DICT)
    words=[]
    for i,t in enumerate(data['text']):
        if t.strip() and float(data['conf'][i])>-1:
            words.append(dict(t=t,x=data['left'][i],y=data['top'][i],w=data['width'][i],h=data['height'][i],c=float(data['conf'][i]),b=data['block_num'][i],p=data['par_num'][i],l=data['line_num'][i]))
    res[fid]=dict(W=im.width,H=im.height,words=words)
    print(fid,len(words))
json.dump(res,open('ocr.json','w'))
