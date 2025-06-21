import numpy as np
a=np.array([[4,2,6],[6,3,9],[8,4,12]])
m=np.matrix('4,2,6;6,3,9;8,4,12')
x=np.sort(a,axis=0)
y=np.sort(m,axis=0)
print(x)
print(y)