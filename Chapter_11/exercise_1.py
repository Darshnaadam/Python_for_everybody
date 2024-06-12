# Exercise 1: Write a simple program to simulate the operation of the grep command
# on Unix. Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:

import re
count = 0
fhand = open('mbox.txt')
regex_input = input("Enter a regular Expression: ")
for line in fhand:
    if re.findall(regex_input, line):
        count += 1
print(f"mbox.txt has {count} lines that match {regex_input}")
    