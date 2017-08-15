# import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# print('Python %s \n\non: %s. \n\nWorking path: %s' % (sys.version, sys.platform, sys.path))


try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    html = urlopen("http://www.pythonscraping.com/pages/page2.html")
    bsObj = BeautifulSoup(html.read(), 'html.parser')
    print(bsObj.head)
    print(bsObj.h1)
    print(bsObj.title)


def get_title(url):
    """

    :rtype: return title of url, incase error or not found return None
    """
    try:
        html1 = urlopen(url)
    except HTTPError as html_err:
        print('Error occur in HTT' %html_err)
        return None
    try:
        bs = BeautifulSoup(html1.read(), 'html.parser')
        title1 = bs.html
    except AttributeError as ea:
        print('Error in attributes %s' % ea)
        return None
    return title1


title = get_title('http://www.pythonscraping.com/pages/page2.html')

if title is None:
    print('Title could not be found')
else:
    print(title)
