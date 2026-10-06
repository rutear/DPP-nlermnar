user_input = input("what you gonna say? ").strip()


while True:
        user_input = input(f"got it, anythings else? ").strip()
        if user_input.upper() == "STOP":
            break