import sys
sys.path.insert(0,'/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/gen')
from web import IC,CAT,ico,cc,chip,status,bar
import assets
OUT='/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/expenses-design/project/'
INK='#0A0A0A';MUT='#6E6E73';BLUE='#2457D6';GRN='#1B7F4B';RED='#B3261E'

def odo(text,cls=''):
    out='';i=0
    for ch in text:
        if ch.isdigit():
            d=int(ch)
            col=''.join(f'<span>{n}</span>' for n in range(10))
            out+=f'<span class="od"><span class="od-col" style="--d:{d};--i:{i}">{col}</span></span>'
            i+=1
        else:
            out+=f'<span class="od-s">{ch}</span>'
    return f'<span class="odo {cls}" aria-label="{text}">{out}</span>'

CSS='''
.lp{--ink:#0A0A0A;--mut:#6E6E73;--line:#D2D2D7;--soft:#F5F5F7;--blue:#2457D6;--grn:#1B7F4B;--red:#B3261E;
 width:100%;position:relative;background:#FFFFFF;color:var(--ink);font-family:'Inter',system-ui,-apple-system,sans-serif;overflow:hidden;-webkit-font-smoothing:antialiased}
.lp *{box-sizing:border-box}
.lp h1,.lp h2,.lp h3,.lp p{margin:0}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
/* nav */
.nav{position:sticky;top:0;z-index:50;height:52px;background:rgba(255,255,255,.72);backdrop-filter:saturate(180%) blur(20px);-webkit-backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid rgba(0,0,0,.08)}
.nav .wrap{height:52px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;letter-spacing:-.01em}
.brand i{width:26px;height:26px;border-radius:8px;background:var(--ink);display:flex;align-items:center;justify-content:center}
.nav-links{display:flex;gap:32px;font-size:13px;color:#424245}
.nav-links a:hover{color:var(--ink)}
.pill{display:inline-flex;align-items:center;justify-content:center;height:34px;padding:0 16px;border-radius:17px;background:var(--ink);color:#fff;font-size:13px;font-weight:600;transition:transform .25s cubic-bezier(.2,.8,.2,1),background .25s}
.pill:hover{transform:scale(1.04);background:#000}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:52px;padding:0 28px;border-radius:26px;background:var(--ink);color:#fff;font-size:17px;font-weight:600;position:relative;overflow:hidden;transition:transform .3s cubic-bezier(.2,.8,.2,1)}
.btn:hover{transform:scale(1.04)}
.btn::after{content:"";position:absolute;inset:0;background:linear-gradient(100deg,transparent 30%,rgba(255,255,255,.35) 50%,transparent 70%);transform:translateX(-120%);animation:sheen 4.5s ease-in-out infinite}
.btn.light{background:#fff;color:var(--ink)}
.btn.light::after{background:linear-gradient(100deg,transparent 30%,rgba(0,0,0,.08) 50%,transparent 70%)}
.link{display:inline-flex;align-items:center;gap:4px;color:var(--blue);font-size:19px;font-weight:500}
.link svg{transition:transform .3s}
.link:hover svg{transform:translateX(4px)}
.eyebrow{font-size:19px;font-weight:600;letter-spacing:-.01em;color:var(--blue)}
.dark .eyebrow{color:#7DA2FF}
.h-xl{font-size:96px;line-height:100px;font-weight:700;letter-spacing:-.045em}
.h-l{font-size:64px;line-height:68px;font-weight:700;letter-spacing:-.04em}
.sub{font-size:24px;line-height:32px;color:var(--mut);font-weight:500;letter-spacing:-.01em}
.dark .sub{color:#A1A1A6}
.sec{padding:140px 0}
.dark{background:#000;color:#F5F5F7}
.soft{background:var(--soft)}
/* hero */
.hero{position:relative;padding:88px 0 0;text-align:center;overflow:hidden;background:linear-gradient(#FAFAFB 60%,#F5F5F7)}
.hb{position:absolute;left:-3%;width:106%;z-index:0;pointer-events:none;background-repeat:no-repeat;background-size:100% 100%;animation:hbdrift 20s ease-in-out infinite alternate}
.hb.t{top:0;aspect-ratio:1672/330;background-image:var(--i-hero-top);-webkit-mask-image:linear-gradient(#000 62%,transparent);mask-image:linear-gradient(#000 62%,transparent)}
.hb.b{bottom:0;aspect-ratio:1672/511;background-image:var(--i-hero-bot);-webkit-mask-image:linear-gradient(transparent,#000 36%,#000 72%,transparent);mask-image:linear-gradient(transparent,#000 36%,#000 72%,transparent);animation-delay:-8s}
.hero .wrap{position:relative;z-index:2}
.blob{position:absolute;border-radius:50%;filter:blur(90px);opacity:.5;z-index:0;animation:drift 18s ease-in-out infinite alternate}
.b1{width:520px;height:520px;background:#9DB7FF;left:-120px;top:120px}
.b2{width:460px;height:460px;background:#9FE3BC;right:-100px;top:60px;animation-delay:-6s}
.b3{width:420px;height:420px;background:#FFD1A6;left:36%;top:520px;animation-delay:-12s}
.hero .h-xl{margin-top:14px;animation:rise 1s cubic-bezier(.2,.8,.2,1) both}
.hero .sub{margin:22px auto 0;max-width:640px;animation:rise 1s .12s cubic-bezier(.2,.8,.2,1) both}
.cta-row{margin-top:34px;display:flex;gap:28px;justify-content:center;align-items:center;flex-wrap:wrap;animation:rise 1s .24s cubic-bezier(.2,.8,.2,1) both}
.eyebrow.top{animation:rise 1s cubic-bezier(.2,.8,.2,1) both}
.stage{position:relative;height:700px;margin-top:56px}
.stage .phone{position:absolute;left:50%;top:0;margin-left:-195px;animation:phoneIn 1.4s .3s cubic-bezier(.2,.8,.2,1) both,float 7s 1.7s ease-in-out infinite}
.fl{position:absolute;z-index:3;display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.86);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(0,0,0,.06);border-radius:18px;padding:12px 16px;box-shadow:0 18px 50px rgba(0,0,0,.12);font-size:15px;font-weight:600;text-align:left;animation:float 6s ease-in-out infinite}
.fl small{display:block;font-size:12px;font-weight:500;color:var(--mut)}
.fl.a{left:4%;top:90px;animation-delay:-1s}
.fl.b{right:3%;top:150px;animation-delay:-3s}
.fl.c{left:9%;top:380px;animation-delay:-2s}
.fl.d{right:8%;top:430px;animation-delay:-4s}
.fl.e{left:50%;margin-left:165px;top:-8px;animation-delay:-5s}
.ping{animation:ping 2.4s ease-in-out infinite}
/* phone */
.phone{text-align:left;width:391px;height:689px;background:var(--i-phone) center/100% 100% no-repeat;position:relative;filter:drop-shadow(0 40px 40px rgba(0,0,0,.22))}
.phone .scr{position:absolute;left:11.5%;top:3.06%;width:76.3%;height:88.4%;border-radius:34px;overflow:hidden;background:#fff}
.phone .scr .in{width:390px;height:844px;transform:scale(.765);transform-origin:0 0;position:relative;font-size:16px}
.phone .isl{position:absolute;left:50%;top:41px;width:78px;height:22px;margin-left:-39px;border-radius:11px;background:#000;z-index:5}
.a-h{padding:56px 20px 8px}
.a-h small{display:block;font-size:13px;color:#5C5C5C}
.a-h b{font-size:24px;line-height:30px;font-weight:700;letter-spacing:-.02em}
.a-card{margin:8px 20px 0;background:#0A0A0A;color:#fff;border-radius:20px;padding:20px}
.a-card small{font-size:14px;color:#CFCFCF}
.a-card .big{font-size:40px;line-height:48px;font-weight:700;letter-spacing:-.02em}
.track{height:8px;border-radius:4px;background:#E6E6E6;overflow:hidden}
.track i{display:block;height:8px;border-radius:4px;transform-origin:left;animation:fillx 6s cubic-bezier(.2,.8,.2,1) infinite}
.a-card .track{background:rgba(255,255,255,.28);margin-top:12px}
.a-card .track i{background:#fff;width:60%}
.a-row{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid #E6E6E6;animation:slidein 6s cubic-bezier(.2,.8,.2,1) infinite;animation-delay:calc(var(--r)*.25s)}
.a-row:last-child{border-bottom:0}
.a-row b{display:block;font-size:16px;line-height:22px;font-weight:600}
.a-row span.s{display:block;font-size:13px;line-height:18px;color:#5C5C5C}
.a-row em{margin-left:auto;font-style:normal;font-size:16px;font-weight:600;font-variant-numeric:tabular-nums}
.a-list{margin:12px 20px 0;background:#fff;border:1px solid #E6E6E6;border-radius:16px;padding:0 16px}
.a-sec{margin:16px 20px 0;display:flex;justify-content:space-between;font-size:18px;font-weight:700}
.a-sec span{font-size:14px;color:var(--blue);font-weight:600}
/* odometer */
.odo{display:inline-flex;align-items:flex-start;font-variant-numeric:tabular-nums;line-height:1}
.od{display:inline-block;height:1em;overflow:hidden}
.od-col{display:flex;flex-direction:column;animation:odo 7s cubic-bezier(.16,.84,.24,1) infinite;animation-delay:calc(var(--i)*.1s)}
.od-col span{height:1em;line-height:1em;display:block}
.od-s{display:inline-block;height:1em;line-height:1em}
/* marquee */
.marq{background:#fff;padding:36px 0;overflow:hidden;border-top:1px solid #ECECEF;border-bottom:1px solid #ECECEF}
.mq-row{display:flex;gap:14px;width:max-content;animation:marq 38s linear infinite}
.mq-row.rev{animation-direction:reverse;animation-duration:46s;margin-top:14px}
.tag{display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 22px 0 10px;border-radius:26px;background:var(--soft);font-size:17px;font-weight:600;white-space:nowrap}
.tag em{font-style:normal;font-weight:600;font-variant-numeric:tabular-nums}
/* feature layout */
.feat{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.feat.flip .txt{order:2}
.feat .txt p.sub{margin-top:22px;max-width:460px}
.feat h2{margin-top:10px}
.panel{position:relative;border-radius:32px;padding:36px;overflow:hidden}
.panel.w{background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.1);border:1px solid #ECECEF}
.panel.k{background:#111113;border:1px solid #2A2A2D}
.panel.s{background:var(--soft)}
/* add demo */
.f-lbl{font-size:14px;color:#5C5C5C;font-weight:500}
.amt{display:flex;align-items:center;gap:8px;margin:6px 0 18px;padding:14px 18px;border:1px solid #E6E6E6;border-radius:18px}
.amt span.r{font-size:32px;font-weight:600;color:#5C5C5C}
.typed{display:inline-block;overflow:hidden;white-space:nowrap;font-size:44px;line-height:52px;font-weight:700;letter-spacing:-.02em;border-right:3px solid var(--blue);width:3ch;animation:typing 9s steps(3,end) infinite,caret .8s step-end infinite}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.tile{height:76px;border-radius:16px;border:1px solid #E6E6E6;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font-size:14px;font-weight:500;animation:tilesel 12s infinite;animation-delay:calc(var(--k)*2s)}
.savebtn{margin-top:18px;height:54px;border-radius:16px;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:600;animation:press 9s infinite}
.toast{position:absolute;left:50%;bottom:-70px;transform:translateX(-50%);background:#fff;border-radius:16px;padding:12px 18px;display:flex;align-items:center;gap:10px;font-size:15px;font-weight:600;box-shadow:0 20px 50px rgba(0,0,0,.18);animation:toast 9s infinite;white-space:nowrap}
/* import demo */
.drop{height:150px;border:2px dashed #4A4A4F;border-radius:22px;display:flex;align-items:center;justify-content:center;color:#A1A1A6;font-size:15px;position:relative;animation:dropglow 9s infinite}
.file{position:absolute;left:50%;top:-60px;margin-left:-115px;width:230px;height:54px;border-radius:14px;background:#fff;color:var(--ink);display:flex;align-items:center;gap:10px;padding:0 14px;font-size:14px;font-weight:600;box-shadow:0 20px 40px rgba(0,0,0,.4);animation:filedrop 9s cubic-bezier(.3,.8,.2,1) infinite;z-index:2}
.imp{margin-top:16px;display:flex;flex-direction:column;gap:8px}
.imp-r{display:flex;align-items:center;gap:12px;background:#1C1C1F;border-radius:14px;padding:10px 14px;font-size:15px;font-weight:600;color:#F5F5F7;animation:implist 9s infinite;animation-delay:calc(var(--r)*.18s)}
.imp-r em{margin-left:auto;font-style:normal;font-variant-numeric:tabular-nums;color:#FF8B80}
.imp-r b{color:#7BD9A0;font-weight:600;font-size:13px}
.count{margin-top:14px;display:flex;align-items:center;justify-content:space-between;font-size:15px;color:#A1A1A6;animation:implist 9s infinite;animation-delay:1.4s}
.count strong{color:#fff;font-size:22px}
/* report demo */
.rep-top{background:#0A0A0A;color:#fff;border-radius:22px;padding:22px;display:flex;justify-content:space-between;align-items:flex-end}
.rep-top small{display:block;font-size:14px;color:#CFCFCF}
.rep-top .big{font-size:44px;font-weight:700;letter-spacing:-.03em}
.up{display:inline-flex;align-items:center;gap:4px;padding:4px 10px;border-radius:999px;background:#fff;color:#0A0A0A;font-size:13px;font-weight:600}
.rb{display:flex;align-items:center;gap:12px;margin-top:16px;font-size:16px;font-weight:600}
.rb .nm{width:84px}
.rb .track{flex:1;height:10px}
.rb .track i{height:10px;animation-name:growx;animation-duration:7s;animation-delay:calc(var(--r)*.15s);transform-origin:left}
.rb em{font-style:normal;width:96px;text-align:right;font-variant-numeric:tabular-nums}
.note{margin-top:22px;background:#fff;border-radius:18px;padding:16px 18px;font-size:16px;line-height:24px;animation:implist 7s infinite;animation-delay:1.6s}
/* budgets */
.bg{background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 14px 40px rgba(0,0,0,.07);margin-top:14px}
.bg:first-child{margin-top:0}
.bg-h{display:flex;justify-content:space-between;align-items:center;font-size:17px;font-weight:600}
.bg-h .l{display:flex;align-items:center;gap:10px}
.bg .track{height:10px;margin-top:12px}
.bg .track i{height:10px;animation-name:growx;animation-duration:7s;animation-delay:calc(var(--r)*.2s)}
.bg small{display:block;margin-top:8px;font-size:13px;color:#5C5C5C}
.chipx{animation:chipin 7s infinite;animation-delay:calc(var(--r)*.2s + .8s)}
/* bento */
.bento{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;margin-top:64px}
.bx{position:relative;border-radius:30px;background:var(--soft);padding:36px;overflow:hidden;min-height:330px;transition:transform .5s cubic-bezier(.2,.8,.2,1),box-shadow .5s}
.bx:hover{transform:translateY(-8px) scale(1.01);box-shadow:0 30px 70px rgba(0,0,0,.14)}
.bx h3{font-size:32px;line-height:36px;font-weight:700;letter-spacing:-.03em;max-width:330px}
.bx p{margin-top:12px;font-size:18px;line-height:26px;color:var(--mut);max-width:330px;font-weight:500}
.bx.s2{grid-column:span 2}.bx.s3{grid-column:span 3}.bx.s4{grid-column:span 4}
.bx.k{background:#000;color:#F5F5F7}.bx.k p{color:#A1A1A6}
.orbit{position:absolute;right:70px;top:50%;margin-top:-130px;width:260px;height:260px;animation:spin 22s linear infinite}
.orbit>span{position:absolute;left:50%;top:50%;margin:-34px 0 0 -34px;width:68px;height:68px}
.ic{display:block;width:68px;height:68px;background-position:center;background-size:contain;background-repeat:no-repeat;filter:drop-shadow(0 10px 10px rgba(0,0,0,.16))}
.orbit>span>span{display:block;animation:spin 22s linear infinite reverse}
.ring{position:absolute;border-radius:50%;border:2px solid rgba(255,255,255,.5);left:50%;top:50%;animation:ringout 3.6s ease-out infinite}
.lockbox{position:absolute;right:36px;bottom:30px;width:150px;height:150px;display:flex;align-items:center;justify-content:center}
.devs{position:absolute;right:24px;bottom:0;display:flex;align-items:flex-end;gap:14px}
.mini-lap{width:210px;height:140px;border-radius:12px 12px 0 0;background:#0A0A0A;padding:6px;animation:float 6s ease-in-out infinite}
.mini-lap div{width:100%;height:100%;background:#fff;border-radius:6px;padding:10px;display:flex;flex-direction:column;gap:6px}
.mini-lap i{display:block;height:8px;border-radius:4px;background:#E6E6E6;overflow:hidden}
.mini-lap i b{display:block;height:8px;border-radius:4px;animation:growx 6s infinite;transform-origin:left}
.mini-ph{width:70px;height:130px;border-radius:14px;background:#0A0A0A;padding:4px;animation:float 5s -2s ease-in-out infinite}
.mini-ph div{height:100%;border-radius:10px;background:#fff;padding:8px 6px;display:flex;flex-direction:column;gap:5px}
.mini-ph i{display:block;height:6px;border-radius:3px;background:#E6E6E6}
.free{position:absolute;right:30px;bottom:22px;font-size:120px;line-height:1;font-weight:700;letter-spacing:-.05em;color:#fff;opacity:.95;animation:pulse 3s ease-in-out infinite}
.wave{position:absolute;left:0;right:0;bottom:0;height:140px;opacity:.9}
/* privacy */
.priv{display:grid;grid-template-columns:1fr 1fr;gap:72px;align-items:center}
.priv h2{margin-top:10px}
.priv .txt p.sub{margin-top:22px;max-width:480px}
.lockwrap{position:relative;height:440px;display:flex;align-items:center;justify-content:center}
.lockwrap .ring{border-color:rgba(125,162,255,.6);animation-duration:4.8s}
.lockimg{position:relative;z-index:2;width:560px;height:373px;background:var(--i-lock) center/100% 100% no-repeat;mix-blend-mode:screen;animation:float 7s ease-in-out infinite}
.pl{list-style:none;margin:34px 0 0;padding:0;display:flex;flex-direction:column;gap:20px}
.pl li{display:flex;gap:16px;align-items:flex-start;font-size:19px;line-height:26px;color:#A1A1A6;font-weight:500}
.pl li b{display:block;color:#F5F5F7;font-weight:600}
.pl li i{width:36px;height:36px;border-radius:18px;background:#1C1C1F;display:flex;align-items:center;justify-content:center;flex:none}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:70px;position:relative}
.steps::before{content:"";position:absolute;left:12%;right:12%;top:34px;height:2px;background:linear-gradient(90deg,var(--ink) 50%,transparent 50%) 0 0/12px 2px;opacity:.25}
.stp{text-align:center;position:relative}
.stp .n{width:68px;height:68px;border-radius:50%;background:var(--ink);color:#fff;margin:0 auto;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700;animation:stepglow 6s infinite;animation-delay:calc(var(--k)*2s)}
.stp h3{margin-top:22px;font-size:26px;font-weight:700;letter-spacing:-.02em}
.stp p{margin:8px auto 0;max-width:280px;font-size:18px;line-height:26px;color:var(--mut);font-weight:500}
/* cta */
.cta2{max-width:1120px;margin:0 auto;border-radius:40px;min-height:560px;position:relative;overflow:hidden;background:#EEEFF4;display:flex;align-items:center}
.cta2::before{content:"";position:absolute;inset:0;background:var(--i-save) right 36%/auto 125% no-repeat;animation:kb 22s ease-in-out infinite alternate;transform-origin:72% 60%}
.cta2::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#EEEFF4 0,rgba(238,239,244,0) 40%)}
.c2-txt{position:relative;z-index:2;padding:0 72px;max-width:600px;text-align:left}
.c2-txt .sub{margin-top:16px;max-width:440px}
.c2-txt .btn{margin-top:34px}
/* real life */
.life{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:64px}
.ph{margin:0;position:relative;border-radius:30px;overflow:hidden;height:540px;background:#E9E9EE}
.ph .img{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat;animation:kb 18s ease-in-out infinite alternate}
.ph .img.cafe{background-image:var(--i-cafe);background-position:50% 40%}
.ph .img.woman{background-image:var(--i-woman);background-position:80% 50%;animation-delay:-9s}
.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.64),transparent 52%)}
.ph figcaption{position:absolute;left:30px;right:30px;bottom:28px;z-index:2;color:#fff}
.ph figcaption b{display:block;font-size:30px;line-height:34px;font-weight:700;letter-spacing:-.03em}
.ph figcaption span{display:block;margin-top:8px;font-size:17px;line-height:24px;color:rgba(255,255,255,.84);font-weight:500}
/* laptop */
.lapwrap{display:flex;justify-content:center;margin-top:56px}
.lap{position:relative;width:1000px;height:629px;border-radius:36px;overflow:hidden;background:var(--i-laptop) center/100% 100% no-repeat;box-shadow:0 40px 90px rgba(0,0,0,.14)}
.lscr{position:absolute;left:21.54%;top:8.375%;width:56.45%;height:56.1%;overflow:hidden;background:#fff;border-radius:3px}
.dash{width:800px;height:499px;transform:scale(.7056);transform-origin:0 0;display:flex;background:#fff;font-size:14px;color:#111}
.d-sb{width:150px;border-right:1px solid #E6E6E6;padding:18px 12px;display:flex;flex-direction:column;gap:6px;flex:none}
.d-br{display:flex;align-items:center;gap:8px;font-weight:700;font-size:14px;margin-bottom:14px}
.d-br i{width:22px;height:22px;border-radius:7px;background:#0A0A0A;display:flex;align-items:center;justify-content:center}
.d-nv{display:flex;align-items:center;gap:8px;height:34px;padding:0 10px;border-radius:10px;font-weight:500;color:#424245}
.d-nv.on{background:#0A0A0A;color:#fff;font-weight:600}
.d-mn{flex:1;padding:20px 24px;min-width:0}
.d-mn small{display:block;color:#5C5C5C;font-size:13px}
.d-mn h4{margin:2px 0 14px;font-size:22px;line-height:28px;font-weight:700;letter-spacing:-.02em}
.d-st{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.d-c{border:1px solid #E6E6E6;border-radius:14px;padding:12px 14px}
.d-c.k{background:#0A0A0A;color:#fff;border-color:#0A0A0A}.d-c.k small{color:#CFCFCF}
.d-c b{display:block;margin-top:4px;font-size:22px;line-height:26px;font-weight:700;letter-spacing:-.02em}
.d-h{margin:16px 0 4px;font-size:15px;font-weight:700}
.d-mn .rb{margin-top:10px;font-size:14px}.d-mn .rb .nm{width:72px}.d-mn .rb em{width:80px}
/* ctas */
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.07)}}
@keyframes hbdrift{from{transform:translateX(-1.6%) scale(1.02)}to{transform:translateX(1.6%) scale(1.05)}}
.foot{padding:34px 0 48px;font-size:13px;line-height:20px;color:#6E6E73}
.foot .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;border-top:1px solid #D2D2D7;padding-top:22px}
.foot nav{display:flex;gap:22px}
/* reveal */
@supports (animation-timeline:view()){
 .rv{animation:reveal linear both;animation-timeline:view();animation-range:entry 0% entry 45%}
 .px{animation:parallax linear both;animation-timeline:view();animation-range:cover 0% cover 100%}
}
@keyframes reveal{from{opacity:0;transform:translateY(60px) scale(.97)}to{opacity:1;transform:none}}
@keyframes parallax{from{transform:translateY(40px)}to{transform:translateY(-40px)}}
@keyframes rise{from{opacity:0;transform:translateY(34px)}to{opacity:1;transform:none}}
@keyframes phoneIn{from{opacity:0;transform:translateY(120px) scale(.9)}to{opacity:1;transform:none}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-16px)}}
@keyframes drift{from{transform:translate(0,0) scale(1)}to{transform:translate(70px,-50px) scale(1.2)}}
@keyframes sheen{0%,60%{transform:translateX(-120%)}100%{transform:translateX(120%)}}
@keyframes marq{to{transform:translateX(-50%)}}
@keyframes odo{0%{transform:translateY(0)}16%,90%{transform:translateY(calc(var(--d)*-1em))}100%{transform:translateY(calc(var(--d)*-1em))}}
@keyframes fillx{0%{transform:scaleX(0)}20%,100%{transform:scaleX(1)}}
@keyframes growx{0%{transform:scaleX(0)}22%,100%{transform:scaleX(1)}}
@keyframes slidein{0%{opacity:0;transform:translateX(30px)}14%,100%{opacity:1;transform:none}}
@keyframes ping{0%,100%{transform:scale(1)}50%{transform:scale(1.07)}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.04)}}
@keyframes typing{0%{width:0}22%,100%{width:3ch}}
@keyframes caret{50%{border-color:transparent}}
@keyframes tilesel{0%,16%{border:2px solid #2457D6;background:#E6EDFC;color:#2457D6;transform:scale(1.04)}17%,100%{border:1px solid #E6E6E6;background:#fff;color:#0A0A0A;transform:none}}
@keyframes press{0%,60%{transform:none}64%{transform:scale(.96)}68%,100%{transform:none}}
@keyframes toast{0%,64%{opacity:0;transform:translate(-50%,24px)}72%,92%{opacity:1;transform:translate(-50%,-110px)}100%{opacity:0;transform:translate(-50%,-110px)}}
@keyframes filedrop{0%{transform:translateY(-30px) rotate(-6deg);opacity:0}8%{opacity:1}30%{transform:translateY(100px) rotate(0)}38%,100%{transform:translateY(100px) scale(.9);opacity:0}}
@keyframes dropglow{0%,20%{border-color:#4A4A4F}30%,40%{border-color:#7DA2FF;background:rgba(125,162,255,.08)}60%,100%{border-color:#4A4A4F;background:transparent}}
@keyframes implist{0%,36%{opacity:0;transform:translateY(16px)}46%,92%{opacity:1;transform:none}100%{opacity:0}}
@keyframes chipin{0%,10%{opacity:0;transform:scale(.7)}22%,100%{opacity:1;transform:none}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes ringout{0%{width:170px;height:170px;margin:-85px 0 0 -85px;opacity:.9}100%{width:520px;height:520px;margin:-260px 0 0 -260px;opacity:0}}
@keyframes stepglow{0%,28%,100%{box-shadow:0 0 0 0 rgba(36,87,214,0);transform:none}10%{box-shadow:0 0 0 14px rgba(36,87,214,.18);transform:scale(1.1)}}
@media (max-width:820px){
 .nav-links{display:none}
 .h-xl{font-size:46px;line-height:50px}.h-l{font-size:38px;line-height:42px}.sub{font-size:19px;line-height:27px}.eyebrow{font-size:16px}
 .sec{padding:84px 0}.wrap{padding:0 20px}
 .stage{height:610px;margin-top:36px}.stage .phone{transform-origin:top center;width:330px;height:582px;margin-left:-165px}
 .phone .scr .in{transform:scale(.646)}.phone .isl{top:35px;width:66px;height:19px;margin-left:-33px}.phone .scr{border-radius:28px}
 .hb{width:260%;left:-80%}
 .fl.a,.fl.d,.fl.c,.fl.b{display:none}.fl.e{margin-left:62px;top:-14px;transform:scale(.8)}
 .life{grid-template-columns:1fr;margin-top:40px}.ph{height:420px}.ph figcaption b{font-size:26px;line-height:30px}
 .lap{width:350px;height:220px;border-radius:22px}.dash{transform:scale(.247)}.lapwrap{margin-top:36px}
 .lockimg{width:360px;height:240px}
 .cta2{margin:0 16px;border-radius:30px;min-height:690px;align-items:flex-start}.cta2::after{display:none}.cta2::before{background-size:auto 54%;background-position:right bottom;transform-origin:80% 100%;-webkit-mask-image:linear-gradient(transparent 46%,#000 64%);mask-image:linear-gradient(transparent 46%,#000 64%)}
 .c2-txt{padding:60px 24px 0;text-align:center}.c2-txt .sub{margin-left:auto;margin-right:auto}
 .feat,.priv{grid-template-columns:1fr;gap:40px}.feat.flip .txt{order:0}
 .panel{padding:22px;border-radius:26px}
 .bento{grid-template-columns:1fr}.bx.s2,.bx.s3,.bx.s4{grid-column:auto}.bx{padding:28px;min-height:300px}.bx h3{font-size:26px;line-height:30px}
 .steps{grid-template-columns:1fr;gap:44px}.steps::before{display:none}
 .cta{border-radius:30px;padding:72px 20px;margin:0 16px}
 .lockwrap{height:340px}.orbit{right:50%;margin-right:-130px;top:auto;bottom:10px;margin-top:0}.devs{transform:scale(.8);transform-origin:right bottom}.bx.s4{min-height:360px}.bx.cat{min-height:540px}
 .typed{font-size:36px}.rep-top .big{font-size:34px}
 .link{font-size:17px}.btn{height:50px;font-size:16px}
}
@media (prefers-reduced-motion:reduce){.lp *,.lp *::before,.lp *::after{animation:none!important;transition:none!important}.tile:first-child{border:2px solid #2457D6;background:#E6EDFC;color:#2457D6}.toast,.file{display:none}}
'''

