'''# Leap Year
year=int(input('Enter a year : '))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'{year} is a leap year...')
else:
    print(f'{year} is not a leap year...')
    
# Prime Number
num=int(input('Enter a number : '))
if num>1:
    for i in range(2,num//2+1):
        if num%i==0:
            print(f'{num} is not a prime number...')
            break
    else:
        print(f'{num} is a prime number...')
    
# composite number
n=int(input('Enter a number : '))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print(f'{n} is composite number...')
            break
    else:
        print(f'{n} is not a composite number...')
else:
    print('Enter positive number...')
    
# Factors
n=int(input('Enter a number : '))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
    
# Sum of all Digits
n=int(input('Enter a number : '))
res=0
while n!=0:
    rem=n%10
    res+=rem
    n//=10
print(res)

# Product of digits
n=int(input('Enter a number : '))
res=1
while n>0:
    rem=n%10
    n//=10
    res*=rem
print(res)

# Sum of even and product of odd
n=int(input('Enter a number : '))
res1=0
res2=1
while n>0:
    rem=n%10
    n//=10
    if rem%2==0:
        res1+=rem
    else:
        res2*=rem
print('Sum of even digits is : ',res1)
print('Product of odd digits is : ',res2)

#Prime digits in a given number
n=int(input('Enter a number : '))
num=n
while n>0:
    rem=n%10
    n//=10
    if rem>1:
        for i in range(2,rem//2+1):
            if rem%i==0:
                break
        else:
            print(rem,end=" ")

# Niven Number
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    res+=rem
if num%res==0:
    print(f'{num} is a niven number...')
else:
    print(f'{num} is not a niven number...')

# Armstrong Number
n= int(input('Enter a number : '))
num=n
res=0
p=len(str(n))
while n>0:
    rem=n%10
    n//=10
    res=res+rem**p
if num==res:
    print(f'{num} is a armstrong number...')
else:
    print(f'{num} is not a armstrong number...')

# Disarium Number
n= int(input('Enter a number : '))
num=n
res=0
p=len(str(n))
while n>0:
    rem=n%10
    n//=10
    res=res+rem**p
    p-=1
if res==num:
    print('It is disarium number...')
else:
    print('Not a disarium number...')

# reverse given number
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    res=res*10+rem
print(f'Reverse of {num} is {res}')

# Palindrome Number
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    res=res*10+rem
if res==num:
    print('Palindrome')
else:
    print('Not a palindrome')
    
#Factorials
n=int(input('Enter a number : '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# Special Number
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    res=res+fact
if res==num:
    print('Special Number')
else:
    print('Not a speacial number')

# PalyPrime
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    res=res*10+rem
if res==num:
    if num>1:
        for i in range(2,num//2+1):
            if num%i==0:
                print('Not palyPrime')
                break
        else:
            print('Paly Prime')
    else:
        print('Not Paly Prime')
else:
    print('Not palyprime')

# Perfect Number
n=int(input('Enter a number : '))
num=n
res=0
for i in range(1,n):
    if n%i==0:
        res=res+i
if res==num:
    print('Perfect')
else:
    print('Not perfect')

#EMIRP Number
n=int(input('Enter a number : '))
num=n
res=0
while n>0:
    rem=n%10
    n//=10
    res=res*10+rem
if res!=num:
    if res>1:
        for i in range(2,res//2+1):
            if res%i==0:
                print('Not EMIRP')
                break
        else:
            if num>1:
                for j in range(2,num//2+1):
                    if num%j==0:
                        print('Not EMIRP')
                        break
                else:
                    print('EMIRP Number')
    else:
        print('Not EMIRP')
else:
    print('Not EMIRP')
    
#Decimal TO Binary
n=int(input('Enter a number : '))
num=n
res=0
x=1
while n>0:
    rem=n%2
    n//=2
    res=res+rem*x
    x*=10
print(res)

# Binary TO Decimal
n=int(input('Enter a value : '))
num=n
res=0
p=0
while n>0:
    rem=n%10
    n//=10
    res=res+rem*2**p
    p+=1
print(res)

# Replace 3 with 6
n=int(input('Enter a value : '))
num=n
p=1
res=0
while n>0:
    rem=n%10
    n//=10
    if rem==3:
        res=res+6*p
    else:
        res=res+rem*p
    p=p*10
print(res)

#Automorphic number
n=int(input('Enter a value : '))
m=n*n
p=len(str(n))
if n==m%(10**p):
    print('Automorphic')
else:
    print('No')

# Fibonocci Series
n=10
f=0
s=1
t=0
for i in range(n):
    t=f+s
    print(f,end=' ')
    f,s=s,t
    
n=10
f,s=0,1
if n==1 or n==2:
    print(n-1)
else:
    for i in range(n-2):
        t=f+s
        f,s=s,t
    print(t)

# Next immediate palindrome number
def isPalindrome(n):
    res=0
    num=n
    while n>0:
        rem=n%10
        n//=10
        res=res*10+rem
    if res==num:
        return True
    else:
        return False
n=11
n+=1
while (True):
    if isPalindrome(n):
        break
    n+=1
print(n)

def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            return True
def isRev(n):
    res=0
    p=len(str(n))
    while n>0:
        rem=n%10
        res=res+rem*10**p+n
'''
