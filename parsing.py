import requests
from bs4 import BeautifulSoup as bs
from copy import copy
from typing import Union


class search:


    def __init__(self, request:str) -> None:
        self.__request = request.replace(' ', '+')
        self.__url = None
        self.__official_url = None
        self.__result = []


    def github(self, quantity:int=1, number_of_comments:Union[None, int]=None) -> None:
        self.__result.clear()
        self.__url = f'https://github.com/search?q={self.__request}&type=issues'
        self.__official_url = 'https://github.com'
        for h in range(quantity):
            for_url = f'https://github.com/search?p={h+1}&q={self.__request}&type=Issues'
            site = requests.get(for_url)
            if site.status_code == 200:
                sp = bs(site.text, 'lxml')
                for i in sp.find_all('div', class_='ml-1 flex-auto'):
                    c = i.find('span', class_='mr-3')
                    if (number_of_comments == None or number_of_comments == 0) or ((int(c.text.replace('\n', '').split()[0]) >= number_of_comments) if c != None else False):
                        b = {'comments':int(c.text.replace('\n', '').split()[0]) if c != None else c}
                        for j in i.find_all('a'):
                            a = j.get('href')
                            if a.count('/') == 1:
                                b['user'] = {}
                                b['user']['url'] = self.__official_url + a
                                b['user']['url_title'] = j.text
                            elif 'issues/' in a or 'pull' in a:
                                b['issues'] = {}
                                b['issues']['url'] = self.__official_url + a
                                b['issues']['url_title'] = j.text
                        self.__result.append(b)


    def readthedocs(self, quantity:Union[str, int]='all') -> None:
        self.__result.clear()
        self.__url = f'https://readthedocs.org/projects/docs/search/?q={self.__request}&project=docs'
        site = requests.get(self.__url)
        sp = bs(site.text, 'lxml')
        for i in sp.find_all('li', class_='module-item search-result-item'):
            if quantity == 'all' or len(self.__result) != quantity:
                b = {}
                for j in i.find_all('a'):
                    b['main' if 'main' not in b else f'docs{len(b)}'] = {'title': ' '.join(j.text.replace('\n', '').split()), 'url': j.get('href')}
                self.__result.append(b)
            else:
                break


    def habr(self) -> dict:
        self.__result.clear()
        self.__url = f'https://habr.com/en/search/?q={self.__request}'


    @property
    def request(self) -> str:
        return f'{self.__request}'


    @property
    def url(self) -> str:
        return copy(self.__url)


    @property
    def official_url(self) -> str:
        return copy(self.__official_url)


    @property
    def result(self) -> str:
        return copy(self.__result)


#site = requests.get('https://github.com/search?q=KivMob&type=issues')
#sp = bs(site.text, 'lxml')
#for i in sp.find_all('div', class_='f4'):
#    print('https://github.com'+i.find('a').get('href'))

a = search('python str')
a.readthedocs(10)
print(len(a.result))
