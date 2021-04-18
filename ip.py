import requests
from lxml import etree
ip_data = requests.get('http://x.fanqieip.com/gip?getType=1&qty=1&port=1&time=1&city=0&format=2&ss=1%2C2%2C3%2C4&dt=1&css=').json()
ip = f'{ip_data["data"][0]["ip"]}:{ip_data["data"][0]["port"]}'
ip = '36.99.41.106:1090'
proxies = {
    'http': 'http://' + ip,
    'https': 'https://' + ip
}
session = requests.Session()
print(proxies)
response = session.get('http://ip.chacha.cn/',proxies=proxies,timeout=5)
print(response)
print(response.text)
selector = etree.HTML(response.text)
ip = selector.xpath('//center/span[1]/text()')[0]
address = selector.xpath('//center/span[2]/text()')[0]
print(f'ip:{ip}, address:{address}')