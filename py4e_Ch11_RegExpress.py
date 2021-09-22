import re #imports the built in package re

#re.search
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if re.search('From:', line):
        print(line)


#re.findall(pattern, string)
x = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

y = re.findall('\S+@\S+', x)

print(y)

#re.findall using ( ) to confine the search
y = re.findall('^From (\S+@\S+)', x)

#Using the re.findall to extract a portion of the string
import re
lin = 'From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#([^ ]*) after @ indicates start string search after @
#[^ ] indicates match a non-blank (not a blank character) character
# * indcates match any of the characters
y = re.findall('@([^ ]*)',lin)

#To further find tune the search to start search at lines beginning with From
y =  re.findall('^From .*@([^ ]*)', lin)

print(y)

#### SPAM COnfidence using RegEx
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-COnfidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

###Escape Character is the \
# since $ is a regular expression character, sometimee we want to search
# for a $ you would just addthe \ infront of $ i.e. \$ to keep it as a $
import re
x = 'We just received$10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
