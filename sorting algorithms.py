'''
#bubble
l=[2,23,10,1]
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
for i in range(n):
    print(l[i])
'''

'''
#selection
l=[2,23,10,1,84,3]
n=len(l)
for s in range(n):
    min=s
    for i in range(s+1,n):
        if l[i]<l[min]:
            min=i
    l[s],l[min]=l[min],l[s]
for i in range(n):
    print(l[i])
'''

'''
#insertion
l=[7,2,1,6]
n=len(l)
for i in range(1,n):
    a=l[i]
    j=i-1
    while j>=0 and a<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=a

for i in range(0,n):
    print(l[i])





























