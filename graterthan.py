"""Prints number from 0 to num-1 and if it's even or uneven"""

num = 10
for num in range(num):
    if num % 2 == 0:
        print(num, "= Even Number")
    else:
        print(num, "= Uneven Number")
