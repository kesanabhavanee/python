import sys 
f=open("logs.txt","r")
#contents=f.read()
word="binder"
L=f.readlines()
for i in L:
    #l=i.split()
    if word in i:
        print(i)
        '''
import subprocess
new=open("log.txt","w")
subprocess.check_call(["python","files.py"],stdout=new)
'''
'''
with open('log.txt','r') as firstfile, open('logs.txt','w') as secondfile:
    for line in firstfile:
        secondfile.write(line)
'''
