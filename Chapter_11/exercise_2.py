# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

import math
import re
rev = []
avg = 0
fname = input("Enter file: ")
try:
    fhand = open(fname)
except:
    print("Cannot open file: ",fname)
    exit()

for line in fhand:
    line = line.strip()
    revision = re.findall('^New Revision: ([0-9.]+)', line)
    for val in revision:
        val = float(val)
        rev = rev + [val]

rev_sum = sum(rev)
count = float(len(rev))

if count:
    avg = rev_sum/count
print(math.trunc(avg))
