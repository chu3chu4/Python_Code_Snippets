# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:10:47 2024

@author: yanwu
"""


def hello():
    print("Hello Nick!")


hello()


def hello(name):
    print(f"Hello {name}!")


hello("John")


def add_number(num1, num2):
    print(f"the result is {num1 + num2}")
    # the line above shows how to do a formatted string


add_number(10, 12)


def dog_info(name, age):
    print(f"{name} is my dog and he is {age} years old!")


dog_info("puppy", 7)


# return a value

def double(number):
    return number * 2

print(double(20))


def words_in_caps(word):
    return word.upper()

print(words_in_caps("yanbo wu"))
