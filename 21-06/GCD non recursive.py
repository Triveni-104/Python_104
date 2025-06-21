a,b=map(int,input().split())
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)  # or print(b), both are same here
print(b)