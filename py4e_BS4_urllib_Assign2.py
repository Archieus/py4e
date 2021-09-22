# Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Destiny.html


import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
inithtml = urllib.request.urlopen(url, context=ctx).read()
initsoup = BeautifulSoup(inithtml, 'html.parser')

count = int(input("Input times to run: ")) #Sample Default 4
pos = int(input("Input Position of Desired link: "))-1 #Sample Default3 -1 for index start at 0.

while count > 0:
    count = count - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[pos].get('href', None)
    url = tag
    name = tags[pos].contents[0]
    print(count, name)
