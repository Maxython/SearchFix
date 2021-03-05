import requests
from bs4 import BeautifulSoup as bs
from copy import copy


class search:


    def __init__(self, request:str) -> None:
        self.__request = request.replace(' ', '+')
        self.__url = None
        self.__result = {}


    def github(self) -> dict:
        self.__url = f'https://github.com/search?q={self.__request}&type=issues'
        site = requests.get(self.__url)
        sp = bs(site.text, 'lxml')
        self.__result['len'] = sp.find('div', class_='d-flex flex-column flex-md-row flex-justify-between border-bottom color-border-secondary pb-3 position-relative').find('h3').text.replace('\n', '').split()[0]


    def readthedocs(self) -> dict:
        self.__url = f'https://readthedocs.org/projects/docs/search/?q={self.__request}&project=docs'


    def habr(self) -> dict:
        self.__url = f'https://habr.com/en/search/?q={self.__request}'


    @property
    def request(self) -> str:
        return f'{self.__request}'


    @property
    def url(self) -> str:
        return copy(self.__url)


    @property
    def result(self) -> str:
        return copy(self.__result)


#site = requests.get('https://github.com/search?q=KivMob&type=issues')
#sp = bs(site.text, 'lxml')
#for i in sp.find_all('div', class_='f4'):
#    print('https://github.com'+i.find('a').get('href'))

a = search('python str')
a.github()
print(a.request)
print(a.url)
print(a.result)