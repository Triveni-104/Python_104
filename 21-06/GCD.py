import math
print(math.gcd(5,12))
print(math.lcm(5,12))

#non recursion
a = 5
b = 12

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)  # or print(b), both are same here
print(b)

