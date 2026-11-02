import sys,asyncio
from playwright.async_api import async_playwright
P='/tmp/claude-0/-home-claude/b52fb265-d1c5-526d-8711-217681a6bd01/scratchpad/expenses-design/project/'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for name,w in [('Landing',1440),('LandingMobile',390)]:
            pg=await b.new_page(viewport={'width':w,'height':900})
            await pg.goto('file://'+P+name+'.dc.html')
            await pg.add_style_tag(content='.rv{animation:none!important;opacity:1!important;transform:none!important}')
            await pg.wait_for_timeout(3500)
            h=await pg.evaluate("document.querySelector('.lp').scrollHeight")
            print(name,'height',h)
            await pg.screenshot(path=f'img/shot-{name}.png',full_page=True)
            await pg.close()
        await b.close()
asyncio.run(main())
