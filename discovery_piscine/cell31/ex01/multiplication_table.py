user_input = input("Enter a number: ")

if not user_input.isdigit():
    print("Error")
    
else:
    for i in range(1, 13):
        ans = i * int(user_input)
        print(f"{i} x {user_input} = {ans}")
        