def phone_home():
    rows=[('food','Swiggy','Food - UPI - Today','412'),('bus','Metro card top-up','Travel - UPI - Today','500'),('oth','Gift for a friend','Others - Cash - 1 Nov','700')]
    r=''
    for i,(k,n,s,a) in enumerate(rows):
        r+=f'<div class="a-row" style="--r:{i+3}">{cc(k,40,20)}<div><b>{n}</b><span class="s">{s}</span></div><em style="color:{RED}">-₹{a}</em></div>'
    return f'''<div class="in"><div class="a-h"><small>This month</small><b>November 2026</b></div>
<div class="a-card"><small>Spent so far</small><div class="big">{odo('₹37,280')}</div><div class="track"><i></i></div>
<div style="margin-top:16px;padding-top:16px;border-top:1px solid rgba(255,255,255,.28);display:flex;gap:16px"><div style="flex:1"><small>Received</small><div style="font-size:18px;font-weight:700">₹62,000</div></div><div style="flex:1"><small>Left this month</small><div style="font-size:18px;font-weight:700">₹24,720</div></div></div></div>
<div class="a-sec">Needs attention<span>See all budgets</span></div>
<div class="a-list" style="padding:14px 16px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font-size:16px">Travel</b>{status('over','Over by ₹600')}</div><div class="track" style="margin-top:10px"><i style="width:100%;background:#B3361A"></i></div><div style="margin-top:8px;font-size:13px;color:#5C5C5C">₹5,100 of ₹4,500</div></div>
<div class="a-sec">Recent<span>See all</span></div><div class="a-list">{r}</div></div>'''
def phone(inner): return f'<div class="phone"><div class="isl"></div><div class="scr">{inner}</div></div>'

