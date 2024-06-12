# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.

import re 
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if re.findall('^X\S*: [0-9.]+', line):
        print(line)