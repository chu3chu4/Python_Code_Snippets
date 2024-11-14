try:
    4/0
except:
    print("you can't divide by Zero!")

try:
    print(name)
except:
    print("you tried to print a variable that is not defined")

try:
    sum = "hi" +2
except TypeError as e:
    print("a string can note be added with an int")

class CheeseError (Exception):# define own Exception error by inherit from Class Exception
    pass

def upper_a_word(word):
    if len(word) <= 0:
        raise CheeseError ("you entered a word with zero letters")

print(upper_a_word(""))