# Exercise 1: Write a function called chop that takes a list and modifies it, removing
# the first and last elements, and returns None. Then write a function called middle
# that takes a list and returns a new list that contains all but the first and last
# elements.

def chop(lst): 
    del lst[0]
    del lst[-1]

def middle(lst):
    new = lst[1:]
    del new[-1]
    return new

chop_lst1 = ['a', 'b', 'c', 'd', 'e']
rest = chop(chop_lst1)
print(chop_lst1)
print(rest)

chop_lst2 = [1,2,3,4]
middle_lst = middle(chop_lst2)
print(middle_lst)
print(chop_lst2)
