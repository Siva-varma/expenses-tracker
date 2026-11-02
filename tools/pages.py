import sys
sys.path.insert(0,'/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/gen')
from web import *

CATS=[('home',15000,40,'Rent'),('food',8200,22,'Food'),('bus',5100,14,'Travel'),('bag',4800,13,'Shopping'),('bill',3480,9,'Bills'),('oth',700,2,'Others')]
def money(n): return '₹{:,}'.format(n)

# ---------- Sign in
left=f'''<section style="flex: 1; min-width: 0; background: {INK}; color: #FFFFFF; padding: 64px; display: flex; flex-direction: column; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 12px"><div style="width: 44px; height: 44px; border-radius: 12px; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ico('bars',24,INK,'2.25')}</div><div style="font-size: 20px; font-weight: 700">Expenses Tracker</div></div>
<div>
<h1 style="margin: 0; font-size: 44px; line-height: 54px; font-weight: 700; max-width: 560px">See where your money goes each month, and take control of it.</h1>
<ul style="list-style: none; margin: 40px 0 0; padding: 0; display: flex; flex-direction: column; gap: 22px">
<li style="display: flex; align-items: center; gap: 16px"><span style="width: 44px; height: 44px; border-radius: 22px; background: #2A2A2A; display: flex; align-items: center; justify-content: center">{ico('plus',22,'#FFFFFF')}</span><div><div style="font-size: 17px; font-weight: 600">Easy to add</div><div style="font-size: 15px; color: #CFCFCF">Type an expense, or upload a bank statement.</div></div></li>
<li style="display: flex; align-items: center; gap: 16px"><span style="width: 44px; height: 44px; border-radius: 22px; background: #2A2A2A; display: flex; align-items: center; justify-content: center">{ico('chart',22,'#FFFFFF')}</span><div><div style="font-size: 17px; font-weight: 600">A clear monthly report</div><div style="font-size: 15px; color: #CFCFCF">Know what you spent most on, and what changed.</div></div></li>
<li style="display: flex; align-items: center; gap: 16px"><span style="width: 44px; height: 44px; border-radius: 22px; background: #2A2A2A; display: flex; align-items: center; justify-content: center">{ico('lock',22,'#FFFFFF')}</span><div><div style="font-size: 17px; font-weight: 600">Private by default</div><div style="font-size: 15px; color: #CFCFCF">We never ask for your bank password.</div></div></li>
</ul></div>
<div style="font-size: 13px; color: #A8A8A8">Rupees and English. Free while we are in early access.</div>
</section>'''
right=f'''<section style="width: 560px; flex: none; display: flex; align-items: center; justify-content: center; background: #FFFFFF">
<div style="width: 380px; display: flex; flex-direction: column; gap: 20px">
<div><h2 style="margin: 0; font-size: 28px; line-height: 34px; font-weight: 700">Welcome</h2><p style="margin: 8px 0 0; font-size: 16px; line-height: 24px; color: {MUT}">Sign in to start tracking your money. It takes less than a minute.</p></div>
<a href="WebHome.dc.html" style="height: 52px; border-radius: 14px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Continue with Google</a>
<p style="margin: 0; font-size: 13px; line-height: 18px; color: {MUT}">By continuing, you agree to the <a href="#" style="color: {INK}; text-decoration: underline">Terms</a> and <a href="#" style="color: {INK}; text-decoration: underline">Privacy Policy</a>.</p>
</div></section>'''
save('WebSignIn.dc.html',page('Web - Sign in',left+right,sb=False))

