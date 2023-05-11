'''
str="Chickoo is the winter special fruit"
len=len(str)
print(len)
count=0
for i in str:
    count=count+1
print(count)
'''

'''
s="python"
char=input("enter the char")
if char in s:
        print("s")
else:
        print("nope")
l=len(s)
print(l)
'''
'''
s=input("enter the string")
dict={}
for i in s:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
    
print(dict)

'''

'''
str=input("enter the string")
len=len(str)
print(len)
if len<=2:
    print("  ")
else:
    print(str[0:2]+str[-2:])
'''

'''
str=input("enter the string")
replace=input("enter the string")
char=str[0]
for i in str:
    if char[0]==i:
        i=replace
        print(str)
    else:
        print(str)
    
'''

'''
s='string is immuatable'
print(s.split())

'''

'''
s1='python'
s2=' is easy'
print(s1+s2)
x=s1.capitalize()
print(x)
y=s2.casefold()
print(y)

'''

'''
s='python is very difficult when it comes to automatiom'
x=s.find('comes')
print(x)
y=s.replace('difficult','easy')
print(y)

s1='python'
s2=s1[::-1]
print(s2)
l=['list','to','string']
s=" ".join(l)
print(s)

s3=s.split()
print(s3)

'''

'''
s='python is easy'
l=s.split()
l.remove('is')
print(l)
s1=" ".join(l)
print(s1)

'''

'''
s='madam'
print(s.count('madam'))

s1='python is very difficult when it comes to automatiom'
start=s1.startswith('python')
print(start)
end=s1.endswith('tp0')
print(end)

'''

'''
name='shortyy'
age=25
place='canada'
print("i'm {} and my age is{} and I'm from {}".format(name,age,place))
'''

'''
s='madam'
if s==s[::-1]:
    print('yes')
else:
    print('no')
'''

'''
#sorting the list of string
l=["yak","apple","zeal","monkey"]
sorted=[]

while l:
    min=l[0]
    for i in l:
        if i<min:
            min=i
    sorted.append(min)
    l.remove(min)

print(sorted)
'''

'''
s1='madam'
s2='sir'
if s1 is s2:
    print("yes")
else:
    print("no")

print(s1.capitalize())

s3='8788'
num=s3.isnumeric()
print(num)

'''

'''
import re
s="this is to remove all the non-alphanumeric i.e., #,%^ & &"
result=re.sub(r'\W+','',s)
print(result)

s1=s.split()
s1.reverse()
result="".join(s1)
print(result)

#can be converted into set also
s='hello world'
s1=''
for char in s:
    if char not in s1:
        s1=s1+char

print(s1)

'''

'''
import re
s='this is to extract the substring'
start="i"
end='t'
startindex=s.find(start)+1
endindex=s.rfind(end)
new=s[startindex:endindex]
print(new)

s1="".join(s.split())
print(s1)

'''

'''
s=""
b=bool(s)
print(b)

'''

'''
s1="madam is"
s2="good"
print(s1,s2,end="")

l=['apples','banana','chickoo']
sep=" "
s=sep.join(l)
print(s)
'''


'''
s="my madam is good"
l=s.split()
print(l)
for i in l:
    print(i[0])
set=set(l)
print(set)
'''

'''
s="hello world"
s1=set(s)
print(s1)

'''


'''
s="madamsm"
l=len(s)

for i in range(0,int(l/2)):
    if s[i]==s[l-i-1]:
        count=1
    else:
        count=0
if count==1:
    print("s")
else:
    print("no")

'''

'''
str="welcome to my blog"
for i in str:
    print(i)
    print(i,end=" ")
    print(i,end="#")
'''    

s="welcome to my blog"
s1=""
l=s.split()
max=0
for i in l:
    if len(i)>max:
       
        s1=i
        max=len(i)
print(s1)

























































































































































































































































































































































































