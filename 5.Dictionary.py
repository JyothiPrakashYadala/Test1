'''# 1.Most frequently occured char in a string
s='Yadala Jyothi Prakash'
d={}
for i in range(0,len(s)):
    if s[i] not in d:
        d[s[i]]=1
    else:
        d[s[i]]+=1
val=list(d.values())
h=val[0]
for p in range(len(val)):
    if val[p]>h:
        h=val[p]
for k,v in d.items():
    if h==v:
        print(k,'=',v)

# 2.Most frequently occured word in a string
s='we want a job where we can utilize our skills'
d={}
l=s.split()
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=1
    else:
        d[l[i]]+=1
val=list(d.values())
h=val[0]
for j in range(len(val)):
    if val[j]>h:
        h==val[j]
for k,v in d.items():
    if h==v:
        print(k,'=',v)

# 3.Lenthiest Word in a string
s='JyothiPrakash is learning python in Jspiders'
d={}
l=s.split()
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=len(l[i])
val=list(d.values())
h=val[0]
for j in range(len(val)):
    if val[j]>h:
        h=val[j]
for k,v in d.items():
    if h==v:
        print(k,'=',v)

# 4.Most repeated value in a string
l=[10,0,7,8,0,5,7,0,7,11,7]
d={}
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=1
    else:
        d[l[i]]+=1
val=list(d.values())
h=val[0]
for j in range(len(val)):
    if h<val[j]:
        h=val[j]
for k,v in d.items():
    if h==v:
        print(k)'''