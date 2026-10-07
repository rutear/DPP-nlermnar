#!/usr/bin/env python3
array =  [2, 8, 9, 48, 8, 22, -12, 2]

newarray = [x+2 for x in array if x > 5]
print(array)        
unique_list = list(dict.fromkeys(newarray))
print(unique_list)
