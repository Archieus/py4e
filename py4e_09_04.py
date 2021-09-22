# 9.4 Write a program to read through the mbox-short.txt and figure
# out who has sent the greatest number of mail messages. The program
# looks for 'From ' lines and takes the second word of those lines as
# the person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find the most prolific
# committer.

#Get the dataset
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

###
counts = {}
emailst = []

# Pull Email Addresses from file into a list to be counted
for line in handle:
    line = line.strip()
    if not line.startswith('From '): continue

    words = line.split() # split the line into separate words
    print(words[1])
    emailst.append(words[1]) # pull second email address into dict

print('email adress', emailst)

## Begin Countint the number of emails sent and create a dictionary
print('Counting...')
for email in emailst:
    counts[email] = counts.get(email,0) + 1
    #print(counts)

print('Counts', counts)

### Identify the largest email sender
numsent = None
emailbox = None

for email,count in counts.items():
    if numsent is None or count > numsent:
        emailbox = email
        numsent =  count

print(emailbox, numsent)
