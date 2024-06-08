# Exercise 1: Write a program which repeatedly reads integers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# integers. If the user enters anything other than a integers, detect their mistake
# using try and except and print an error message and skip to the next integers.

total = 0
count = 0
while True:
    line = input("Enter number: ")
    if line == 'done':
        break

    try:
        num = float(line)
        print(num)
    except:
        print("Invalid input")
        continue

    count += 1
    total = total + num

print("All done!")
print("Total: ",total)
print("Count: ", count)
print("Average: ",total/count)