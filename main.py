from DrissionPage import ChromiumPage, ChromiumOptions

co = ChromiumOptions()
co.set_argument('--start-maximized')
co.set_argument('--incognito')

page = ChromiumPage(co)

office = '张江'
page.get('https://orangetest.aiorange.com/login')
page.ele('xpath=//div[@class="toUser"]').click()
page.ele('xpath=//div[@class="user-name"]//input').input('chenlibin')
page.ele('xpath://div[@class="pass-word"]//input').input('Start2025')
page.ele('xpath=//button[@class="odos-btn odos-btn--primary"]').click()
page.ele(f'xpath=//div[@class="label"  and text()="{office}"]').click()
page.wait.eles_loaded('xpath=//div[@class="menu-sider"]')

text = page.ele('xpath=//div[@class="search"]//input').attr('placeholder')
print(text)

page.close()