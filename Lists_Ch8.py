## Chapter 8 Lists
#enter 3,5,9, done

total = 0
count = 0

while True:

inp = input('Enter a number: ')
if inp == 'done' : break
value = float(inp)

total = total + value # only keeps one number in memory
count = count + 1

average =  total/count

print("Average:", average)

### Same result, but different code using builtin functions
#Enter 3,5,9, done
numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value) # keeps numbers in memory

average = sum(numlist) / len(numlist)
print('Average:', average)

## List and stings
abc = 'With Three Words'
stuff = abc.split()
for w in stuff:
    print(w)

### Example using split to parse mail data
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
