
'''
list=[10,-1,-9,29]
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
    if i<max:
        min=i

print(max)
print(min)
'''

'''
List=['abc', 'xyz', 'aba', '1221']
count=0
for i in List:
    if len(i)>=2 and i[0]==i[-1]:
        count=count+1
print(count)

'''

'''
#cloning or copying
l=[1,5,3,9]
new=list(l)
print(l)
print(new)
'''


'''
#print the longest item

l=["shortyy","hello","rabbit","peacock"]
n=int(input("enter the size"))
for i in l:
    if len(i)>n:
        print(i)


'''

'''
def same():    
    l1=[2,6,4,0]
    l2=[4,8,6,1,7]
    for i in l1:
        if i in l2:
            return True
print(same())

'''

'''
List =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
del List[5]
del List[4]
del List[0]
print(List)

'''
'''
l=[2,7,5,9,6]
for i in l:
    if i%2==0:
        l.remove(i)
print(l)
'''

'''
from random import shuffle
color=["orange","red","yellow","blue"]
#shuffle(color)
#print(color)
s=set(color)
print(s)
k=list(s)
print(k)
'''

'''
import itertools
print(list(itertools.permutations([1,2,3])))


l1=[9,54,7,2,3]
l2=[0,5,87,7]
l1_l2=list(set(l1)-set(l2))
l2_l1=list(set(l2)-set(l1))
total=l1_l2+l2_l1
print(total)

for index,value in enumerate(l1):
    print(index,value)


'''


'''

l=["J","A","V","A"]
print(*l)
s="".join(l)
print(s)

l1=[9,54,7,2,3]
l2=[0,5,87,7]
l1.append(l2)
print(l1)
l1=l1+l2
print(l1)

'''

'''
l=[8,9,8,7,2,2,2,4]
count=1
c=[]
len=len(l)
for i in range(0,len):
    for j in range(i+1,len):
        if l[i]==l[j]:
            print(l[j])
            count=count+1
            #c.append(count)
print(c)


'''

'''
MyList = [8,6,8,10,8,20,10,8,8]

res = {i:MyList.count(i) for i in MyList}

print(res)
keymax=min(res,key=res.get)
print(keymax)
'''

'''
list1 = [5, 10, 15, 20, 25, 50, 20]
old=20
new=200
#list1=[new if x == old else x for x in list1]

print(list1)

'''

'''
list1=[10,20,[300,400,[5000,6000],500],30,40]
after=6000
new=7000
for element1 in list1:
    if isinstance(element1, list):
        for element2 in element1:
            if isinstance(element2, list):
                for element3 in element2:
                    print(element3)
                    if element3==after:
                        element2.append(new)
            else:
                print(element2)
    else:
        print(element1)

'''

'''
l=[1,2,3,4,5]
k=[i*i for i in l if i%2==0]
print(k)
'''

'''
l=[2,-5,32,-7,0,4]
positive=[i for i in l if i>=0]
print(positive)

'''

'''
l=[3,4,8,2,3,8,7]
u=[]
d=[]
for i in l:
    if i not in u:
        u.append(i)
    else:
        d.append(i)
print(u,d)

'''

'''
l=["One","oops","python"]
rev=[i[::-1] for i in l]
print(rev)

'''

'''
l=[9,43,2,1,3]
fm=max(l[0],l[1])
sm=min(l[0],l[1])
for i in range(2,len(l)):
    if l[i]>fm:
        sm=fm
        fm=l[i]
    else:
        if l[i]>sm:
            sm=l[i]
print(sm)

'''

'''
b=['b','u','n','n','y']
for i in b:
    print(i,end="")

'''


l=[]
i=0
n=int(input("enter the range"))
while i<n:
    num=int(input("enter the num"))
    if num%2!=0:
        l=l+[num]
    i=i+1
print(l)


































































































































































































