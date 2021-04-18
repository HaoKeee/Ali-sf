import requests
proxy = {
    'http': 'http://localhost:1080',
    'https': 'https://localhost:1080'
}
session = requests.Session()
# session.keep_alive = False
total = session.send(requests.Request('get','https://sf.taobao.com/').prepare())
print(f'session:{session}')
print(f'session.headers:{session.headers}')
param = {
    'spm': 'a213w.3064813.a214dqe.14.6e295dadaZgQVW',
    'city': '',
    'province': '%B8%A3%BD%A8'
}
detail = session.send(requests.Request('get','https://sf.taobao.com/item_list.htm',params=param).prepare())
print(f'session:{session}')
print(f'session.headers:{session.headers}')
print(f'session.cookies:{session.cookies}')
print(f'detail:{detail}')
print(f'detail.headers:{detail.headers}')
print(f'detail.cookies:{detail.cookies}')
print(f'detail.text:{detail.text}')