''''
def rlcm(a,b,x,y):
    if(a==b):
        return (x*y)//a
    if(a>b):
        return rlcm(a-b,b,x,y)
    else:
        return rlcm(a,b-a,x,y)
    
a,b=map(int,input().split())
ans=rlcm(a,b,a,b)
print(ans)
'''

#
def vignan():
    global i
    i+=1
    print(i)
    vignan()
i=0
vignan()
