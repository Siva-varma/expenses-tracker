import os
OUT='/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/expenses-design/project/'
W,H=1280,860
INK='#111111';MUT='#5C5C5C';BRD='#E6E6E6';BLUE='#2457D6';BLT='#E6EDFC';GRN='#1B7F4B';GLT='#E1F3E8';RED='#B3261E'
IC={
'food':'<path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 0 0 2-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 0 0-5 5v6c0 1.1.9 2 2 2h3Zm0 0v7"/>',
'home':'<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .709-1.528l7-5.999a2 2 0 0 1 2.582 0l7 5.999A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
'bus':'<path d="M8 6v6"/><path d="M15 6v6"/><path d="M2 12h19.6"/><path d="M18 18h3s.5-1.7.8-2.8c.1-.4.2-.8.2-1.2 0-.4-.1-.8-.2-1.2l-1.4-5C20.1 6.8 19.1 6 18 6H4a2 2 0 0 0-2 2v10h3"/><circle cx="7" cy="18" r="2"/><path d="M9 18h5"/><circle cx="16" cy="18" r="2"/>',
'bag':'<path d="M16 10a4 4 0 0 1-8 0"/><path d="M3.103 6.034h17.794"/><path d="M3.4 5.467a2 2 0 0 0-.4 1.2V20a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6.667a2 2 0 0 0-.4-1.2l-2-2.667A2 2 0 0 0 17 2H7a2 2 0 0 0-1.6.8z"/>',
'bill':'<path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M14 8H8"/><path d="M16 12H8"/><path d="M13 16H8"/>',
'oth':'<circle cx="12" cy="12" r="10"/><path d="M17 12h.01"/><path d="M12 12h.01"/><path d="M7 12h.01"/>',
'inc':'<path d="M17 7 7 17"/><path d="M17 17H7V7"/>',
'wallet':'<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/>',
'chart':'<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
'list':'<path d="M3 12h.01"/><path d="M3 18h.01"/><path d="M3 6h.01"/><path d="M8 12h13"/><path d="M8 18h13"/><path d="M8 6h13"/>',
'user':'<circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/>',
'plus':'<path d="M12 5v14M5 12h14"/>',
'upload':'<path d="M12 16V5M7.5 9.5 12 5l4.5 4.5M5 19h14"/>',
'search':'<circle cx="11" cy="11" r="6"/><path d="m20 20-4-4"/>',
'chev_d':'<path d="m6 9 6 6 6-6"/>',
'chev_l':'<path d="m15 6-6 6 6 6"/>',
'chev_r':'<path d="m9 6 6 6-6 6"/>',
'check':'<path d="m5 12.5 4.5 4.5L19 7.5"/>',
'alert':'<circle cx="12" cy="12" r="8.5"/><path d="M12 8v5M12 16h.01"/>',
'lock':'<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
'x':'<path d="M6 6l12 12M18 6 6 18"/>',
'up':'<path d="M12 19V5M6 11l6-6 6 6"/>',
'bars':'<path d="M6 19v-5M12 19V9M18 19V5"/>',
'cal':'<rect x="4" y="5.5" width="16" height="14" rx="2"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
}
CAT={'food':('#FCEBDA','#B85A0B','#E07A1F','Food'),'home':('#E6EDFC','#2457D6','#2457D6','Rent'),'bus':('#DDF2F5','#0B7684','#0E8FA0','Travel'),
     'bag':('#F1E5FA','#7A2FB5','#8A3FC7','Shopping'),'bill':('#FAE4EE','#A82D66','#C23B7A','Bills'),'oth':('#ECEFF3','#4A5568','#6B7785','Others'),
     'inc':(GLT,GRN,GRN,'Income')}
def ico(n,s=20,c='currentColor',sw='1.75'):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none">{IC[n]}</svg>'
def cc(k,size=40,isz=20):
    t,c,_,_=CAT[k]
    return f'<span style="width: {size}px; height: {size}px; border-radius: {size//2}px; background: {t}; display: inline-flex; align-items: center; justify-content: center; flex: none">{ico(k,isz,c)}</span>'
def chip(k):
    t,c,_,n=CAT[k]
    return f'<span style="display: inline-flex; align-items: center; height: 26px; padding: 0 10px; border-radius: 13px; background: {t}; color: {c}; font-size: 13px; font-weight: 600">{n}</span>'
def status(kind,text):
    m={'ok':(GLT,GRN,'check'),'warn':('#FBF0DC','#7A4A00','alert'),'over':('#FBE9E4','#9A2A12','alert')}[kind]
    return f'<span style="display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px 3px 8px; border-radius: 999px; background: {m[0]}; color: {m[1]}; font-size: 13px; line-height: 18px; font-weight: 600; white-space: nowrap">{ico(m[2],14,"currentColor","2.25")}{text}</span>'
