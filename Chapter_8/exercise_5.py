# Exercise 5: Minimalist Email Client.

fname = input("Enter file name: ")
count = 0
fhand = open(fname)
for line in fhand:
    word = line.split()
    if len(word) < 3 or word[0] != 'From':
        continue
    second = word[1]
    print(second)
    count += 1
print(f"There were {count} lines in the file with From as the first word")
