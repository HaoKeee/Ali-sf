#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json
from lxml import etree
with open('response.html', 'r') as html:
    response = html.read()

selector = etree.HTML(response)
content = selector.xpath('//script[@id="sf-item-list-data"]/text()')[0].strip()
data = json.loads(content)
print(type(data))
item = data['data']
for i in item:print(i)
# for key,value in item.items():
#     print(key)
#     print(value)
#     print("-------------------------------------------------------------------------------------------------------")