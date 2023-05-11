'''
n=int(input("enter the num"))
for i in range(0,n):
    for num in range(i+1):
        print(" * ",end="")
    print("\r")
    
'''

'''
n=int(input("enter the num"))
l=[]
for i in range(1,n+1):
    l.append("*"*i)
print("\n".join(l))
'''

'''
n=int(input("enter the num"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)
'''

'''
n=int(input("enter the num"))
space=2*n-2
for i in range(0,n):
    for j in range(0,space):
        print(end=" ")
    space=space-1
    for k in range(0,i+1):
        print(i,end=" ")
    print('\r')
'''

'''
#number pyramid
n =int(input("enter the number"))
space=2*n-2
for i in range(0,n+1):
    for j in range(1,space):
        print(end=" ")
    space=space-1
    for k in range(0,i):
        print(i,end=' ')
    print('\r')

'''

'''
#inverted pyramid
n=int(input("enter the number"))
space=n-2
for i in range(n+1,0,-1):
    for j in range(space,1,-1):
        print(end=" ")
    space=space+1
    for j in range(0,i-1):
        print("*",end=' ')
    print(" ")

'''

'''
#diamond
n =int(input("enter the number"))
space=2*n-2
for i in range(0,n+1):
    for j in range(1,space):
        print(end=" ")
    space=space-1
    for k in range(0,i):
        print('*',end=' ')
    print('\r')
space=n-2
for i in range(n,0,-1):
    for j in range(space,-1,-1):
        print(end=" ")
    space=space+1
    for j in range(0,i-1):
        print("*",end=' ')
    print(" ")

'''


n =int(input("enter the number"))

space=n-2
for i in range(n,-1,-1):
    for j in range(space,0,-1):
        print(end=" ")
    space=space+1
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")
space=2*n-2    
for i in range(0,n+1):
    for j in range(0,space):
        print(end=" ")
    space=space-1
    for k in range(0,i+1):
        print('*',end=' ')
    print('\r')


'''
n=int(input("enter the num"))
for i in range(0,n):
    for num in range(i+1):
        print("*",end="")
    print("\r")
for i in range(n+1,0,-1):
    for j in range(1,i-1):
        
        print("*",end="")
    print("\r")


'''
'''
n=int(input("enter the num"))
k=0
for i in range(0,n+1):
    for j in range(0,i):
        print(j,end='')
    print("\r")
for i in range(0,n+1):
    for j in range(0,i):
        print(i,end='')
    print("\r")

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print("\r")
for i in range(n,0,-1):
    k=k+1
    for j in range(1,i+1):
        print(k,end='')
    print("\r")

'''
'''
n=int(input("enter the num"))
#k=int(input("enter the wanted num"))
for i in range(n+1,0,-1):
    i=i-1
    for j in range(1,i+1):
        print(i,end=' ')
    print("\r")
'''
'''
n=int(input("enter the num"))
k=0
for i in range(0,n+1):
    for j in range(0,i):
        k=k+1
        print(k,end='')
    print("\r")

'''


n=int(input("enter the num"))
for i in range(n+1,0,-1):
    for j in range(0,i):
        print(i,end='')
        i=i-1
    print("\r")















































































































































































































































































