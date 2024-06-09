# Exercise 2: Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be open")
    quit()

msg = dict()
for line in fhand:
    word = line.split()
    if len(word) < 3 or word[0] != 'From':
        continue
    else:
        if word[2] not in msg:
            msg[word[2]] = 1
        else:
            msg[word[2]] += 1

print(msg)  
    