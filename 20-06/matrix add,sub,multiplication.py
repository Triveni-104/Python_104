import numpy as np
a=([[1,2.3],[4,5,6]])
b=([[4,5,6],[1,2,3]])
c=np.matrix('1,2,3;4,5,6')
d=np.matrix('4,5,6;1,2,3')
ans=np.sum([a,b],axis=1)
print(ans)
ans1=np.sum([c,d],axis=1)
print(ans1)