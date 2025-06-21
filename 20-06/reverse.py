import numpy as np
a=np.array([[2,4,8],[3,6,9],[1,3,2]])
m=np.matrix('2,4,8;3,6,9;1,3,2')
x=(np.sort(-a,axis=1))*-1
print(x)
y=(np.sort(-a,axis=0))*-1
print(y)