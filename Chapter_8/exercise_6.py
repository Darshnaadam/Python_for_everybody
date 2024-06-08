# Rewrite the program that prompts the user for a list of numbers and prints out the
# maximum and minimum of the numbers at the end when the user enters “done”.
# Write the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers after the
# loop completes.

my_list = []
while True:
    user_input = input("Enter number: ")
    if user_input == 'done':
        break
    try:
        number = float(user_input)
    except:
        print("invalid input")
        quit()

    my_list.append(user_input)

if my_list:
    print("List:", my_list)
    print("Maximum: ", max(my_list) or None)
    print("Minimum: ", min(my_list) or None)
    
    




