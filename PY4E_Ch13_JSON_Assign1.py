# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar
# to http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
# read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers#
# in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we
# give you the sum for your testing and the other is the actual data you need
# to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1342461.json (Sum ends with 26)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.json'

handle = urllib.request.urlopen(url, context=ctx) #Opens a handle but doesn't pull data down
data = handle.read().decode() # need to decode and pulls the data down .read()

info = json.loads(data)

# Find the Keys and Values
#for key in info:
#    value = info[key]
#    print("The key and value are ({}) = ({})".format(key, value))

# print(info['comments'][1]['count'])

numlist = []

for item in range(len(info['comments'])):
    numlist.append(int((info['comments'][item]['count'])))


print(sum(numlist))
