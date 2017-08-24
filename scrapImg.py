# this demonstrate scrap product image from http://www.pythonscraping.com/pages/page3.html avoid logo image
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read(), 'html.parser')
images = bsObj.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image['src'])

tag2attrs = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
print(tag2attrs)


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
#
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bsObj = BeautifulSoup(html)
# images = bsObj.findAll('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])
