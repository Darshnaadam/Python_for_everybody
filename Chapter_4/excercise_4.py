# Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hrs, rate):
    if hrs <= 40:
        print("Pay: ", hrs * rate)
    elif hrs > 40:
        print("Pay: ", 40 * rate + (hrs - 40) * 1.5 * rate)

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computepay(hrs, rate)
print(pay)

