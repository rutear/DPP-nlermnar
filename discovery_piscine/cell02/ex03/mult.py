
First_num = int(input("Enter the first number: "))
Second_num = int(input("Enter the second number: "))

ans = First_num * Second_num

print(f"{First_num} x {Second_num} = {ans}")
if ans < 0:
    print("this num is negative.")
elif ans > 0:
    print("this num is positive.")
else:
    print("this num is zero.")