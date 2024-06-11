# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how
# many messages the person has.

dictionary = dict()  
maximum = 0
maximum_address = ''                 
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in dictionary:
            dictionary[words[1]] = 1 
        else:
            dictionary[words[1]] += 1    
    

for address in dictionary:
    if dictionary[address] > maximum:
        maximum = dictionary[address]
        maximum_address = address

print(maximum_address, maximum)