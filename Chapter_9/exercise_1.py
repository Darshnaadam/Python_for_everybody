# Exercise 1: Download a copy of the file
# www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn’t matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.

count = 0
dictionary = dict()
fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        count += 1
        if word in dictionary:
            continue
        dictionary[word] = count

print(dictionary)
if 'python' in dictionary:
    print('True')
else:
    print('False')
