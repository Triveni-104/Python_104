set={'python','c','c++','java','sql','javascript','angular java'}
print('python' in set)

#adding items
set.add('html')
set.add('node js')
set.add('express js')
print(set)

#update
set.update(['microbiology','biochemistry'])
print(set)

#remove
set.remove('microbiology')
print(set)

#discard
set.pop('html')
print(set)