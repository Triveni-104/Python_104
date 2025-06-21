#recursive
def rhl(x,y):
    if(x>=y):
        print(x)
        x-=1
        rhl(x,y)#recursion calling

a,b=map(int,input().split())
rhl(a,b)