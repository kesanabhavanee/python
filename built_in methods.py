'''
import random
import string
maxlength=255
s=""
for i in range(random.randint(1,maxlength)):
    print(i)
    s=s+random.choice(string.ascii_letters)
    #print(s)
print(s)
#print(random.randint(0,10)/4)
print("genarate random char")
print(random.choice(string.ascii_letters))
print("random in a range")
str=""
for i in range(10):
    str=str+random.choice(string.ascii_letters)
print(str)

'''


'''
import random
l=[3,6,5,8,8]
print(random.choice(l))
t=(4,8,2,5)
print(random.choice(t))
d={4:"r",3:"u",6:0}
print(random.choice(list(d)))
print(random.random())
random.seed(0.5)
print(random.random())
'''

'''
#did not work
import random
import datetime
print(random.randrange(0,6))
print(random.randrange(6,10))
print(random.randrange(start=0,stop=10,step=3))
#print(random.randrange(3/2/2023,20/3/2023))
startdate=datetime.date(2020,3,1)
enddate=datetime.date(2022,3,1)
time_between_dates=enddate-startdate
'''
'''
print("ttotal_days",time_between_dates)
days=time_between_dates.days
print("days",days)
'''
'''
randomdays=random.randrange(time_between_dates)
randomdate=startdate+datetime.timedelta(days=randomdays)
print(randomdate)


'''




import random
l=[5,8,2,9]
random.shuffle(l)
print(l)
print(random.random())
print(random.uniform(0,6))
print(random.sample(l,2))
random.seed(10)
print(random.random())













