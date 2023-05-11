import math
n=int(input("enter the number"))
l=len(str(n))
print(l)
sum=0
temp=n

while temp!=0:
    rem=temp%10
    sum=sum+pow(rem,l)
    temp//=10
if sum==n:
    print("yes")
else:
    print("no")
