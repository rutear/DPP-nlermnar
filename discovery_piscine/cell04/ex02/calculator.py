
First_num = int(input("Enter the first number: "))
Second_num = int(input("Enter the second number: "))

symbol = ["+", "-", "*", "/"]

for i in symbol:
    if i == "+":
        ans = First_num + Second_num
        print(f"{First_num} + {Second_num} = {ans}")
    elif i == "-":
        ans = First_num - Second_num
        print(f"{First_num} - {Second_num} = {ans}")
    elif i == "*":
        ans = First_num * Second_num
        print(f"{First_num} * {Second_num} = {ans}")
    elif i == "/":
        if Second_num != 0:
            ans = First_num / Second_num
            print(f"{First_num} / {Second_num} = {ans}")
        else:
            print("Error: can't division by zero.")
