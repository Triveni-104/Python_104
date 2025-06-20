#union(|)
set1={1,2,3}
set2={3,4,5}
print(set1 | set2)

#intersection(&)
print(set1 & set2)

#difference
dm=set1.difference(set2)
print("diffeence:", dm)
print()

print(set1 - set2)

#issubset()
isub=set1.issubset(set2)
print("issubset:",isub)
print()

#issuperset()
isup=set1.issuperset(set2)
print("issuperset:",isup)
print()