d = {'a':10,'b':1,'c':22} #create dictionary (Constant)
t = sorted(d.items())

# sort by key NOT Value
for k,v in sorted(d.items()): #loops through dict in key order
    print(k,v)


#sort by Values instad of keys Using "reverse=True"
c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#ten most common words
fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst =  sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

##Alternative way to sort by values using list comprehension
# expressed the list as an expression
print(sorted( [(v,k) for k,v in c.items()]))
