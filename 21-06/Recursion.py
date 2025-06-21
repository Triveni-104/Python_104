#non recursive
for i in range(5, 11):
    print(i)

#recursive
def r1h(x,y):
    if(x<=y):
        print(5)
        x+=1
        r1h(x,y)#recursion calling
        
a,b=map(int,input().split())
while a<=b:
    print(a)
    a+=1
    