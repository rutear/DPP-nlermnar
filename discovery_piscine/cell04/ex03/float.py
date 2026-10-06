user_input = input("give a number: ")

if user_input.isnumeric():
    num = float(user_input)
    if num.is_integer():
        print("this num is an integer.")
    else:
        print("this num is an decimal.")
else:
    print("Invalid input. Please enter a valid number.")