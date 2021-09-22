import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # will create a  file if doesn't exist.
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # Drops (deletesexisting table before each run.

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    #This is similar to a dictionary.  The cur.execute is not really retrieving data, but confirming the validity and opening a set of records
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,)) # ? Place holder to avoid SQLinjection.  (email,) = a one tuple (one thingin it)
    row = cur.fetchone() # information we are retrieving from the database
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,)) #VALUES(?,1) sets the count at 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,)) # In databases, always use UPDATE to increment in the event there are multiple users updating the database VALUES
    conn.commit() # Will write to the disk writing records to the database.

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' # sorts retrieved data from database.

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