def tag(k,txt,amt=None,col=INK):
    a=f' <em style="color:{col}">{amt}</em>' if amt else ''
    return f'<span class="tag">{cc(k,34,17)}{txt}{a}</span>'
def marquee():
    r1=[('food','Food'),('home','Rent'),('bus','Travel'),('bag','Shopping'),('bill','Bills'),('oth','Others')]
    r2=[('food','Swiggy','-₹412'),('bus','Metro card','-₹500'),('inc','Salary','+₹62,000'),('bill','Electricity','-₹1,860'),('bag','Clothes','-₹2,140'),('food','Groceries','-₹1,240'),('home','Rent','-₹15,000')]
    a=''.join(tag(k,t) for k,t in r1)*2
    b=''.join(tag(k,t,amt,GRN if amt.startswith('+') else RED) for k,t,amt in r2)*2
    return f'<div class="marq"><div class="mq-row">{a}{a}</div><div class="mq-row rev">{b}{b}</div></div>'

def add_demo():
    tiles=[('food','Food'),('home','Rent'),('bus','Travel'),('bag','Shopping'),('bill','Bills'),('oth','Others')]
    t=''.join(f'<div class="tile" style="--k:{i}">{ico(k,22,CAT[k][1])}{n}</div>' for i,(k,n) in enumerate(tiles))
    return f'''<div class="panel w rv" style="padding-bottom:36px"><div class="f-lbl">Amount</div><div class="amt"><span class="r">₹</span><span class="typed">450</span></div><div class="f-lbl" style="margin-bottom:8px">Category</div><div class="tiles">{t}</div><div class="savebtn">Save transaction</div><div class="toast">{ico('check',20,GRN,'2.5')}Saved to Food</div></div>'''
