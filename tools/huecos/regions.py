import cv2,numpy as np,sys,json
def regions(path):
    im=cv2.imread(path); g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    H,W=g.shape
    # text strokes: strong local contrast, small components
    a=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,41,18)
    b=cv2.adaptiveThreshold(255-g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,41,18)
    comps=[]
    for m in (a,b):
        n,lab,st,_=cv2.connectedComponentsWithStats(m,8)
        for i in range(1,n):
            x,y,w,h,area=st[i]
            if 12<=h<=110 and w<=140 and area>=25 and area/(w*h)>0.08 and not (w>4*h and h<25):
                comps.append((x,y,w,h))
    mask=np.zeros((H,W),np.uint8)
    for x,y,w,h in comps: mask[y:y+h,x:x+w]=255
    # join chars horizontally into words/lines
    k=cv2.getStructuringElement(cv2.MORPH_RECT,(28,5))
    j=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,k)
    n,lab,st,_=cv2.connectedComponentsWithStats(j,8)
    out=[]
    for i in range(1,n):
        x,y,w,h,area=st[i]
        if h>=14 and w>=18: out.append([int(x),int(y),int(w),int(h)])
    return out,(W,H)
if __name__=='__main__':
    fid=sys.argv[1]
    out,(W,H)=regions(f'hi/{fid}.png')
    im=cv2.imread(f'hi/{fid}.png')
    for i,(x,y,w,h) in enumerate(out):
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3); cv2.putText(im,str(i),(x,y-4),cv2.FONT_HERSHEY_SIMPLEX,1.1,(255,0,0),3)
    cv2.imwrite(f'/tmp/reg_{fid}.png',im); print(len(out))
