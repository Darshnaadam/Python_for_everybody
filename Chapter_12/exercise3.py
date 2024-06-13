# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
char = 0
char_limit = 3000

for line in fhand:
    next_count = char + len(line)
    if next_count <= char_limit:
        print(line.rstrip().decode())
    elif char < char_limit:
        char_remain = char_limit - char - 1
        print(line[:char_remain])
    char = next_count
print(char)
