## Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1342460.xml (Sum ends with 90)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urllib.request.urlopen(url, context=ctx)
xmldata = xml.read()

tree = ET.fromstring(xmldata)
lst = tree.findall('comments/comment')

counts = []
for item in lst:
    print('Count:' , item.find('count').text)
    counts.append(int(item.find('count').text))

print(sum(counts))
