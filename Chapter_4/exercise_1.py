# Exercise 1: Use random function and Run the program on your system and see what numbers you get

import random

for i in range(10):
    x = random.random()
    print(x)

print(random.randint(5, 10))

t = [1, 2, 3]
a = random.choice(t)
print(a)

