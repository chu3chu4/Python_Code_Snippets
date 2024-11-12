"""
Exercise

Your task Create a function named has_remainder() that takes two ints and divides the first number by the second number. Then the fucntion should return True if there is a remainder. The function should retufn False if there is not a remainder

"""
from math import remainder


def has_remainder(int1, int2):
    remainder = int1 % int2

    if remainder != 0:
        print(f"The remainder is {remainder}")
        return True
    else:
        print("There is no remainder")
        return False


has_remainder(5,2)
has_remainder(10,2)