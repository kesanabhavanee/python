'''
s=input("enter the string")
x=s[0::]
x1=s[::-1]
if x==x1:
    print("yes")
else:
    print("no")
'''


def pal(str):
    s=input("enter the string")
    x=s[0::]
    x1=s[::-1]
    if x==x1:
        return "yes"
    else:
        return "no"

print(pal(str))

