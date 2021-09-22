#  http://py4e-data.dr-chuck.net/comments_42.html SAMPLE data
# http://py4e-data.dr-chuck.net/comments_1342458.html Project data


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
contents = []
comments = []
numlist = []

tags = soup('span')

for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

    contents = tag.contents[0]
    comments = contents.split()

    #print(tag.contents[0])
    for c in comments:
        numlist.append(int(c))

print(sum(numlist))
