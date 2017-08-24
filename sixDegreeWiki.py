import datetime
import random
from asyncio import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# html = urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find')
bsObj = BeautifulSoup(html.read(), 'html.parser')

# for link in bsObj.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# find div bodyContent
# bodyContent = bsObj.find('div', attrs={'id': 'bodyContent'})
# print(bodyContent)

print('------------------------')

# from body content extract
# for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# make function to get links of wiki article
def get_links(article_url):
    html_resource = urlopen('https://en.wikipedia.org/' + article_url)
    bs = BeautifulSoup(html_resource.read(), 'html.parser')
    return bs.find('div', attrs={'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# use the function above
random.seed(datetime.datetime.now())
links = get_links('/wiki/Kevin_Bacon')

while len(links) > 0 :
    new_article = links[random.randint(0, len(links) - 1)].attrs['href']
    print(new_article)
    sleep(2)
    links = get_links(new_article)