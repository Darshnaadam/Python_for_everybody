# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'

import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if re.search('^F..m', line):
        print(line)