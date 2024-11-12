# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:59:18 2024

@author: yanwu
"""

'''
user_text = input ("type your text here: ")

print (user_text.upper())


user_number = input("Type the number you want to double: ")

print (int(user_number) * 2) #note, the input function will always take the input as a String. I need to change it to Int


# ask user for a string, then ask if the string should be printed in upper case or lower case, then print the string according to user's choice

'''

word = input("type a string please: ")

lower_or_upper_case = input("enter 1 if you want lower case, 2 for upper case: ")

choice = int(lower_or_upper_case)

if choice == 1:
    print(word.lower())

    # if choice == 2:
if choice == 2:
    print(word.upper())

else:
    print("you entered a number which is neither 1 nor 2")



#hi from github
