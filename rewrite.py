'''new=open("log.txt","r")
f=open("logs.txt","w")
for data in new:
    f.write(data)'''

with open('log.txt','r') as firstfile, open('logs.txt','w') as secondfile:
    for line in firstfile:
        secondfile.write(line)

'''
firstfile=open('log.txt','r')
secondfile=open('logs.txt','w')
for line in firstfile:
    secondfile.write(line)
'''
