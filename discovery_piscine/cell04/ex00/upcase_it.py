#!/usr/bin/env python3
user_input = input("give me a word:").strip()

if user_input.isdigit():
    print("i said a word!,not a number")
else:
    print(user_input.upper())