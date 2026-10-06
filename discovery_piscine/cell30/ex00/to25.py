user_input = input("Enter a number that is less than 25: ")


if int(user_input) > 25:
    print("Error")
else:
    for user_input in range(int(user_input), 26):
        print(user_input)
        if user_input == 25:
            break
