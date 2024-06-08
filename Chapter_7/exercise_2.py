# Exercise 2: Write a program to prompt for a file name, and then read through
# the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
# the line to extract the floating-point number on the line. Count these lines and
# then compute the total of the spam confidence values from these lines. When you
# reach the end of the file, print out the average spam confidence.

fname = input('Enter file name: ')
fn = open(fname)
count = 0
total = 0

for line in fn:
    if line.startswith("X-DSPAM-Confidence:"):
        t = line.find("0")
        number = float(line[t:])
        count = count + 1
        total = total + number

average = total/count
print("Average Spam Count: ",average)
        