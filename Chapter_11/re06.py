import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    x = re.findall('\S+@+\S+', line)
    if len(x) > 0:
        print(x)