def import_demo():
    rows=[('food','Swiggy','-₹412'),('bus','Metro card','-₹500'),('bill','Electricity','-₹1,860'),('home','Rent','-₹15,000')]
    r=''.join(f'<div class="imp-r" style="--r:{i+2}">{cc(k,30,15)}{n}<b>Sorted</b><em>{a}</em></div>' for i,(k,n,a) in enumerate(rows))
    return f'''<div class="panel k rv"><div class="drop"><div class="file">{ico('list',20,INK)}HDFC_statement.csv</div>Drop your statement here</div><div class="imp">{r}</div><div class="count"><span>Added to your month</span><strong>148 transactions</strong></div></div>'''
def report_demo():
    cats=[('home','Rent','₹15,000','36%',36,'#2457D6'),('food','Food','₹11,400','27%',27,'#E07A1F'),('bus','Travel','₹5,300','13%',13,'#0E8FA0'),('bag','Shopping','₹4,300','10%',10,'#8A3FC7'),('bill','Bills','₹3,300','8%',8,'#C23B7A'),('oth','Others','₹2,560','6%',6,'#6B7785')]
    b=''.join(f'<div class="rb">{cc(k,30,15)}<span class="nm">{n}</span><div class="track"><i style="--r:{i};width:{min(p*2.4,100)}%;background:{c}"></i></div><em>{a}</em></div>' for i,(k,n,a,pc,p,c) in enumerate(cats))
    return f'''<div class="panel s rv"><div class="rep-top"><div><small>You spent in October</small><div class="big">{odo('₹41,860')}</div></div><span class="up">{ico('up',14,INK,'2.25')}₹2,480 more</span></div><div style="padding:6px 4px 0">{b}</div><div class="note"><b>What changed.</b> Food went up by ₹1,900 and ended ₹1,400 over budget. Try about ₹2,300 a week.</div></div>'''
