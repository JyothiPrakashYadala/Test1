'''# Positional Arguments
def Sample(a):
    return a
x=Sample(10)
print(x)

# Keyword arguments
def Sample(a):
    return a
print(Sample(a=10))

# Default Arguments
def Sample(a=0,b=2,c=3):
    print(a,end=" ")
    print(b,end=' ')
    print(c)
Sample(40,b=20)

# Variable Length Non-Keyword Arguments
def Sample(*args):
    return args
x=Sample(10,20,30,40)
print(x)

# Variable length keyword arguments
def Sample(**kwargs):
    return kwargs
x=Sample(a=10,b=20,c=30)
print(x)

# Prime or Not
def Prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
if Prime(int(input())):
    print('It is a prime number')
else:
    print('Not Prime')

# Prime numbers in given range
def Prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return n
for p in range(1,20):
    if Prime(p):
        print(p,end=' ')

# Reverse Given Number
def Rev(n):
    res=0
    while n!=0:
        rem=n%10
        n//=10
        res=res*10+rem
    return res
a=1012
x=Rev(a)
print(x)

# PalyPrime
def Palindrome(n):
    res=0
    num=n
    while n>0:
        rem=n%10
        n//=10
        res=res*10+rem
    if res==num:
        return True
def Prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return True
n=int(input('Enter a number : '))
if Palindrome(n):
    if Prime(n):
        print(f'{n} is a palyPrime...')
    else:
        print(f'{n} is not a palyPrime...')
else:
    print(f'{n} is not a palyPrime...')

# EMIRP Number
def isPalindrome(n):
    res=0
    num=n
    while n>0:
        rem=n%10
        n//=10
        res=res*10+rem
    if res!=num:
        return res
def Prime(n,res):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
                break
        else:
            if res>1:
                for j in range(2,res//2+1):
                    if res%j==0:
                        return False
                        break
                else:
                    return True
            else:
                return False
    else:
        return False
for n in range(10,100):
    x=isPalindrome(n)
    if isPalindrome(n):
        if Prime(n,x):
            print(n,x,sep=' : ')

# Factorial
def Fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
x=Fact(5)
print(x)

# Special Number
def Fact(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
def Special(n):
    res=0
    num=n
    while n>0:
        rem=n%10
        n//=10
        x=Fact(rem)
        res=res+x
    if num==res:
        return True
for n in range(1,100000):
    if Special(n):
        print(n)

# Niven Number
def Niven(n):
    num=n
    res=0
    while n>0:
        rem=n%10
        n//=10
        res=res+rem
    if num%res==0:
        return True
for n in range(1,100):
    if Niven(n):
        print(n,end=' ')
'''