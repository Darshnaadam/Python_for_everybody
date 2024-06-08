# Exercise 2: Rewrite your pay program using try and except so that your program
# handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hrs <= 40:
        print("Pay: ", hrs * rate)
    elif hrs > 40:
        print("Pay: ", 40 * rate + (hrs - 40) * 1.5 * rate)

except:
    print("Error, please enter numberic input")
