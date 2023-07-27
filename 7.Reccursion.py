'''# 1 to 10
def Seq(n):
    print(n,end=' ')
    if n<10:
        return Seq(n+1)
Seq(1)

# -1 to -10
def Seq(n):
    print(n,end=' ')
    if n>-10:
        return Seq(n-1)
Seq(-1)

# -10 to -1
def Seq(n):
    print(n,end=' ')
    if n<-1:
        return Seq(n+1)
Seq(-10)

# Sum of Digits
def Sum(n):
    if n==0:
        return 0
    return n%10+Sum(n//10)
print(Sum(123))

# Factorial
def Fact(n):
    if n==0 or n==1:
        return 1
    return n*Fact(n-1)
print(Fact(5))

# Reverse a string
def Rev(i):
    if i==-(len(s)+1):
        return ''
    return s[i]+Rev(i-1)
s='Python'
print(Rev(-1))

# Fibonnoci
def Fib(n):
    if n==1 or n==2:
       return n-1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(10))'''

