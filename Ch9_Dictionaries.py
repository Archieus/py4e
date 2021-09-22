ccc = {}
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


### To create a new key with a name if not already there
# otherwise adds 1 to an existing names
counts = {}
names = ['csev', 'cwen', 'csev', 'zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

## Builtin Python
if name in counts:
    x = counts[name]
else:
    x = 0

##Get method in dictionaries Simplifying counting with get()

x = counts.get(name,0)

counts =  dict()
names = ['csev', 'cwen', 'csev','zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0)+1
print(counts)


###
counts = {}
print('Enter a line of text:')
line = input('')
words = line.split()

print('Words', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) +1
    #print(counts)
print('Counts', counts)

####
name = input('enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount =  count

print(bigword, bigcount)