# ---------- Home
banner=f'''<a href="WebReport.dc.html" style="display: flex; align-items: center; gap: 14px; background: #FFFFFF; border: 1px solid {BRD}; border-radius: 16px; padding: 10px 20px"><span style="width: 40px; height: 40px; border-radius: 20px; background: #F0F0F0; display: flex; align-items: center; justify-content: center; flex: none">{ico('chart',20,INK)}</span><div style="flex: 1"><div style="font-size: 16px; line-height: 22px; font-weight: 600">October report is ready</div><div style="font-size: 14px; line-height: 20px; color: {MUT}">You spent ₹2,480 more than in September.</div></div><span style="font-size: 14px; font-weight: 600; color: {BLUE}">Open report</span></a>'''
stats=f'''<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">
<section style="background: {INK}; color: #FFFFFF; border-radius: 16px; padding: 20px"><div style="font-size: 14px; line-height: 20px; color: #CFCFCF">Spent so far</div><div style="font-size: 36px; line-height: 44px; font-weight: 700; font-variant-numeric: tabular-nums">₹37,280</div><div role="img" aria-label="60 percent of the money received has been spent" style="margin-top: 10px; height: 8px; border-radius: 4px; background: rgba(255,255,255,0.28)"><div style="width: 60%; height: 8px; border-radius: 4px; background: #FFFFFF"></div></div></section>
{card(f'<div style="display: flex; align-items: center; gap: 10px"><span style="width: 32px; height: 32px; border-radius: 16px; background: {GLT}; display: flex; align-items: center; justify-content: center">{ico("inc",18,GRN)}</span><div style="font-size: 14px; line-height: 20px; color: {MUT}">Received</div></div><div style="margin-top: 6px; font-size: 36px; line-height: 44px; font-weight: 700; color: {GRN}; font-variant-numeric: tabular-nums">₹62,000</div>')}
{card(f'<div style="font-size: 14px; line-height: 20px; color: {MUT}">Left this month</div><div style="margin-top: 8px; font-size: 36px; line-height: 44px; font-weight: 700; font-variant-numeric: tabular-nums">₹24,720</div>')}
</div>'''
rows=''
for k,a,p,n in CATS:
    rows+=f'<div style="display: flex; align-items: center; gap: 14px">{cc(k,36,18)}<div style="width: 90px; font-size: 15px; font-weight: 600">{n}</div><div style="flex: 1">{bar(p,CAT[k][2],f"{n}: {p} percent of spending")}</div><div style="width: 150px; text-align: right; font-size: 15px; font-variant-numeric: tabular-nums"><span style="font-weight: 600">{money(a)}</span> <span style="color: {MUT}">{p}%</span></div></div>'
where=card(f'{h2("Where your money is going")}<div style="margin-top: 16px; display: flex; flex-direction: column; gap: 14px">{rows}</div>',extra='flex: 1.5; min-width: 0')
attn=card(f'''<div style="display: flex; align-items: center; justify-content: space-between">{h2("Needs attention")}{link("See all budgets","WebBudgets.dc.html")}</div>
<div style="margin-top: 4px; display: flex; flex-direction: column; gap: 14px">
<div><div style="display: flex; align-items: center; justify-content: space-between"><div style="font-size: 15px; font-weight: 600">Travel</div>{status('over','Over by ₹600')}</div><div style="margin-top: 8px">{bar(100,'#B3361A','Travel budget used: more than 100 percent')}</div><div style="margin-top: 4px; font-size: 13px; color: {MUT}">₹5,100 of ₹4,500</div></div>
<div><div style="display: flex; align-items: center; justify-content: space-between"><div style="font-size: 15px; font-weight: 600">Shopping</div>{status('warn','Almost at limit')}</div><div style="margin-top: 8px">{bar(96,'#B8700A','Shopping budget used: 96 percent')}</div><div style="margin-top: 4px; font-size: 13px; color: {MUT}">₹4,800 of ₹5,000</div></div>
</div>''')
def trow(k,name,sub,amt,recv=False,last=False):
    col=GRN if recv else RED
    sign='+' if recv else '-'
    b='' if last else f'border-bottom: 1px solid {BRD};'
    return f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0; {b}">{cc(k,36,18)}<div style="flex: 1; min-width: 0"><div style="font-size: 15px; line-height: 20px; font-weight: 600">{name}</div><div style="font-size: 13px; line-height: 18px; color: {MUT}">{sub}</div></div><div style="font-size: 15px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums">{sign}{amt}</div></div>'
