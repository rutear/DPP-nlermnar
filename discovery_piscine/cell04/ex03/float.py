#!/usr/bin/env python3
user_input = input("give a number: ")

num = float(user_input)
if num.is_integer():
    print("this num is an integer.")
else:
    print("this num is an decimal.")
