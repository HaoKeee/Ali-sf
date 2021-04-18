import requests
def get_proxy():
        data = requests.get('http://x.fanqieip.com/gip?getType=1&qty=1&port=1&time=1&city=0&format=2&ss=1%2C2%2C3%2C4&dt=1&css=').json()
        print(data)
        ip = f'{data["data"][0]["ip"]}:{data["data"][0]["port"]}'
        print(ip)
        return { 'http': 'http://'+ip, 'https': 'http://'+ip }