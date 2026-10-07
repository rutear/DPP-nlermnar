#!/usr/bin/env python3
First_num = int(input("Enter the first number: "))
Second_num = int(input("Enter the second number: "))

print(f"{First_num} + {Second_num} = {(First_num+Second_num)}")
print(f"{First_num} - {Second_num} = {(First_num-Second_num)}")
print(f"{First_num} x {Second_num} = {(First_num*Second_num)}")
if Second_num != 0:
    ans = First_num / Second_num
    print(f"{First_num} / {Second_num} = {ans}")
else:
    print("Error: can't division by zero.")
