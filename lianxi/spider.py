import re
import urllib.request
from bs4 import BeautifulSoup
# resp = requests.get('https://www.so.com/')
# print(resp)
# print(resp.content)
# soup = BeautifulSoup(resp.content)
# print(soup)
url = 'http://www.baidu.com'
op = urllib.request.urlopen(url)
soup=BeautifulSoup(op,'lxml')
a = soup.findAll(name='a',attrs={"href":re.compile(r'^http:')})
for i in a:
    print(i)