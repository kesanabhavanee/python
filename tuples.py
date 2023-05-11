'''
#input from user
t=()
i=0
n=int(input("enter the number"))
while i<n:
    num=int(input("enter the num"))
    t=t+(num,)
    i=i+1
print(t)

'''

'''
#input from user
t=()
i=0
n=int(input("enter the number"))
while i<n:
    num=input("enter the num")
    t=t+(num,)
    i=i+1
print(t)
'''

'''
#student details
t=()
t1=()
n=int(input("enter the range"))
for i in range(n):
    num=int(input("enter the num"))
    name=input("enter the name")
    sec=input("enter the sec")
    t1=(num,name,sec)
    t=t+(t1,)
print(t)
'''

'''
t=((2,'shortyy','b'),(3,'suri','a'),(4,'hameed','c'))
k=0
n=int(input("enter the num"))
for i in range(3):
    if t[i][0]==n:
        print(t[i])
        k=1
        break
if k==0:
    print("not found")
    
'''

'''
t=(1,3,2,8,7)
m1,m2=None,None
for i in t:
    if i>=m1:
        m1,m2=x,m1
    elif x>m2:
        m2=x
print(m2)

'''

'''
t1=(1,2,3,4,5)
t2=(4,5,6)
for i in t2:
    if i not in t1:
        t1=t1+(i,)
print(t1)
'''

'''
t=[[1,2,3],[4,9,8,5],[6,1]]
re=[]
for i in range(0,len(t)):
    s=0
    for j in range(0,len(t[i])):
        s=s+t[j][i]
    re.append(s)
print(re)
'''

'''def column_sum(lst):
    res=[]
    for i in range(0,len(lst)):
        s=0
        for j in range(0,len(lst[i])):
            s+=lst[j][i]
        res.append(s)
    return res
     
# Driver code
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(column_sum(lst))
'''    

'''
t=((1,2,3),(3,4),(5,6,7,1))
t1=()
for i in t:
    s=0
    for j in i:
        s=s+j
    t1=t1+(s,)
print(t1)

'''



'''
t=((1,2,3),(3,4),(5,6,7,1))
t1=()
#for i in t:
#        t1=t1+(max(i),)
#print(t1)

for i in t:
    max=i[0]
    for j in i:
        if j>max:
            max=j
    t1=t1+(max,)
print(t1)
'''

'''
t1=((1,2,3),(3,4),(5,6,7,1))

max=t[0]
for i in t:
    if i<max:
        max=i
print(max)

t2=()
for i in t1:
    t2=t2+(len(i),)
ind=t2.index(max(t2))
print(t1[ind])

'''

t=("amit","ram","esha")
for i in t:
    if i[0] in ("aeiouAEIOU"):
        print(i)

















































































