from random import randint

x = (randint(1, 10)); y = (randint(1, 10))
print("{} + {} = ".format(x, y))
z = int(input(""))
while x + y != z:
    z = int(input("Try again: "))
