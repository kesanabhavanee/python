'''
n=int(input("enter the range"))
s=set()
s1=set()
for i in range(n):
    string=input("enter the elements")
    s.update(string)
    s1.add(string)
print("input set:",s)
print(s1)
'''


'''
s1={1,2,3,4}
s2={4,6,1}
#s=s1&s2
#s=s1|s2
#s=s1-s2
#s=s1.difference(s2)
#s=s1.symmetric_difference(s2)
if s2print(s)
'''

'''
s1={1,2,3,4}
s2={5,6}
if s1.isdisjoint(s2):
    print("yes")
else:
    print("no")
'''


s1={1,2,7,4,10}
s2={2,3,9,54}
maxi=0
mini=0
mp=1
for n1 in s1:
    for n2 in s2:
        if n1*n2>mp:
            maxi=n1
            mini=n2
            mp=n1*n2
print(maxi,mini)
            
        