recent=card(f'''<div style="display: flex; align-items: center; justify-content: space-between">{h2("Recent")}{link("See all","WebTransactions.dc.html")}</div>
{trow('food','Swiggy','Food - UPI - Today','₹412')}{trow('bus','Metro card top-up','Travel - UPI - Today','₹500')}{trow('oth','Gift for a friend','Others - Cash - 1 Nov','₹700',last=True)}''')
cols=f'<div style="display: flex; gap: 16px; align-items: stretch; min-height: 0">{where}<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 16px">{attn}{recent}</div></div>'
save('WebHome.dc.html',page('Web - Home',main('This month','November 2026',btn_out('Import statement','WebImport.dc.html','upload'),banner+stats+cols),'Home'))

# ---------- Transactions content
TX=[('food','Swiggy','Food','UPI','Today','₹412',False),('bus','Metro card top-up','Travel','UPI','Today','₹500',False),
    ('food','Grocery store','Food','Cash','Yesterday','₹1,240',False),('bill','Electricity bill','Bills','HDFC Bank','Yesterday','₹1,860',False),
    ('inc','Salary','Income','HDFC Bank','1 Nov','₹62,000',True),('home','Rent','Rent','HDFC Bank','1 Nov','₹15,000',False),
    ('oth','Gift for a friend','Others','Cash','1 Nov','₹700',False)]
def tx_content():
    tool=card(f'''<div style="display: flex; align-items: center; gap: 12px">
<div style="position: relative; flex: 1"><span style="position: absolute; left: 14px; top: 13px; color: {MUT}">{ico('search',20,MUT)}</span><input type="search" aria-label="Search transactions" placeholder="Search by name or note" style="width: 100%; height: 46px; box-sizing: border-box; padding: 0 14px 0 44px; border-radius: 12px; border: 1px solid #CFCFCF; background: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; color: {INK}"></div>
<div role="group" aria-label="Filter" style="display: flex; gap: 8px"><button type="button" aria-pressed="true" style="height: 40px; padding: 0 16px; border: none; border-radius: 20px; background: {BLUE}; color: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 600">All</button><button type="button" aria-pressed="false" style="height: 40px; box-sizing: border-box; padding: 0 16px; border: 1px solid #CFCFCF; border-radius: 20px; background: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 500; color: {INK}">Spent</button><button type="button" aria-pressed="false" style="height: 40px; box-sizing: border-box; padding: 0 16px; border: 1px solid #CFCFCF; border-radius: 20px; background: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 500; color: {INK}">Received</button></div>
<button type="button" style="height: 46px; box-sizing: border-box; padding: 0 14px; border: 1px solid #CFCFCF; border-radius: 12px; background: #FFFFFF; display: flex; align-items: center; gap: 8px; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 500; color: {INK}">All categories{ico('chev_d',18,MUT)}</button>
<button type="button" style="height: 46px; box-sizing: border-box; padding: 0 14px; border: 1px solid #CFCFCF; border-radius: 12px; background: #FFFFFF; display: flex; align-items: center; gap: 8px; font-family: 'Inter', system-ui, sans-serif; font-size: 15px; font-weight: 500; color: {INK}">{ico('cal',18,MUT)}November 2026{ico('chev_d',18,MUT)}</button>
</div>''',pad='14px 16px')
    head=''.join(f'<div style="{s}font-size: 13px; line-height: 18px; font-weight: 600; color: {MUT}">{t}</div>' for t,s in [('Name','flex: 2.2;'),('Category','flex: 1.2;'),('Account','flex: 1.2;'),('Date','flex: 1;'),('Amount','flex: 1; text-align: right;')])
    body=''
    for i,(k,n,c,a,d,amt,r) in enumerate(TX):
        col=GRN if r else RED; sign='+' if r else '-'
        b='' if i==len(TX)-1 else f'border-bottom: 1px solid {BRD};'
        body+=f'<div style="display: flex; align-items: center; gap: 16px; min-height: 60px; box-sizing: border-box; padding: 10px 20px; {b}"><div style="flex: 2.2; display: flex; align-items: center; gap: 12px; font-size: 15px; font-weight: 600">{cc(k,36,18)}{n}</div><div style="flex: 1.2">{chip(k if k!="inc" else "inc")}</div><div style="flex: 1.2; font-size: 15px; color: {MUT}">{a}</div><div style="flex: 1; font-size: 15px; color: {MUT}">{d}</div><div style="flex: 1; text-align: right; font-size: 15px; font-weight: 600; color: {col}; font-variant-numeric: tabular-nums">{sign}{amt}</div></div>'
    table=f'''<section style="background: #FFFFFF; border: 1px solid {BRD}; border-radius: 16px; overflow: hidden"><div style="display: flex; gap: 16px; padding: 12px 20px; background: #F7F7F7; border-bottom: 1px solid {BRD}">{head}</div>{body}<div style="padding: 12px 20px; border-top: 1px solid {BRD}; font-size: 13px; color: {MUT}">Showing 7 transactions in November 2026</div></section>'''
    return tool+table
