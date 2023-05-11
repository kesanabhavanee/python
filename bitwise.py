'''
n=int(input("enter the number"))
k=1
if n&k==k:
    print("odd")
else:
    print("even")

'''
'''
n=int(input("enter the number"))
k=1
if (n^k)!=(n+1):
    print("odd")
else:
    print("even")

'''

'''
n=int(input("enter the number"))
k=1
if n|k==n+1:
    print("even")
else:
    print("odd")
'''

'''
n=int(input("enter the number"))
k=1
initial=n>>k
final=initial<<k
if n!=final:
    print("odd")
else:
    print("even")

'''


n=int(input("enter the number"))
k=2

x=n|(1<<(k-1))
print(x)
'''
y=n&(~(1<<(k-1)))
print(y)

z=n^(1<<(k-1))
print(z)
'''






























































