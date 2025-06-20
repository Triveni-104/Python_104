jobrole={101:'front-end developer',102:'back-end developer',103:'sql administrater'}
print(jobrole)
jobrole[101]='ui/ux developer'
jobrole[104]='data engineer'
jobrole[105]='python developer'
jobrole[106]='data analyst'
print(jobrole)
#del
jobrole.pop(101)
del jobrole[103]
print(jobrole)
#len
print(len(jobrole))
#keys
print(jobrole.keys())
#values
print(jobrole.values())
#items
print(jobrole.items())
#fromkeys
key={"101","102","103","104","105"}
value=(['back-end developer', 'data engineer', 'python developer', 'data analyst'])
d=dict.fromkeys[key,value]
print(d)