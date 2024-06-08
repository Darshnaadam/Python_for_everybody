# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hrs <= 40:
    print("Pay: ", hrs * rate)
elif hrs > 40:
    print("Pay: ", 40 * rate + (hrs - 40) * 1.5 * rate)