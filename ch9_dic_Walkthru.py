fname =  input('Enter File: ')
if len(fname) < 1: fname = 'mbox-short.txt'
hand = open(fname)

di = dict()


for lin in hand:
    lin = lin.rstrip() #remove whitespace from each line
    # print(lin) # testing code
    wds = lin.split() # split the line into words
    # print(wds) #testing code
    for w in wds:

        if w in di :
            di[w] = di[w] + 1 # count word & add to dictionary
            # print('**Existing**') #testing code
        else:
            di[w] = 1 #add a new word if not in dict begin count @ 1
            # print('**NEW**') # testing code
            print(w,di[w])

        ##Alternate way without a if else statement using .get()
            #oldcount = di.get(w,0)
            #newcount =  oldcount + 1
            #di[w] = newcount

        ##Even more concise Idiom: retrieve/create/update counter
            di[w] = di.get(w,0) + 1
print(di) # print the dictionary
