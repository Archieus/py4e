import urllib.error, urllib.request, urllib.parse
from bs4 import BeautifulSoup

a = int(input("Position: "))-1
b = int(input("Times: "))
url = input("Enter URL: ")

for c in range(b):
    x = urllib.request.urlopen(url).read() #html
    y = BeautifulSoup(x,'html.parser') #Soup
    z = y('a') #tags
    d = z[a].get('href',None) #tag
    url = d # URL
    e = z[a].contents[0] # name

print(e)
