'''
#raw string
print(r'\tvignan')

print('\nvignan')
'''

#
import string
print(string.__all__)
print(string.ascii_letters)
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.octdigits)
print(string.hexdigits)
print(string.printable)
print(len(string.printable))
print(string.punctuation)
print(len(string.punctuation))
print(string.whitespace)
print(len(string.whitespace))

#
s1="a1"
s2="1a"
print(s1.isidentifier())
print(s2.isidentifier())

#is title
s1="Vignan Anil"
s2="Vignan Anil"
print(s1.istitle())
print(s2.istitle())

#
s1=("Vignan of Anil of guntur of python")
print(s1.center(49,'@'))
print(s1.rjust(49))
#
list1=['boe','batch','of','2023']
str1='@#'
print(str1.join(list1))

#zfill
s1=("Vignan of Anil of guntur of python")
print(s1.zfill(50))

#program 1
import string
s=input()
uc,lc,dc,sc=0,0,0,0
u=string.ascii_uppercase
l=string.ascii_lowercase
d=string.digits
for i in s:
    if i in u:
        uc+=1
    elif i in l:
        lc+=1
    elif i in d:
        dc+=1
    else:
        sc+=1
print(uc,lc,dc,sc)     
#3rd method
s = input()
uc, lc, dc, sc = 0, 0, 0, 0

for i in s:
    if 'A' <= i <= 'Z':
        uc += 1
    elif 'a' <= i <= 'z':
        lc += 1
    elif '0' <= i <= '9':
        dc += 1
    else:
        sc += 1
print(uc,lc,dc,sc)   


#chr & ord
s = input()
uc, lc, dc, sc = 0, 0, 0, 0

for i in s:
    if ord(i)>=65 and ord(i)<=90:
        uc += 1
    elif ord(i)>=97 and ord(i)<=122:
        lc += 1
    elif ord(i) >= 48 and ord(i) <= 57:
        dc += 1
    else:
        sc += 1
print(uc,lc,dc,sc)   
