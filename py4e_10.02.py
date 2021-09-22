# 10.2 Write a program to read through the mbox-short.txt and figure
# out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.


#Get the dataset
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

###
counts = {} # Dictionary
hms = [] # List
hour = [] # List

# Pull Email Addresses from file into a list to be counted
for line in handle:
    line = line.strip() # Strip whitespace
    if not line.startswith('From '): continue

    time = line.split() # split line and extract time element
    #print(time[5])
    hms.append(time[5]) # pull hh:mm:ss into a list

#pull hours from time element
for ms in hms:
    ms = ms.split(':')
    hour.append(ms[0])

#Begins the counting process
for h in hour:
    counts[h] = counts.get(h,0) + 1 #new dict called counts
    #print(counts)

#Convert Dict Counts to a list to sort
lst = list()

for key,val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst) # Sort by Key 

for key, val in lst :
    print(key, val)
