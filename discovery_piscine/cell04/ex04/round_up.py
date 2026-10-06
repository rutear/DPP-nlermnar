user_input = input("give a number: ")

num = float(user_input)
round_num = round(num)
print(f"{num},{round_num}")
if num > round_num:
    round_num+1
    print(round_num)
else:
    print(round_num)