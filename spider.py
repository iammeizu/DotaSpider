from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re


class DotaSpider:

    def __init__(self, base_url):
        self.base_url = base_url
        self.hero_name_list = self.get_hero_name()

    def run(self):
        url = 'http://www.vpgame.com/market/dota2.html'
        # for hero_name in self.hero_name_list:
        res = self.do_request(url, hero=self.hero_name_list[0])
        print('res', res.text)
        self.parse(res.text)

    def get_hero_name(self):
        hero_name = []
        f = open('dota2_hero.htm', 'r')
        soup = BeautifulSoup(f, 'lxml')
        result = soup.find_all('a', {'class': 'heroPickerIconLink'})
        for item in result:
            hero_name.append(item.attrs['id'][5:])
        # print(hero_name, len(hero_name))
        return hero_name

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        result = soup.find_all('div', {'class': re.compile('pull-left' + '.*')})
        print('result:', result)

    def do_request(self, url, hero):
        param = {'npc': 'npc_dota_hero_' + hero}
        r = requests.get(url, params=param)
        return r

if __name__ == "__main__":
    spider = DotaSpider('http://www.vpgame.com/')
    spider.run()
