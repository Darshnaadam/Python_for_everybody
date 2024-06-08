# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = int(input("Enter the temperature in Celsius: "))
fahrenheit = celsius * (9/5) + 32
print("Fahrenheit: ", fahrenheit)