def budgets_demo():
    items=[('home','Rent','ok','On track','₹15,000 of ₹15,000',100,'#1B7F4B'),('bus','Travel','over','Over by ₹600','₹5,100 of ₹4,500',100,'#B3361A'),('bag','Shopping','warn','Almost at limit','₹4,800 of ₹5,000',96,'#B8700A'),('food','Food','ok','On track','₹8,200 of ₹10,000',82,'#1B7F4B')]
    o=''
    for i,(k,n,st,t,cap,p,c) in enumerate(items):
        o+=f'<div class="bg"><div class="bg-h"><div class="l">{cc(k,34,17)}{n}</div><span class="chipx" style="--r:{i}">{status(st,t)}</span></div><div class="track"><i style="--r:{i};width:{p}%;background:{c}"></i></div><small>{cap}</small></div>'
    return f'<div class="panel s rv">{o}</div>'

def life():
    return '''<section class="sec soft"><div class="wrap"><div class="rv" style="text-align:center"><div class="eyebrow">Real life</div><h2 class="h-l" style="margin-top:10px">Made for real months.</h2></div>
<div class="life rv"><figure class="ph"><div class="img cafe" role="img" aria-label="A man smiling at his phone in a cafe"></div><figcaption><b>Check your month over coffee.</b><span>Add a spend in ten seconds, wherever you are.</span></figcaption></figure><figure class="ph"><div class="img woman" role="img" aria-label="A woman at her desk, smiling"></div><figcaption><b>Your first salary deserves a plan.</b><span>Set a budget and watch it work all month.</span></figcaption></figure></div></div></section>
'''
def dash():
    nav=[('home','Home',1),('list','Transactions',0),('bars','Budgets',0),('up','Reports',0)]
    n=''.join(f'<div class="d-nv{" on" if on else ""}">{ico(k,16,"#fff" if on else "#424245")}{t}</div>' for k,t,on in nav)
    cats=[('home','Rent','₹15,000',36,'#2457D6'),('food','Food','₹11,400',27,'#E07A1F'),('bus','Travel','₹5,300',13,'#0E8FA0'),('bag','Shopping','₹4,300',10,'#8A3FC7')]
    b=''.join(f'<div class="rb">{cc(k,26,13)}<span class="nm">{t}</span><div class="track"><i style="--r:{i};width:{min(p*2.4,100)}%;background:{c}"></i></div><em>{a}</em></div>' for i,(k,t,a,p,c) in enumerate(cats))
    return f'''<div class="dash"><div class="d-sb"><div class="d-br"><i>{ico('bars',13,'#fff','2.5')}</i>Expenses</div>{n}</div>
<div class="d-mn"><small>November 2026</small><h4>Good evening</h4>
<div class="d-st"><div class="d-c k"><small>Spent so far</small><b>{odo('₹37,280')}</b></div><div class="d-c"><small>Received</small><b style="color:{GRN}">₹62,000</b></div><div class="d-c"><small>Left this month</small><b>₹24,720</b></div></div>
<div class="d-h">Where your money is going</div>{b}
<div class="d-h" style="margin-top:14px">Needs attention</div><div class="d-c" style="padding:10px 14px"><div style="display:flex;justify-content:space-between;align-items:center;font-weight:600"><span>Travel</span>{status('over','Over by ₹600')}</div><div class="track" style="margin-top:8px"><i style="width:100%;background:#B3361A;animation:none"></i></div></div></div></div>'''
def web():
    return f'''<section class="sec"><div class="wrap"><div class="rv" style="text-align:center"><div class="eyebrow">On the web</div><h2 class="h-l" style="margin-top:10px">Your month, on a bigger screen.</h2><p class="sub" style="margin:18px auto 0;max-width:600px">Open it in any browser to review your report and budgets. It stays in sync with your phone.</p></div>
<div class="lapwrap rv"><div class="lap" role="img" aria-label="Expenses Tracker open on a laptop"><div class="lscr">{dash()}</div></div></div></div></section>
'''

