def fact(n,a,b):
   if n == 0 or n == 1:
        return b
   else:
        n-=1
        return fact(n,a,b*n)


n=int(input())
result=fact(n,1,n)
print(result)