save('WebTransactions.dc.html',page('Web - Transactions',main('November 2026','Transactions',btn_out('Import statement','WebImport.dc.html','upload'),tx_content()),'Transactions'))

# ---------- Add drawer
def cat_btn(k,sel):
    t,c,_,n=CAT[k]
    if sel: st=f'border: 2px solid {BLUE}; background: {BLT}; color: {BLUE}; font-weight: 600'; ic=ico(k,22,BLUE)
    else: st=f'border: 1px solid {BRD}; background: #FFFFFF; color: {INK}; font-weight: 500'; ic=ico(k,22,c)
    return f'<button type="button" aria-pressed="{"true" if sel else "false"}" style="height: 72px; box-sizing: border-box; padding: 0; {st}; border-radius: 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; font-family: \'Inter\', system-ui, sans-serif; font-size: 14px">{ic}{n}</button>'
def fieldbtn(label,idn,val,icon):
    return f'<div style="flex: 1; min-width: 0"><div id="{idn}" style="font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}; margin-bottom: 6px">{label}</div><button type="button" aria-labelledby="{idn}" style="width: 100%; height: 48px; box-sizing: border-box; padding: 0 14px; border: 1px solid #CFCFCF; border-radius: 12px; background: #FFFFFF; color: {INK}; display: flex; align-items: center; justify-content: space-between; font-family: \'Inter\', system-ui, sans-serif; font-size: 16px; font-weight: 500">{val}{ico(icon,18,MUT)}</button></div>'
