import re

handle = open('regex_sum_1342456.txt')

numlist = []
inum = []
for line in handle:
    line = line.strip() # for each line in handle strip whitespace
    #print(line)
    numlist = re.findall('[0-9]+',line)
    #print(len(numlist), numlist)
    if len(numlist) == 0 : continue # skips over any item with a length = 0
    for num in numlist: # iterate through the list to save each value to list
        inum.append(int(num))
print(sum(inum))
