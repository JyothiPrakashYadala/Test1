'''# Reverse String without using any inbuilt methods

s='prakash'
reversedname=""
x=len(s)-1
while(x!=-1):
    reversedname+=s[x]
    x-=1
print(reversedname)

# Reverse string with slicing
s='prakash'
n=s[::-1]
print(n)

# Reverse string without slicing
s='prakash'
res=''
for i in range(-1,-(len(s)+1),-1):
    res+=s[i]
print(res)

# String Palindrome
s=input('Enter a string : ')
res=''
for i in range(-1,-(len(s)+1),-1):
    res+=s[i]
if res==s:
    print(f'{s} Given string is a palindrome {res}')
else:
    print(f'{s} string is not a palindrome {res}')
    
# Sub-Palindromes in a string
s='ABCBA'
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        n=s[i:j]
        if n==n[::-1]:
            print(n)

# Upper To Lower
s='Yadala Jyothi Prakash'
x=s.upper()
print(x)

# Lower To Upper
s='Yadala Jyothi Prakash'
x=s.lower()
print(x)

# Replace character
s='Yadala Prakash'
x=s.replace('a','@')
print(x)

# Repalce character
s='Yadala Prakash'
res=''
for i in s:
    if i=='a':
        res+='@'
    else:
        res+=i
print(res)

# count of each char
s="Yadala Prakash"
res=''
for i in range(0,len(s)):
    if s[i] not in res:
        res+=s[i]
        print(s.count(s[i]),s[i])

# count of vowels
v='AEIOUaeiou'
s='Jyothi Prakash Yadala'
res=''
for i in range(0,len(s)):
    if s[i] in v:
        if s[i] not in res:
            res+=s[i]
            print(s[i],'=',s.count(s[i]))

# count of vowels
s='Jyothi Prakash Yadala'
v='AEIOUaeiou'
c=0
for i in range(0,len(s)):
    if s[i] in v:
        c+=1
print(c)

#List to string without join()
l=['P','r','a','k','a','s','h']
res=''
for i in range(0,len(l)):
    res+=l[i]
print(res)

#List to string using join()
l=['a','b','c','d']
res=''.join(l)
print(res)

# Vowels in a string
s='Jyothi Prakash'
v='AEIOUaeiou'
res=''
for i in range(0,len(s)):
    if s[i] in v:
        res+=s[i]
print(res)

# Remove Duplicates
s='Jyothi Prakash'
res=''
for i in range(0,len(s)):
    if s[i] not in res:
        res+=s[i]
print(res)

#count of characters
s='aaabbccccbaaf'
res=''
c=1
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=str(c)+str(s[i])
        c=1
res+=str(c)+str(s[i+1])
print(res)

#Index Positions of given character
s='Prakash'
l=[]
r='a'
for i in range(0,len(s)):
    if s[i]==r:
        l.append(i)
print(l)

# Reverse string without reversing words in a string
s='Jyothi Prakash is learning python in Jspiders'
l=s.split()
for i in range(0,len(l)//2):
    l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
x=' '.join(l)
print(x)

# Reverse each word in a string
s='Jyothi Prakash is learning python in Jspiders'
l=s.split()
res=''
for i in range(len(l)):
    l[i]=l[i][::-1]
res=' '.join(l)
print(res)'''