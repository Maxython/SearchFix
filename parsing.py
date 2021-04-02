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
            g = bs(requests.get(f'https://github.com/search?p={h+1}&q={self.__request}&type=Issues').text, 'lxml').find_all('div', class_='ml-1 flex-auto')
            if len(g) == 0:
                break
            for i in g:
                c = i.find('span', class_='mr-3')
                if (number_of_comments == None or number_of_comments == 0) or ((int(c.text.replace('\n', '').split()[0]) >= number_of_comments) if c != None else False):
                    b = {'comments':int(c.text.replace('\n', '').split()[0]) if c != None else 0, 'user':{}, 'issue':{}}
                    for j in i.find_all('a'):
                        a = j.get('href')
                        if a.count('/') == 1:
                            b['user']['url'] = self.__official_url + a
                            b['user']['title'] = j.text
                        elif 'issues/' in a or 'pull' in a:
                            b['issue']['url'] = self.__official_url + a
                            b['issue']['title'] = j.text
                    self.__result.append(b)



    def readthedocs(self, quantity:Union[None, int]=None) -> None:
        self.__result.clear()
        self.__url = f'https://readthedocs.org/projects/docs/search/?q={self.__request}&project=docs'
        self.__official_url = 'https://readthedocs.org/'
        for i in bs(requests.get(self.__url).text, 'lxml').find_all('li', class_='module-item search-result-item'):
            if quantity == None or len(self.__result) != quantity:
                b = {'docs': []}
                for j in i.find_all('a'):
                    c = {'title': ' '.join(j.text.replace('\n', '').split()), 'url': j.get('href')}
                    if 'main' in b:
                        b['docs'].append(c)
                    else:         
                        b['main'] = c
                self.__result.append(b)
            else:
                break


    def habr(self, quantity:int=1, total:Union[None, int]=None) -> None:
        self.__result.clear()
        self.__url = f'https://habr.com/en/search/?q={self.__request}'
        self.__official_url = 'https://habr.com/en/'
        for i in range(quantity):
            g = bs(requests.get(f'https://habr.com/en/search/page{i+1}/?target_type=posts&order_by=relevance&q={self.__request}&flow=').text, 'lxml').find_all('article', class_='post post_preview')
            if len(g) == 0:
                break
            for j in g:
                a = j.find('span', class_='post-stats__result-counter').text
                if total == None or int(a.replace('+', '').replace('–', '-')) >= total:
                    b = {'total':a, 'post':{}, 'user':{}}
                    a = j.find('a', class_='post__title_link')
                    b['post']['url'] = a.get('href')
                    b['post']['title'] = a.text
                    a = j.find('a', class_='post__user-info user-info')
                    b['user']['url'] = a.get('href')
                    b['user']['title'] = a.text.replace('\n', '')
                    self.__result.append(b)


    def habrqna(self, quantity:int=1, answer:bool=False, quantity_answer:Union[None, int]=None) -> None:
        self.__result.clear()
        self.__url = f'https://qna.habr.com/search?q={self.__request}'
        self.__official_url = 'https://qna.habr.com/'
        for i in range(quantity):
            site = requests.get(f'https://qna.habr.com/search/questions?q={self.__request}&page={i+1}')
            if site.status_code == 200:
                for j in bs(site.text, 'lxml').find_all('li', class_='content-list__item'):
                    a = j.find('div', class_='mini-counter__count').text.replace('\n', '').replace(' ', '')
                    if (not answer or j.find('svg', class_='icon_svg icon_check') != None) and (quantity_answer == None or quantity_answer <= int(a)):
                        b = {'answer': a}
                        a = j.find('a', class_='question__title-link question__title-link_list')
                        b['title'] = ' '.join(a.text.replace('\n', '').split())
                        b['url'] = a.get('href')
                        self.__result.append(b)
                continue
            break


    def all(self, github:bool=True, number_of_comments:Union[None, int]=None, rtd:bool=True, quantity:Union[None, int]=None, habr:bool=True, total:Union[None, int]=None, hqna:bool=True, answer:bool=False, quantity_answer:Union[None, int]=None) -> None:
        a = [{'act':github, 'title':'GitHub'}, {'act':rtd, 'title':'Read the Docs'}, {'act':habr, 'title':'Habr'}, {'act':hqna, 'title':'Habr qna'}]
        if github:
            self.github(number_of_comments=number_of_comments)
            a[0]['url'] = self.url
            a[0]['official_url'] = self.official_url
            a[0]['result'] = self.result
        if rtd:
            self.readthedocs(quantity=quantity)
            a[1]['url'] = self.url
            a[1]['official_url'] = self.official_url
            a[1]['result'] = self.result
        if habr:
            self.habr(total=total)
            a[2]['url'] = self.url
            a[2]['official_url'] = self.official_url
            a[2]['result'] = self.result
        if hqna:
            self.habrqna(answer=answer, quantity_answer=quantity_answer)
            a[3]['url'] = self.url
            a[3]['official_url'] = self.official_url
            a[3]['result'] = self.result
        self.__result = a


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
