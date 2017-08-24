# This file to demonstrate basic understand about urllib work

# Used to make request
from urllib.request import urlopen
# used to parse values into the url
import urllib.parse

# x = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
# print(x.read())

url = 'https://pythonprogramming.net/?s=basics&submit=Search'
values = {'s': 'basics',
          'submit': 'Search'}


data = urllib.parse.urlencode(values)
data = data.encode('utf-8')  # data should be byte. print here will see b'q=python+programming+tutorials'  '
# create request object
req = urllib.request.Request(url, data)

# create response for request
resp = urllib.request.urlopen(req)
respData = resp.read()

print(data)
print(req)
print(respData)