def bar(pct,color,label,h=8):
    return f'<div role="img" aria-label="{label}" style="height: {h}px; border-radius: {h//2}px; background: {BRD}"><div style="width: {min(pct,100)}%; height: {h}px; border-radius: {h//2}px; background: {color}"></div></div>'
def card(inner,pad='20px',extra=''):
    return f'<section style="background: #FFFFFF; border: 1px solid {BRD}; border-radius: 16px; padding: {pad}; {extra}">{inner}</section>'
def h2(t,i=''):
    return f'<h2 {("id=%s"%i) if i else ""} style="margin: 0; font-size: 18px; line-height: 24px; font-weight: 700">{t}</h2>'
def btn_dark(label,href,icon=None,h=48,w=''):
    return f'<a href="{href}" style="height: {h}px; {w} box-sizing: border-box; padding: 0 20px; border-radius: 14px; background: {INK}; color: #FFFFFF; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 16px; font-weight: 600">{ico(icon,20) if icon else ""}{label}</a>'
def btn_out(label,href,icon=None,h=44):
    return f'<a href="{href}" style="height: {h}px; box-sizing: border-box; padding: 0 18px; border: 1.5px solid {INK}; border-radius: 22px; background: #FFFFFF; color: {INK}; display: inline-flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 600">{ico(icon,18) if icon else ""}{label}</a>'
def link(label,href,size=14):
    return f'<a href="{href}" style="min-height: 44px; display: inline-flex; align-items: center; font-size: {size}px; font-weight: 600; color: {BLUE}">{label}</a>'

NAV=[('home','Home','WebHome.dc.html'),('list','Transactions','WebTransactions.dc.html'),('wallet','Budgets','WebBudgets.dc.html'),('chart','Reports','WebReport.dc.html'),('upload','Import statement','WebImport.dc.html')]
def sidebar(active):
    items=''
    for k,l,h in NAV:
        on=(l==active)
        items+=f'<a href="{h}" {"aria-current=page" if on else ""} style="height: 44px; box-sizing: border-box; padding: 0 12px; border-radius: 12px; display: flex; align-items: center; gap: 12px; font-size: 15px; font-weight: {700 if on else 500}; color: {INK if on else MUT}; background: {"#F0F0F0" if on else "transparent"}">{ico(k,20)}{l}</a>'
    return f'''<aside style="width: 240px; flex: none; box-sizing: border-box; border-right: 1px solid {BRD}; padding: 24px 16px; display: flex; flex-direction: column; gap: 24px; background: #FFFFFF">
<div style="display: flex; align-items: center; gap: 10px; padding: 0 4px"><div style="width: 36px; height: 36px; border-radius: 10px; background: {INK}; display: flex; align-items: center; justify-content: center">{ico('bars',20,'#FFFFFF','2.25')}</div><div style="font-size: 16px; line-height: 20px; font-weight: 700">Expenses Tracker</div></div>
{btn_dark('Add transaction','WebAdd.dc.html','plus',48,'width: 100%;')}
<nav aria-label="Main" style="display: flex; flex-direction: column; gap: 4px">{items}</nav>
<div style="margin-top: auto; display: flex; align-items: center; gap: 10px; padding: 8px 4px; border-top: 1px solid {BRD}; padding-top: 16px"><span style="width: 40px; height: 40px; border-radius: 20px; border: 1px solid {BRD}; display: flex; align-items: center; justify-content: center">{ico('user',20)}</span><div><div style="font-size: 15px; line-height: 20px; font-weight: 600">Siva</div><div style="font-size: 13px; line-height: 18px; color: {MUT}">Settings</div></div></div>
</aside>'''
def page(title,body,active=None,overlay='',w=W,h=H,sb=True):
    sbh=sidebar(active) if sb else ''
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
</style>
</helmet>
<div style="width: {w}px; height: {h}px; box-sizing: border-box; position: relative; display: flex; overflow: hidden; background: #FFFFFF; color: {INK}; font-family: 'Inter', system-ui, -apple-system, sans-serif">
{sbh}
{body}
{overlay}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    return html
def main(head_eyebrow,head_title,actions,content,gap=16):
    return f'''<main style="flex: 1; min-width: 0; box-sizing: border-box; padding: 32px 40px 32px; display: flex; flex-direction: column; gap: {gap}px; background: #FAFAFA; overflow: hidden">
<header style="display: flex; align-items: center; justify-content: space-between; min-height: 56px">
<div><div style="font-size: 13px; line-height: 18px; color: {MUT}">{head_eyebrow}</div><h1 style="margin: 0; font-size: 28px; line-height: 34px; font-weight: 700">{head_title}</h1></div>
<div style="display: flex; align-items: center; gap: 12px">{actions}</div>
</header>
{content}
</main>'''
def save(name,html):
    open(OUT+name,'w').write(html)
