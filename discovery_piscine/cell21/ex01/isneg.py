user_input = input()


if user_input == "0":
    print("This number is both positive and negative")
if int(user_input) < 0:
    print("This number is negative")
if int(user_input) > 0:
    print("This number is positive")
