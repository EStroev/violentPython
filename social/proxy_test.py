import mechanize


def test_proxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

url = 'http://2ip.ru'
hide_me_proxy = {'http': '173.10.21.69:3128'}

test_proxy(url, hide_me_proxy)