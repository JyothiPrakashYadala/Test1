'''#Square
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()
    
#Rectangle
r=5
c=7
for i in range(r):
    for j in range(c):
        print('*',end=' ')
    print()
    
#Right Triangle-1
r=5
c=1
for i in range(r):
    for j in range(c):
        print('*',end=' ')
    print()
    c+=1
    
#Right Angle Traiangle-2
r=5
c=1
sp=r-1
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(c):
        print('*',end=' ')
    print()
    c+=1
    sp-=1
    
#Right Angle Triangle-3
r=5
st=5
for i in range(r):
    for j in range(st):
        print('*',end=' ')
    print()
    st-=1
    
#Right Angle Triangle-4
r=5
st=5
sp=0
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    sp+=1
    st-=1
    
#Equilateral Triangle
r=5
st=1
sp=r-1
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    st+=2
    sp-=1
    
#Reverse Equilateral Triangle
r=5
st=9
sp=0
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    st-=2
    sp+=1
    
#Diamond
r=7
st=1
sp=r-1
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    if i<r//2:
        sp-=1
        st+=2
    else:
        sp+=1
        st-=2
    
#Right Equilateral Triangle
r=7
st=1
for i in range(r):
    for j in range(st):
        print('*',end=' ')
    print()
    if i<r//2:
        st+=1
    else:
        st-=1
    
#Left Equilateral Triangle
r=7
sp=r//2
st=1
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    if i<r//2:
        sp-=1
        st+=1
    else:
        sp+=1
        st-=1
    
#Num-1
r=5
st=5
num=1
for i in range(r):
    for j in range(st):
        print(num,end='   ')
        num+=1
    print()
    
# Num-2
r=5
st=5
num=1
for i in range(r):
    for j in range(st):
        print(num,end=' ')
    print()
    num+=1
    
# Num-3
r=5
st=5
for i in range(r):
    num=1
    for j in range(st):
        print(num,end=' ')
        num+=1
    print()
    
# Num-4
r=5
st=1
for i in range(r):
    num=1
    for j in range(st):
        print(num,end=' ')
        num+=1
    print()
    st+=1
    
# Num-5
r=5
st=1
for i in range(r):
    num=5
    for j in range(st):
        print(num,end=' ')
        num-=1
    print()
    st+=1
    
# Num-6
r=5
st=1
sp=r-1
for i in range(r):
    num=st
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num-=1
    print()
    st+=1
    sp-=1
    
# Num-7
r=5
st=5
sp=0
for i in range(r):
    num=st
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num-=1
    print()
    st-=1
    sp+=1
    
# Num-8
r=5
st=5
sp=0
for i in range(r):
    num=5
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num-=1
    print()
    st-=1
    sp+=1
    
# Num-9
r=5
st=1
for i in range(r):
    num=st
    for j in range(st):
        print(num,end=' ')
    print()
    st+=1
    
# Num-10
r=5
st=1
sp=r-1
for i in range(r):
    num=st
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num-=1
    print()
    st+=2
    sp-=1

# Num-11
r=5
st=1
sp=r-1
for i in range(r):
    num=1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num+=1
    print()
    st+=2
    sp-=1
    
# Num-12
r=5
st=1
sp=r-1
for i in range(r):
    num=5
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(chr((num+64)),end=' ')
        num-=1
    print()
    st+=1
    sp-=1
    
# Num-13
r=5
st=1
sp=r-1
for i in range(r):
    num=1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(chr(num+64),end=' ')
        num+=1
    print()
    st+=2
    sp-=1
    
# Num-14
r=7
st=1
sp=r//2
for i in range(r):
    num=1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num+=1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-15
r=7
st=1
sp=r//2
for i in range(r):
    num=st
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num-=1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-16
r=7
st=1
sp=r//2
for i in range(r):
    num=1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num=num+1 if k<st//2 else num-1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-17
r=7
st=1
sp=r//2
for i in range(r):
    num=sp+1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num+=1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-18
r=7
st=1
sp=r//2
for i in range(r):
    num=st//2+1
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num=num-1 if k<st//2 else num+1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-19
r=9
st=1
sp=r//2
for i in range(r):
    num=5
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        num=num-1 if k<st//2 else num+1
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-20
r=7
st=1
sp=r//2
for i in range(r):
    if i%2==0:
        num=1
    else:
        num=2
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num,end=' ')
        if k<st//2:
            if i%2==0:
                num+=1
            else:
                num+=2
        else:
            if i%2==0:
                num-=1
            else:
                num-=2
    print()
    if i<r//2:
        st+=2
        sp-=1
    else:
        st-=2
        sp+=1
    
# Num-21
r=5
st=1
sp=r-1
num=1
for i in range(r):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print(num*num,end=' ')
        num+=1
    print()
    st+=1
    sp-=1

# String Pattern
s='python'
r=11
st=1
for i in range(r):
    for j in range(st):
        print(s[j],end=' ')
    print()
    if i<r//2:
        st+=1
    else:
        st-=1

#Square
n=int(input('Enter no.of rows : '))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

n = 5
st=n*n
for i in range(n):
    for j in range(st):
        print('*',end=' ')
    print()

n = 5
st =1
for i in range(n):
    for j in range(st):
        print('*',end=' ')
    print()
    st+=1

n = 5
st = 1
sp = n-1
for i in range(n):
    for j in range(sp):
        print(' ',end=' ')
    for k in range(st):
        print('*',end=' ')
    print()
    st+=1
    sp-=1

#Top cone
n1 = 5
st=1
sp=n1-1
for i in range(n1):
    for j in range(sp):
        print(' ',end='')
    for k in range(st):
        print('H',end='')
    print()
    st+=2
    sp-=1

# Upper Verticals

n2 = 6
st = 25
for i in range(n2):
    for j in range(st):
        if (j>=2 and j<=6) or (j>=20 and j<=25):
            print('H',end='')
        else:
            print(' ',end='')
    print()
    
# Horizontal

n3 = 3
st = 30
for i in range(n3):
    for j in range(st):
        if j>=2:
            print('H',end='')
        else:
            print(' ',end='')
    print()

#Lower verticals
n4 = 6
st = 25
for i in range(n4):
    for j in range(st):
        if (j>=2 and j<=6) or (j>=20 and j<=25):
            print('H',end='')
        else:
            print(' ',end='')
    print()

n5 = 9
st = 9
sp = 18
for i in range(n5):
    for j in range(sp):
        print(' ',end='')
    for k in range(st):
        print('H',end='')
    print()
    st-=2
    sp+=1

n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()


year = int(input('Enter a year : '))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

f=0
s=1
t=0
n=3
for i in range(n):
    if i==n-1:
        print(f,end=' ')
    t=f+s
    f,s=s,t
    
def Fib(n):
    if n==0 or n==1:
        return n
    return Fib(n-1)+Fib(n-2)
n=10
print(Fib(n-1))

l=[1,2,3,4,5,6,7,8,9]
n=4
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]+l[j]==n:
            print(l[i],'+',l[j],'=',n)
            
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
m3=[]
for i in range(0,len(m1)):
    for j in range(0,len(m1[i])):
        m3.append(m1[i][j]+m2[i][j])
print(m3)'''