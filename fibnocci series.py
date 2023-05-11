n=int(input("enter the num"))
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
