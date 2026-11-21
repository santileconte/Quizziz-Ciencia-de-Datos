import sys,json,cv2,numpy as np,pytesseract
from PIL import Image
ids=sys.argv[1:] or [l.split('.')[0] for l in __import__('os').listdir('hi')]
res={}
def run(img,tag):
    d=pytesseract.image_to_data(img,lang='eng',config='--psm 11 --oem 1',output_type=pytesseract.Output.DICT)
    out=[]
    for i,t in enumerate(d['text']):
        if t.strip() and float(d['conf'][i])>=30 and any(ch.isalnum() for ch in t):
            out.append(dict(t=t,x=d['left'][i],y=d['top'][i],w=d['width'][i],h=d['height'][i],c=float(d['conf'][i]),src=tag))
    return out
for fid in sorted(ids):
    g=cv2.imread(f'hi/{fid}.png',cv2.IMREAD_GRAYSCALE)
    g=cv2.GaussianBlur(g,(3,3),0)
    a=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,15)   # dark text -> black
    b=cv2.adaptiveThreshold(255-g,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,15) # light text -> black
    w=run(a,'d')+run(b,'l')
    # dedupe overlapping words: keep higher conf
    w.sort(key=lambda x:-x['c']); keep=[]
    for x in w:
        ov=False
        for k in keep:
            ix=max(0,min(x['x']+x['w'],k['x']+k['w'])-max(x['x'],k['x'])); iy=max(0,min(x['y']+x['h'],k['y']+k['h'])-max(x['y'],k['y']))
            if ix*iy>0.4*min(x['w']*x['h'],k['w']*k['h']): ov=True;break
        if not ov: keep.append(x)
    res[fid]=dict(W=g.shape[1],H=g.shape[0],words=keep)
    print(fid,len(keep),end=' ')
json.dump(res,open('ocr2.json','w'))
