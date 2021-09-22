# Counting Organizations
# This application will read the mailbox data (mbox.txt) and count the
# number of email messages per organization
# (i.e. domain name of the email address) using a database with the
# following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database
# file above for grading.
# If you run the program multiple times in testing or with dfferent
# files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application:
# http://www.py4e.com/code3/emaildb.py.
# The data file for this application is the same as in previous assignments:
# http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the
# results to the database as each record is read in the loop,
# it might take as long as a few minutes to process all the data.
# The commit insists on completely writing all the data to disk every
# time it is called.

# The program can be speeded up greatly by moving the commit operation outside
# of the loop. In any database program, there is a balance between the number
#  of operations you execute between commits and the importance of not losing
# the results of operations that have not yet been committed.
import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # will create a  file if doesn't exist.
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # Drops (deletesexisting table before each run.

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    addr = email.split('@')
    org = addr[1]
    #This is similar to a dictionary.  The cur.execute is not really retrieving data, but confirming the validity and opening a set of records
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) # ? Place holder to avoid SQLinjection.  (email,) = a one tuple (one thingin it)
    row = cur.fetchone() # information we are retrieving from the database
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,)) #VALUES(?,1) sets the count at 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,)) # In databases, always use UPDATE to increment in the event there are multiple users updating the database VALUES
    conn.commit() # Will write to the disk writing records to the database.

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' # sorts retrieved data from database.

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
