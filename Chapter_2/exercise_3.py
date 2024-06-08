# Write a program to prompt the user for hours and rate per hour to
# compute gross pay.
# Example: 
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

hrs = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hrs * rate
print("Pay: ", pay)