drawer=f'''<div style="position: absolute; inset: 0; background: rgba(17,17,17,0.45)"></div>
<aside role="dialog" aria-label="Add transaction" style="position: absolute; top: 0; right: 0; bottom: 0; width: 440px; box-sizing: border-box; background: #FFFFFF; display: flex; flex-direction: column; box-shadow: -8px 0 32px rgba(0,0,0,0.15)">
<header style="flex: none; padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid {BRD}"><h2 style="margin: 0; font-size: 20px; line-height: 26px; font-weight: 700">Add transaction</h2><a href="WebTransactions.dc.html" aria-label="Close" style="width: 44px; height: 44px; display: flex; align-items: center; justify-content: center">{ico('x',22)}</a></header>
<div style="flex: 1; min-height: 0; padding: 20px 24px; display: flex; flex-direction: column; gap: 16px; overflow: hidden">
<div role="group" aria-label="Type of transaction" style="display: flex; padding: 4px; border-radius: 14px; background: #EFEFEF; gap: 4px"><button type="button" aria-pressed="true" style="flex: 1; height: 44px; border: none; border-radius: 10px; background: {BLUE}; color: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 16px; font-weight: 600">Spent</button><button type="button" aria-pressed="false" style="flex: 1; height: 44px; border: none; border-radius: 10px; background: transparent; color: {INK}; font-family: 'Inter', system-ui, sans-serif; font-size: 16px; font-weight: 500">Received</button></div>
<div style="background: #FFFFFF; border: 1px solid {BRD}; border-radius: 16px; padding: 12px 16px"><label for="amount" style="display: block; font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}">Amount</label><div style="display: flex; align-items: center; gap: 8px"><span aria-hidden="true" style="font-size: 32px; line-height: 48px; font-weight: 600; color: {MUT}">₹</span><input id="amount" type="text" inputmode="numeric" value="450" style="flex: 1; min-width: 0; border: none; outline: none; background: transparent; padding: 0; font-family: 'Inter', system-ui, sans-serif; font-size: 40px; line-height: 48px; font-weight: 700; color: {INK}"></div></div>
<div><div id="cat-label" style="font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}; margin-bottom: 8px">Category</div><div role="group" aria-labelledby="cat-label" style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{cat_btn('food',True)}{cat_btn('home',False)}{cat_btn('bus',False)}{cat_btn('bag',False)}{cat_btn('bill',False)}{cat_btn('oth',False)}</div></div>
<div style="display: flex; gap: 12px">{fieldbtn('Paid from','from-label','Cash','chev_d')}{fieldbtn('Date','date-label','Today','cal')}</div>
<div><label for="note" style="display: block; font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}; margin-bottom: 6px">Note (optional)</label><input id="note" type="text" placeholder="For example, lunch with team" style="width: 100%; height: 48px; box-sizing: border-box; padding: 0 14px; border-radius: 12px; border: 1px solid #CFCFCF; background: #FFFFFF; font-family: 'Inter', system-ui, sans-serif; font-size: 16px; color: {INK}"></div>
</div>
<footer style="flex: none; padding: 16px 24px 24px; display: flex; gap: 12px; border-top: 1px solid {BRD}"><a href="WebTransactions.dc.html" style="height: 52px; padding: 0 24px; box-sizing: border-box; border: 1.5px solid {INK}; border-radius: 14px; display: flex; align-items: center; font-size: 16px; font-weight: 600">Cancel</a><a href="WebTransactions.dc.html" style="flex: 1; height: 52px; border-radius: 14px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 600">Save transaction</a></footer>
</aside>'''
save('WebAdd.dc.html',page('Web - Add transaction',main('November 2026','Transactions',btn_out('Import statement','WebImport.dc.html','upload'),tx_content()),'Transactions',overlay=drawer))

# ---------- Import
def bankchip(n,sel):
    if sel: return f'<button type="button" aria-pressed="true" style="height: 44px; padding: 0 16px; border: 2px solid {BLUE}; border-radius: 22px; background: {BLT}; color: {BLUE}; display: flex; align-items: center; gap: 6px; font-family: \'Inter\', system-ui, sans-serif; font-size: 15px; font-weight: 600">{ico("check",16,BLUE,"2.25")}{n}</button>'
    return f'<button type="button" aria-pressed="false" style="height: 44px; box-sizing: border-box; padding: 0 16px; border: 1px solid #CFCFCF; border-radius: 22px; background: #FFFFFF; color: {INK}; font-family: \'Inter\', system-ui, sans-serif; font-size: 15px; font-weight: 500">{n}</button>'
def step(n,t,d):
    return f'<li style="display: flex; gap: 14px"><span style="width: 32px; height: 32px; border-radius: 16px; background: {INK}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 700; flex: none">{n}</span><div><div style="font-size: 16px; line-height: 22px; font-weight: 600">{t}</div><div style="font-size: 14px; line-height: 20px; color: {MUT}">{d}</div></div></li>'
