#!/usr/bin/env python3
password = "fnaf"

user_input = input("Enter the password: ")

if user_input.strip() == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")