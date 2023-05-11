#without regular expressions
'''
f=open("logs.txt","r")
n=open("log.txt","a")
n.truncate(0)
list=['reboot','crash','tomstone']
L=f.readlines()
for i in L:
    for item in list:
        if item in i:
        
            new=open("log.txt","a")
            new.write(i)
            new.close()
            print(i)
'''

'''
import re
f=open("logs.txt","r")
n=open("log.txt","a")
n.truncate(0)
list=['reboot','crash','tomstone']
L=f.readlines()
for i in L:
    #for item in list:
        #if item in i:
    r=re.findall(list)
    
    new=open("log.txt","a")
    new.writelines(i)
    new.close()
        print(i)
    else:
        print("not")
        


'''

import re
f=open("logs.txt","r")
n=open("log.txt","w")
#n.truncate(0)
#list=['reboot','crash','tomstone']
L=f.readlines()
#print(L)
#LINES = L.split('\n')
Search_String = "reboot"
#Search_String1="crash"
for LINE in L:
    if re.findall(r'\b{}\b'.format(Search_String),LINE):
    #if re.findall(r'\breboot\b|\bcrash\b|\btombstone\b',LINE):
        print(LINE)
        new=open("log.txt","a")
        #new.write(LINE)
        #new.close()
        #new=open("log.txt","a")
        new.writelines(LINE)
        new.close()
        #print(i)
        #print(i)
    #for item in list:
        #if item in i:

'''
'''
'''
    lines=i.split('\n')
    search_string="crash"
    for line in lines:
        if re.search(r'\b{}\b'.format(search_string),line):
            print(line)
'''
'''

'''

        
    





#subprocess.check_call(["python","files.py"],stdout=new)


  
'''
import re
f=open("logs.txt",encoding="UTF-8")
data=f.read()
print(data)
f.close()


for i in data:
    word=re.search(r'reboot',i)
    if word==None:
        print("no")
    else:
        print(i)

'''


'''
f=open("logs.txt","r")
#n=open("log.txt","a")
res = f.readlines()
word=['reboot','crash','tombstone']
n=open("log.txt","w")
n.truncate(0)


def newfile():
    
    for result in res:
        for item in word:
            if item in result:
                new=open("log.txt","a")
                new.write(result)
                n.close()
obj=newfile()
'''


'''

if result.find(w1):
            print(result,file=n)
        if result.find(w2):
            print(result,file=n)
'''











