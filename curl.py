import requests
import json

def main():
    url = 'http://www.vpgame.com/webservice/v2/market/search/item'
    params = {
        'app_id': 570,
    }
    res = requests.get(url, params)
    # print('res:', res.text)
    data = json.loads(res.text)
    parse(data)

def parse(data):
    body = data['body']['item']
    for item in body:
        print(item)


if __name__ == '__main__': main()