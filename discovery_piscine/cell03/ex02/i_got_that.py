user_input = input("what you gonna say? ").strip()

if user_input.isdigit():
    print("You said a number!")
else:
    while True:
        user_input = input(f"got it, anythings else? ").strip()
        if user_input.upper() == "STOP":
            break