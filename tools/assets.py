import numpy as np, base64, io, os
from PIL import Image
from scipy import ndimage as ndi
A='/mnt/user-data/attachments/b52fb265-d1c5-526d-8711-217681a6bd01/'
OUT='/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/gen/img/'
os.makedirs(OUT,exist_ok=True)
SRC=dict(hero='5739a9d0',phone='36f1be30',laptop='fe0cae85',cafe='13a7a5c8',woman='d6d5d335',icons='2aeffd2c',lock='76e8254f',save='db5c1b7c',share='de76d48e')
def load(k): return Image.open(A+SRC[k]+'-image.png').convert('RGB')
def save(im,name,q=80):
    p=OUT+name; im.save(p,'WEBP',quality=q,method=6); return p

def hero():
    im=load('hero'); w,h=im.size
    save(im.crop((0,0,w,330)),'hero-top.webp',78)
    save(im.crop((0,430,w,h)),'hero-bot.webp',78)

def phone():
    im=np.array(load('phone')).astype(float)
    lum=im.mean(2); sat=im.max(2)-im.min(2)
    H,W=lum.shape
    m=((lum<225)|(sat>25))
    m[955:]=False; m[:38]=False; m[:,:528]=False; m[:,1002:]=False
    m=ndi.binary_closing(m,iterations=3); m=ndi.binary_fill_holes(m)
    ms=ndi.gaussian_filter(m.astype(float),0.8)
    sh=np.clip((246-lum)/246,0,1)*0.0
    sh[:954]=0
    a=np.maximum(ms,sh*(1-ms))
    rgb=np.where(ms[...,None]>0.02,im,0)
    out=np.dstack([rgb,a*255]).astype(np.uint8)
    img=Image.fromarray(out,'RGBA').crop((490,30,1046,1010))
    img.save(OUT+'phone.webp','WEBP',quality=88,method=6)
    img.save(OUT+'phone.png')

def icons():
    im=np.array(load('icons')).astype(float)
    lum=im.mean(2); sat=im.max(2)-im.min(2)
    m=(sat>20)|(lum<172)
    m=ndi.binary_closing(m,iterations=4); m=ndi.binary_fill_holes(m)
    grp,n=ndi.label(ndi.binary_dilation(m,iterations=22))
    lab=grp*m
    objs=ndi.find_objects(lab)
    big=[(i+1,s) for i,s in enumerate(objs) if (s[0].stop-s[0].start)*(s[1].stop-s[1].start)>20000]
    big.sort(key=lambda t:(round(((t[1][0].start+t[1][0].stop)/2)/400),(t[1][1].start+t[1][1].stop)/2))
    names=['food','home','bus','bag','bill','oth']
    res={}
    for (i,s),nm in zip(big,names):
        mk=(lab==i)
        mk=ndi.binary_fill_holes(mk)
        ms=ndi.gaussian_filter(ndi.binary_erosion(mk,iterations=2).astype(float),0.9)
        y0,y1,x0,x1=s[0].start-4,s[0].stop+4,s[1].start-4,s[1].stop+4
        rgba=np.dstack([im,ms*255]).astype(np.uint8)[y0:y1,x0:x1]
        t=Image.fromarray(rgba,'RGBA')
        sz=max(t.size); sq=Image.new('RGBA',(sz,sz),(0,0,0,0)); sq.paste(t,((sz-t.size[0])//2,(sz-t.size[1])//2))
        sq=sq.resize((176,176),Image.LANCZOS)
        sq.save(OUT+f'ic-{nm}.webp','WEBP',quality=90,method=6); sq.save(OUT+f'ic-{nm}.png')
        res[nm]=sq.size
    return res,len(big)

def photos():
    lap=load('laptop').crop((200,70,1472,870)); save(lap.resize((1272,800)),'laptop.webp',82)
    cafe=load('cafe'); save(cafe.resize((1100,733),Image.LANCZOS),'cafe.webp',78)
    w=load('woman'); save(w.resize((1500,844),Image.LANCZOS),'woman.webp',78)
    lk=load('lock'); save(lk.resize((1100,733),Image.LANCZOS),'lock.webp',80)
    sv=load('save'); save(sv,'save.webp',80)
    sh=load('share'); save(sh.resize((1400,788),Image.LANCZOS),'share.webp',78)

def b64(name):
    mime='image/webp'
    return f'data:{mime};base64,'+base64.b64encode(open(OUT+name,'rb').read()).decode()

def css_vars():
    names=['hero-top','hero-bot','phone','laptop','cafe','woman','lock','save','share']+['ic-'+n for n in ['food','home','bus','bag','bill','oth']]
    return ''.join(f'--i-{n}:url("{b64(n+".webp")}");' for n in names)

if __name__=='__main__':
    hero(); phone(); print(icons()); photos()
    for f in sorted(os.listdir(OUT)):
        if f.endswith('.webp'): print(f,os.path.getsize(OUT+f)//1024,'KB')