def page(width,mobile=False):
    star=ico('plus',20,'#fff')
    hero=f'''<header class="nav"><div class="wrap"><a class="brand" href="#top"><i>{ico('bars',16,'#fff','2.5')}</i>Expenses Tracker</a><nav class="nav-links" aria-label="Sections"><a href="#features">Features</a><a href="#steps">How it works</a><a href="#privacy">Privacy</a></nav><a class="pill" href="WebSignIn.dc.html">Sign in</a></div></header>
<section class="hero" id="top"><div class="hb t"></div><div class="hb b"></div>
<div class="wrap"><div class="eyebrow top">Free while in early access</div><h1 class="h-xl">Know where every rupee goes.</h1><p class="sub">Add what you spend. Read a clear report every month. See exactly what to change.</p>
<div class="cta-row"><a class="btn" href="WebSignIn.dc.html">Continue with Google</a><a class="link" href="#features">See how it works {ico('chev_r',20,BLUE,'2.25')}</a></div>
<div class="stage"><div class="fl a"><span style="color:{GRN}">{ico('inc',22,GRN,'2.25')}</span><div>Salary received<small>+₹62,000</small></div></div><div class="fl b ping">{status('over','Travel over by ₹600')}</div><div class="fl c">{cc('food',36,18)}<div>Food<small>₹8,200 this month</small></div></div><div class="fl d">{cc('home',36,18)}<div>Rent paid<small>-₹15,000</small></div></div><div class="fl e">{status('ok','On track')}</div>
{phone(phone_home())}</div></div></section>'''
    body=hero+marquee()
    body+=f'''<section class="sec" id="features"><div class="wrap"><div class="feat"><div class="txt rv"><div class="eyebrow">Add</div><h2 class="h-l">Ten seconds. Done.</h2><p class="sub">Type the amount, tap a category, save. Date and account are already filled in. Spent or received, it works the same way.</p></div>{add_demo()}</div></div></section>
<section class="sec dark"><div class="wrap"><div class="feat flip"><div class="txt rv"><div class="eyebrow">Import</div><h2 class="h-l">Drop in your bank statement.</h2><p class="sub">Download the file from HDFC, SBI, ICICI, Axis or Kotak and drop it in. Every line arrives sorted into a category. You review it before anything is saved.</p></div>{import_demo()}</div></div></section>
<section class="sec"><div class="wrap"><div class="feat"><div class="txt rv"><div class="eyebrow">Report</div><h2 class="h-l">A report that explains itself.</h2><p class="sub">Each month you see what you spent most on, what changed since last month, and one clear thing to try. Plain words, no jargon.</p></div>{report_demo()}</div></div></section>
<section class="sec soft"><div class="wrap"><div class="feat flip"><div class="txt rv"><div class="eyebrow">Budgets</div><h2 class="h-l">Know before you cross the line.</h2><p class="sub">Set a monthly limit for each category. Green means on track, amber means close, red means over. Every status comes with words, so it is clear at a glance.</p></div>{budgets_demo()}</div></div></section>
'''
    import math
    orbit=''.join(f'<span style="transform:translate({round(math.cos(math.radians(a))*108)}px,{round(math.sin(math.radians(a))*108)}px)"><span><i class="ic" style="background-image:var(--i-ic-{k})"></i></span></span>' for a,k in [(-90,'food'),(-30,'home'),(30,'bus'),(90,'bag'),(150,'bill'),(210,'oth')])
    orbit=f'<div class="orbit">{orbit}</div>'
    bento=f'''<section class="sec"><div class="wrap"><div class="rv" style="text-align:center"><div class="eyebrow">Everything in one place</div><h2 class="h-l" style="margin-top:10px">Made for everyday money.</h2></div>
<div class="bento rv">
<div class="bx s4 cat"><h3>Your categories, your colours.</h3><p>Food, Rent, Travel, Shopping, Bills and Others come ready. Each has its own colour, so your month reads at a glance.</p>{orbit}</div>
<div class="bx s2 k"><h3>Free for now.</h3><p>No cards. No trial timer.</p><div class="free">₹0</div></div>
<div class="bx s2"><h3>Rupees and English.</h3><p>Built for how India spends. Amounts, dates and words you already know.</p></div>
<div class="bx s4"><h3>On your phone and on the web.</h3><p>Add a coffee on the bus, review the month at your desk. Everything stays in sync.</p><div class="devs"><div class="mini-lap"><div><i><b style="width:80%;background:#2457D6"></b></i><i><b style="width:55%;background:#E07A1F"></b></i><i><b style="width:35%;background:#0E8FA0"></b></i><i><b style="width:20%;background:#8A3FC7"></b></i></div></div><div class="mini-ph"><div><i style="background:#0A0A0A;height:34px;border-radius:6px"></i><i></i><i></i><i></i></div></div></div></div>
</div></div></section>
<section class="sec dark" id="privacy"><div class="wrap"><div class="priv"><div class="txt rv"><div class="eyebrow">Privacy</div><h2 class="h-l">Your money stays yours.</h2><p class="sub">We never ask for your bank password. You sign in with Google, and you decide what goes in.</p>
<ul class="pl"><li><i>{ico('lock',18,'#fff')}</i><div><b>No bank passwords. Ever.</b>Upload a statement file instead.</div></li><li><i>{ico('check',18,'#fff','2.25')}</i><div><b>You review every line.</b>Nothing is saved until you say so.</div></li><li><i>{ico('user',18,'#fff')}</i><div><b>Just you.</b>One account, one private month.</div></li></ul></div>
<div class="lockwrap rv"><div class="ring" style="animation-delay:0s"></div><div class="ring" style="animation-delay:1.2s"></div><div class="ring" style="animation-delay:2.4s"></div><div class="lockimg" role="img" aria-label="A padlock"></div></div></div></div></section>
<section class="sec" id="steps"><div class="wrap"><div class="rv" style="text-align:center"><div class="eyebrow">How it works</div><h2 class="h-l" style="margin-top:10px">Three steps. That is all.</h2></div>
<div class="steps rv"><div class="stp" style="--k:0"><div class="n">1</div><h3>Sign in</h3><p>Continue with Google. No forms, no new password.</p></div><div class="stp" style="--k:1"><div class="n">2</div><h3>Add or import</h3><p>Type a spend, or drop in a bank statement.</p></div><div class="stp" style="--k:2"><div class="n">3</div><h3>Read your report</h3><p>See where it went and what to change next month.</p></div></div></div></section>
<section style="padding:0 0 110px"><div class="cta2 rv"><div class="c2-txt"><h2 class="h-l">Start with this month.</h2><p class="sub">It takes less than a minute to begin, and it is free.</p><a class="btn" href="WebSignIn.dc.html">Continue with Google</a></div></div></section>
<footer class="foot"><div class="wrap"><div>Expenses Tracker. Amounts shown are sample data.</div><nav aria-label="Footer"><a href="#">Terms</a><a href="#">Privacy Policy</a><a href="#">Contact</a></nav></div></footer>'''
    marker='<section class="sec dark" id="privacy">'
    assert marker in bento
    body+=bento.replace(marker,life()+web()+marker,1)
    return f'<div class="lp" style="width:{width}px">{body}</div>'

def build(name,width,height,title):
    css=CSS+'.lp{'+assets.css_vars()+'}'
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:inherit;text-decoration:none}}
{css}
</style>
</helmet>
{page(width)}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{width},"height":{height}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    open(OUT+name,'w').write(html)
if __name__=='__main__':
    H1=int(sys.argv[1]) if len(sys.argv)>1 else 5200
    H2=int(sys.argv[2]) if len(sys.argv)>2 else 7600
    build('Landing.dc.html',1440,H1,'Landing page')
    build('LandingMobile.dc.html',390,H2,'Landing page mobile')
    print('ok')
