#Exercise3.py
#write a map that uses a list and a function
#Franco
import math

a_list_in_a_cool_way =[10, 100, 1000, 10000, 100000, 1000000]

a_list = list(map(lambda x: math.sqrt(x),a_list_in_a_cool_way))

for item in a_list:
    print(item)