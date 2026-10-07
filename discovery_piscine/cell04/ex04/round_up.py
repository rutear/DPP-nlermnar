#!/usr/bin/env python3
user_input = input("give a number: ")

num = float(user_input)
round_num = round(num)
# print(f"{num},{round_num}")
if num > round_num:
    # print("true")
    print(round_num+1)
    exit()
else:
    print(round_num)