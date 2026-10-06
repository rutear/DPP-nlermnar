multiple_table = (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in multiple_table:
    print(f"table of {i}",end=" : ")
    for j in multiple_table:
        ans = i * j
        print(f"{ans}", end=" ")
    print("",end="\n")
    