fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        print(line)