leftc=card(f'''<p style="margin: 0; font-size: 16px; line-height: 24px; color: {MUT}">Download your statement from your bank, then add it here. We read it once and fill in your transactions for you.</p>
<h2 id="bank-label" style="margin: 24px 0 10px; font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}">1. Choose your bank</h2>
<div role="group" aria-labelledby="bank-label" style="display: flex; flex-wrap: wrap; gap: 8px">{bankchip('HDFC Bank',True)}{bankchip('SBI',False)}{bankchip('ICICI Bank',False)}{bankchip('Axis Bank',False)}{bankchip('Kotak',False)}</div>
<h2 id="file-label" style="margin: 24px 0 10px; font-size: 14px; line-height: 20px; font-weight: 500; color: {MUT}">2. Add the statement file</h2>
<button type="button" style="width: 100%; box-sizing: border-box; padding: 32px 16px; border: 2px dashed #8A8A8A; border-radius: 16px; background: #FFFFFF; color: {INK}; display: flex; flex-direction: column; align-items: center; gap: 8px; font-family: 'Inter', system-ui, sans-serif"><span style="width: 52px; height: 52px; border-radius: 26px; background: #F0F0F0; display: flex; align-items: center; justify-content: center">{ico('upload',26)}</span><span style="font-size: 16px; line-height: 22px; font-weight: 600">Choose a file, or drag it here</span><span style="font-size: 13px; line-height: 18px; color: {MUT}">CSV or Excel file, up to 5 MB</span></button>
<div style="margin-top: 24px; display: flex; justify-content: flex-end">{btn_dark('Review transactions','WebTransactions.dc.html')}</div>''',pad='24px',extra='flex: 1.5; min-width: 0')
rightc=f'''<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 16px">
{card(f'{h2("What happens next")}<ol style="list-style: none; margin: 16px 0 0; padding: 0; display: flex; flex-direction: column; gap: 18px">{step(1,"We read your file","Dates, names and amounts are picked out for you.")}{step(2,"You review the list","Fix a category or remove a line before anything is saved.")}{step(3,"Your report updates","Budgets and the monthly report use the new transactions.")}</ol>')}
{card(f'<div style="font-size: 16px; line-height: 22px; font-weight: 600">Where do I find the file?</div><p style="margin: 4px 0 0; font-size: 14px; line-height: 20px; color: {MUT}">Open your bank website or app, go to Account statement, pick the dates, and download as CSV or Excel.</p>')}
<div style="display: flex; align-items: flex-start; gap: 10px; padding: 0 4px">{ico('lock',20,INK)}<p style="margin: 0; font-size: 13px; line-height: 18px; color: {MUT}">We never ask for your bank password. You can review every transaction before it is saved.</p></div>
</div>'''
save('WebImport.dc.html',page('Web - Import statement',main('Add many at once','Import statement',link('Back to Transactions','WebTransactions.dc.html',15),f'<div style="display: flex; gap: 16px; align-items: flex-start">{leftc}{rightc}</div>',gap=8),'Import statement'))

