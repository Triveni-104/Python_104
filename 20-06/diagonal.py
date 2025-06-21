import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
print(a.trace())
print(m.trace())

#
import numpy as np
a=np.array([[1,1,1],[2,2,2],[3,3,3]])
m=np.matrix('1,1,1;2,2,2;3,3,3')
print(np.unique(a))
print(np.unique(m))

#det
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
m=np.matrix('1,2,3;4,5,6;7,8,9')
ans=a.mean()
ans1=m.mean()
print(ans)
print(ans1)