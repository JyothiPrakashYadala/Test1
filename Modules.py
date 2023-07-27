'''
# import
import math
x=4
y=math.sqrt(x)
print(y)
z=math.factorial(5)
print(z)

# Aliasing
import math as m
x=m.factorial(5)
print(x)

from math import factorial as f
x=f(5)
print(x)'''

def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            print(n,' is Prime')
if __name__=='__main__':
    prime(int(input('Enter a value : ')))
            