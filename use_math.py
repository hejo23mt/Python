"""Using math library"""


import math

z = 3.14159265
print("z =", z)
print("z two decimals =", round(z, 2))
print("z four decimals =", round(z, 4))
print("square root of z =", math.sqrt(z))
print("pi in math =", math.pi)
print("e in math =", math.e)
for x in range(10):
    print(f"3^{x} = {math.pow(3, x)}")
