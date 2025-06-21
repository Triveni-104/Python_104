import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.sum())
print(m.sum())
a.sum(axis=1)#row wise operation
m.sum(axis=1)

#max
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.max())
print(m.max())
print(a.max(axis=1))
print(m.max(axis=1))
print(m.max(axis=0))
print(m.max(axis=0))

#cumsum
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.cumsum())
print(m.cumsum())

#min
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.min())
print(m.min())
print(a.min(axis=1))
print(m.min(axis=1))
print(a.min(axis=0))
print(m.min(axis=0))

#len
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.size())
print(m.size())


#Product function
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.prod())
print(m.prod())
print(a.prod(axis=1))
print(m.prod(axis=1))
print(a.prod(axis=0))
print(m.prod(axis=0))
