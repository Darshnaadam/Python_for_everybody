# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

largest = None
smallest = None
total = 0
count = 0

while True:
    line = input("Enter numbers: ")
    if line == 'done':
        break

    try:
        num = float(line)
        print(line)

        count += 1
        total = total + num

        if largest == None or num > largest:
            largest = num

        if smallest == None or num < smallest:
            smallest = num
    except:
        print("Invalid input")
        continue

print("All done!")
print("Total: ",total)
print("Count: ", count)
print("Maximum number: ",largest)
print("Minimum number: ",smallest)
