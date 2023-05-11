'''

s=input("enter the string")
n=input("enter the letter")
l=len(s)
count=0
for i in range(0,l):
    
        if s[i]==n:
            count=count+1
print(count)

'''

'''
s=input("enter the string")
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(str(count))
'''       



s=input("enter the string")
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(str(count))
keymax=max(count,key=count.get)
print(keymax)

























