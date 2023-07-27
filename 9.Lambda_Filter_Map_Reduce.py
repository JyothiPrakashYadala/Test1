'''# Lambda
m=lambda x,y:x+y
print(m(2,3))

s=lambda x1,x2:x1+x2
print(s('Jyothi ','Prakash'))

x=lambda i:i**2
print(x(2))

n=lambda x : list(x)
print(n('123'))

# Map

l=[1,2,3,4,5,6]
res=map(lambda x:x*x,l)
print(list(res))

def Div(n):
    return n//2
l=[2,4,6,8,10]
x=map(Div,l)
print(list(x))

#filter
l=[1,2,3,4,5,6,7,8,9,10]
n=filter(lambda x:x%2==0,l)
print(list(n))

def Prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n
i=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=filter(Prime,i)
print(list(x))

#reduce
from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]
x=reduce((lambda x,y:x if x>y else y),l)
print(x)'''

import Modules
Modules.prime(3)