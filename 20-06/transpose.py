import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.transpose())
print(m.transpose())