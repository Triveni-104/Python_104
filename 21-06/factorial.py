def fact(n):
   if n == 0 or n == 1:
        return 1
   else:
        return n * fact(n - 1)


n=int(input())
f=fact(n)
print(f)

#non recursive
n=int(input())
f=1
while n>=1:
    f*=n
    n-=1
print(f)

#1 to multiplication
def fact(n,a,b):
   if n == 0 or n == 1:
        return b
   else:
        n-=1
        return fact(n,a,b*n)


n=int(input())
result=fact(n,1,n)
print(result)

