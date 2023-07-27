'''# 1.Remove Duplicates
l=[1,2,3,4,5,6,1,2,3]
l1=[]
for i in range(0,len(l)):
    if l[i] not in l1:
        l1.append(l[i])
print(l1)

# 2.Even Numbers in a list
l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in range(0,len(l)):
    if l[i]%2==0:
        l1.append(l[i])
print(l1)

# 3.Values in even index position
l=[1,2,3,4,5,6,7,8,9,20]
l1=[]
for i in range(0,len(l)):
    if i%2==0:
        l1.append(l[i])
print(l1)

# 4.Even before Odd
l=[1,2,3,4,5,6,7,8,9,10]
e=[]
o=[]
for i in range(0,len(l)):
    if l[i]%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
print(e+o)

# 5.Highest Value in a list
l=[10,0,7,8,0,5,0,7,11]
h=l[0]
for i in range(0,len(l)):
    if l[i]>l[0]:
        h=l[i]
print(h)

# 6.Bubble sort
l=[10,0,7,8,0,5,0,7,11]
for i in range(0,len(l)-1):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l) 

# 7.2nd Highest value
l=[10,0,7,8,0,5,0,7,11]
for i in range(0,2):
    for j in range(0,len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l[-2]) 

# 8.Reverse List
l=[10,0,7,8,0,5,0,7,11]
for i in range(0,len(l)//2):
    l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print(l) 

# 9.Unique Values in a list
l=[10,0,7,8,0,5,0,7,11]
for i in range(0,len(l)):
    x=l.count(l[i])
    if x==1:
        print(l[i],end=' ')

# 10.Occurance of each value
l=[10,0,7,8,0,5,0,7,11]
res=[]
for i in range(0,len(l)):
    if l[i] not in res:
        res.append(l[i])
        print(l[i],'=',l.count(l[i]))

# 11.Selection Sort
l=[10,0,7,8,0,5,0,7,11]
for i in range(0,len(l)-1):
    min_val=i
    for j in range(i+1,len(l)-1):
        if l[min_val]>l[j]:
            min_val=j
    l[i],l[min_val]=l[min_val],l[i]
print(l)

# 12.Print 0's at end of list
l=[10,0,7,8,0,5,0,7,11]
l1=[]
n=l.count(0)
for i in range(n):
    l.remove(0)
for j in range(n):
    l.append(0)
print(l)'''