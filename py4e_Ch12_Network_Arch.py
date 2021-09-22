#Socket1.py script
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #doesn't make connection
mysock.connect( (data.pr4e.org, 80)) #Used to make the connection

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#encode() is required to convert to UTF-8
mysock.send(cmd)

while True:
    data = mysock.recv(512) # receive 512 characters
    if (len(data) < 1):
        break
    print(data.decode()) #converts back to unicode.
mysock.close() # Closes the connection


###urllib
import urllib.request, urllib.parse, urllib.error

###same code is required to open any webpage urllib.py
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip()) #this will decode a 'byte array' and convertto a string

## Think of this as "data" or "internet file" on the internet, not a webpage
counts = dict()
for line in fhand:
    words = line.decode().split() #converts byte string to unicode string & split
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)

### reading a html files
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand: :
    print(line.decode().strip()) #decodes bytes & converts to string

##Techniquest to parse html
### Beautifule soup from www.crummy.com deals with html efficiently
# test using http://www.dr-chuck.com/page1.htm
# script will return: http://www.dr-chuck.com/page2.htm

import urllib,request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read() #.read() reads the whole blob as one big string
soup = BeautifulSoup(html, 'html.parser') # returns a "soup" object
#we can ask questions of the "soup" object.

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) # almost like a dictionary
