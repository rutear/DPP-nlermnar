user_input = input("Enter your age: ")

inyear = [10,20,30]
if user_input.isdigit():
    for i in inyear:
        print(f"in {i} your age will be {int(user_input) + i}")
else:
    print("Error")