# ---------- Budgets
BUD=[('home','Rent',15000,15000,'ok','On track'),('food','Food',8200,10000,'ok','On track'),('bus','Travel',5100,4500,'over','Over by ₹600'),('bag','Shopping',4800,5000,'warn','Almost at limit'),('bill','Bills',3480,6000,'ok','On track'),('oth','Others',700,1500,'ok','On track')]
colr={'ok':GRN,'warn':'#B8700A','over':'#B3361A'}
cards=''
for k,n,s,b,st,txt in BUD:
    pct=round(s*100/b); left=b-s
    cap=f'₹{left:,} left' if left>0 else ('Budget fully used' if left==0 else f'₹{-left:,} over')
    cards+=card(f'''<div style="display: flex; align-items: center; justify-content: space-between"><div style="display: flex; align-items: center; gap: 10px">{cc(k,36,18)}<div style="font-size: 17px; font-weight: 600">{n}</div></div>{status(st,txt)}</div>
<div style="margin-top: 14px; display: flex; align-items: baseline; gap: 6px"><span style="font-size: 28px; line-height: 34px; font-weight: 700; font-variant-numeric: tabular-nums">{money(s)}</span><span style="font-size: 14px; color: {MUT}">of {money(b)}</span></div>
<div style="margin-top: 10px">{bar(pct,colr[st],f"{n} budget used: {pct} percent")}</div><div style="margin-top: 8px; font-size: 13px; color: {MUT}">{cap}</div>''',pad='18px 20px')
total=card(f'''<div style="display: flex; align-items: center; justify-content: space-between; gap: 40px"><div style="flex: none"><div style="font-size: 14px; line-height: 20px; color: {MUT}">Spent against all budgets</div><div style="display: flex; align-items: baseline; gap: 8px"><span style="font-size: 36px; line-height: 44px; font-weight: 700; font-variant-numeric: tabular-nums">₹37,280</span><span style="font-size: 15px; color: {MUT}">of ₹42,000</span></div></div><div style="flex: 1">{bar(89,GRN,"89 percent of the total budget used",10)}<div style="margin-top: 8px; font-size: 13px; color: {MUT}">₹4,720 left across all categories</div></div></div>''')
save('WebBudgets.dc.html',page('Web - Budgets',main('November 2026','Budgets',btn_out('Edit budgets','#'),total+f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px">{cards}</div>'),'Budgets'))

# ---------- Report
RC=[('home','Rent',15000,36),('food','Food',11400,27),('bus','Travel',5300,13),('bag','Shopping',4300,10),('bill','Bills',3300,8),('oth','Others',2560,6)]
rr=''
for k,n,a,p in RC:
    rr+=f'<div style="display: flex; align-items: center; gap: 14px">{cc(k,32,16)}<div style="width: 90px; font-size: 15px; font-weight: 600">{n}</div><div style="flex: 1">{bar(p,CAT[k][2],f"{n}: {p} percent of spending")}</div><div style="width: 150px; text-align: right; font-size: 15px; font-variant-numeric: tabular-nums"><span style="font-weight: 600">{money(a)}</span> <span style="color: {MUT}">{p}%</span></div></div>'
summ=f'''<section style="width: 320px; flex: none; box-sizing: border-box; background: {INK}; color: #FFFFFF; border-radius: 16px; padding: 24px; display: flex; flex-direction: column"><div style="font-size: 14px; line-height: 20px; color: #CFCFCF">You spent in October</div><div style="font-size: 44px; line-height: 52px; font-weight: 700; font-variant-numeric: tabular-nums">₹41,860</div><span style="margin-top: 8px; align-self: flex-start; display: inline-flex; align-items: center; gap: 4px; padding: 3px 10px 3px 8px; border-radius: 999px; background: #FFFFFF; color: {INK}; font-size: 13px; line-height: 18px; font-weight: 600">{ico('up',14,INK,'2.25')}₹2,480 more than September</span>
<div style="margin-top: auto; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.28); display: flex; gap: 16px"><div style="flex: 1"><div style="font-size: 13px; color: #CFCFCF">September</div><div style="font-size: 18px; font-weight: 700; font-variant-numeric: tabular-nums">₹39,380</div></div><div style="flex: 1"><div style="font-size: 13px; color: #CFCFCF">October</div><div style="font-size: 18px; font-weight: 700; font-variant-numeric: tabular-nums">₹41,860</div></div></div></section>'''
brk=card(f'{h2("Where your money went")}<div style="margin-top: 16px; display: flex; flex-direction: column; gap: 14px">{rr}</div>',extra='flex: 1; min-width: 0')
chg=card(f'{h2("What changed")}<p style="margin: 8px 0 0; font-size: 16px; line-height: 24px">Food went up by <strong>₹1,900</strong> compared with September. It ended <strong>₹1,400</strong> over your food budget.</p>{link("Open food budget","WebBudgets.dc.html",15)}',extra='flex: 1; min-width: 0')
tryc=f'''<section style="flex: 1; min-width: 0; background: #F0F0F0; border-radius: 16px; padding: 20px">{h2("One thing to try")}<p style="margin: 8px 0 0; font-size: 16px; line-height: 24px">Set a food limit of about ₹2,300 a week. Think of it like a small leaking tap: many small orders quietly fill the bucket by month end.</p>{link("See your food transactions","WebTransactions.dc.html",15)}</section>'''
nav=f'<a href="#" aria-label="Previous month" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid {BRD}; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ico("chev_l",20)}</a><a href="#" aria-label="Next month" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid {BRD}; background: #FFFFFF; display: flex; align-items: center; justify-content: center">{ico("chev_r",20)}</a>'
save('WebReport.dc.html',page('Web - Monthly report',main('Monthly report','October 2026',nav,f'<div style="display: flex; gap: 16px; align-items: stretch">{summ}{brk}</div><div style="display: flex; gap: 16px; align-items: stretch">{chg}{tryc}</div>'),'Reports'))
print('done')
