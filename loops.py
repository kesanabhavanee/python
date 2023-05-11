'''
n=int(input("enter the numbers"))
for i in range(1,n+1):
    #print(i)
    if i%2==0:
        print(i)
'''

'''
n=int(input("enter the range"))
sum=0
for i in range(0,n):
    sum=sum+i
print(sum)
s=1
for i in range(1,n):
    s=s*i
print(s)
'''

'''
n=int(input("enter the number"))
#l=len(str(n))
#print(l)
count=0
while n>1:
    n=n/10
    count=count+1
    
print(count)
'''

'''
s="reverse"
l=len(s)
for i in range(0,l):
    print(s[l-i-1])

'''
'''
n=int(input("enter the number"))
c1,c2=0,0
for i in range(0,n):
    if i%2==0:
        c1=c1+1
    else:
        c2=c2+1
print(c1,c2)
'''

'''
n=int(input("enter the number"))
for i in range(0,n):
    if i%2= &i
'''

'''
n=int(input("enter the number"))
n1=0
n2=1
count=0
if n==0:
    print(n1)
elif n==1:
    print(n2)
else:
    while count<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
'''

'''
n=int(input("enter the number"))
i=0
while i<n:
    print(i,i*i)
    i=i+1
'''

'''
n=105
while(n>=7):
    print(n)
    n=n-7
'''

'''
n=10
sum=0
while n>0:
    print(n)
    sum=sum+n
    n=n-1
print(sum)
'''

'''
n1=int(input("enter the number"))
n2=int(input("enter the number"))
if n1>n2:
    while n1>n2:
        if n2%2==0:
            print(n2)
        n2=n2+1
else:
    while n2>n1:
        if n1%2==0:
            print(n1)
        n1=n1+1
'''


'''
n=int(input("enter the number"))
sum=0
mul=1
rev=0
while n>0:
    rem=n%10
    sum=sum+rem
    mul=mul*rem
    rev=rev*10+rem
    n=n//10
print(sum,mul,rev)
if rev==n:
    print("pali")
else:
    print("not")
'''

'''
n=int(input("enter the number"))
fact=1
if n==0 or n==1:
    print(fact)

while n>0:
    fact=fact*n
    n=n-1
    #if n==0 or n==1:
    #print(fact)
print(fact)
'''

'''
n=int(input("enter the number"))
k=1
while (k<=49 and n>=1):
    print(k,"___",n)
    k=k+1
    n=n-1
'''

'''
n=int(input("enter the number"))
i=1
while i<n:
    if n%i==0:
        print(i)
    i=i+1
'''

'''
l=[23,45,32,35,7,8]
s=len(l)
i=0
while i<s:
    if l[i]%2!=0:
        print(l[i])
    i=i+1
'''

'''
s='python'
l=len(s)
i=0
while i<l:
    print(s[i])
    i=i+1

'''

'''
n=int(input("enter the number"))
i=2
sp=1
sn=0
while i<=n:
    if i%2==0:
        sp=sp+i**2
        i=i+1
    else:
        sn=sn+i**2
        i=i+1
print(sp-sn)
'''

'''
import math
n=int(input("enter the number"))
p1=1
p2=1
i=1
s1=0
s2=0
while i<=n:
    p1=p1*i
    s1=s1+p1
    p2=i*i*i
    s2=s2+p2
    i=i+1
print(s1,s2)

'''

'''
n=int(input("enter nth number"))
x=int(input("enter the number"))
i=1
sum=0
while i<=n:
    sum=sum+((x^i)/i)
    i=i+1
print(round(sum,2))   
    
'''

'''
n=int(input("enter the number"))
i=0
str='2'
while i<n:
    print(str,end='\t')
    str=str+'2'
    i=i+1

'''

'''
i=101
while i<500:
    if i%13==0 and i%3!=0:
        print(i)
    i=i+1
'''

'''
n=int(input("enter the number"))
f=1
i=1
sum=1
while i<=n:
    f=f*i
    #sum=sum+(1/f)
    i=i+1
print(f)
#print(sum)
'''

'''
import math
n=list(input("enter the binary num"))
p=0
dec=0
for i in reversed(n):
    dec=dec+int(i)*pow(2,p)
    p=p+1
    print(i)
print(dec)
'''

'''
num=int(input("enter the num"))
bin=0
p=1
n=num
while n>0:
    rem=int(n%2)
    bin=bin+rem*p
    p=p*10
    n=n/2
print(bin)

'''

'''
n1=int(input("enter the number"))
n2=int(input("enter the number"))
if n1>n2:
    smaller=n2
else:
    smaller=n1
for i in range(1,smaller+1):
    if (n1%i==0) and (n2%i==0):
        hcf=i
print(hcf)
'''

'''
n1=int(input("enter the number"))
n2=int(input("enter the number"))
if n1>n2:
    greater=n1
else:
    greater=n2
while(True):
    if (greater%n1==0) and (greater%n2==0):
        lcm=greater
        break
    greater=greater+1
print(lcm)

'''







































































































































































































































    

































