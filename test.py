# import chardet
# from urllib.request import quote
import requests,json
# import hashlib as hb
# code = hb.md5('641818885924'.encode('utf-8'))
# print(code.hexdigest())

# beijing = "北京"
# print(quote(beijing, encoding='gbk'))
# print(quote("北京", encoding='gbk'))
# url = 'https://sf.taobao.com/item_list.htm'
# params = {
#     'spm': 'a213w.7398504.pagination.2.294e348arrQzNN',
#     'category': '50025969',
#     'auction_source': 0,
#     'province': quote("北京", encoding='gbk'),
#     'st_param': -1,
#     'auction_start_seg': -1,
#     'page': 5
# }
# response = requests.get(url, params=params)
# print(response.url)
def organize_cookie(filename):
    with open(filename, 'r') as f:
        datas = json.loads(f.read())
    result = {}
    for data in datas:
        result[data['name']] = data['value']
    return result

from getip import get_proxy
params = {
    'spm': 'a213w.7398504.paiList.1.5e183d88286qPk',
    'rack_id': '2d764cf0-5fb2-4162-b62e-9c02df91ebf1'
}
headers = {
    'referer': 'https://sf.taobao.com',
    'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR"
}

cookies = organize_cookie('18756794700.json')
# session = requests.Session()

proxy = get_proxy()
response = requests.get('https://sf-item.taobao.com/sf_item/641818885924.htm',headers=headers,proxies=proxy,params=params,cookies=cookies)
print(response)
print(response.text)
