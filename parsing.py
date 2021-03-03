import requests
from bs4 import BeautifulSoup as bs

site = requests.get('https://github.com/search?q=KivMob&type=issues')
sp = bs(site.text, 'lxml')
for i in sp.find_all('div', class_='f4'):
    print('https://github.com'+i.find('a').get('href'))
