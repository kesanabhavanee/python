import re
'''
pattern=re.compile("hello")
pattern=re.compile("hello",flags=re.I)
match=pattern.match("ello hello world",pos=5,endpos=10)
k=type(match)
print(k)
y=pattern.search("say hello hello")
print(y)
x=pattern.findall("say hello Hello")
print(x)
digits=re.compile("\d")
y=digits.findall("1 2 3 4 5.5")
print(y)
match_iter=pattern.finditer(" say hello Hello")
#next(match_iter)
for match in match_iter:
    print("match is ",match)

i=re.findall("hello","say hello Hello",flags=re.I)
print(i)

'''
'''
txt="this book costs $15."
pattern=re.compile("$15")
y=pattern.search(txt)
print(y)
pattern=re.compile("\$15")
x=pattern.search(txt)
print(x)

'''

'''
txt="The first Premiere League was played in 2008 and 1 player did not play with 3rd player while 8th player is not feeling well"
pattern=re.compile("[^A-Z3-9\s]")
#x="".join(pattern.findall(txt))
x=pattern.findall(txt)
print(x)
pattern=re.compile("\d+")#\d
y=pattern.findall(txt)
print(y)
'''
'''
txt="The first Premiere League was played in 2008 at that age is 40"
pattern=re.compile("thes|age",flags=re.I)
x=pattern.findall(txt)
print(x)
'''
'''
txt="""
I have 2 dogs.One dog is 1 year old dog and other one is 2 year old.
Both dogs are vey cute
"""
pattern=re.compile("dog?")
x=pattern.findall(txt)
print(x)
#pattern=re.compile("[^\d\s]")
#x="".join(pattern.findall(txt))
#print(x)
'''

'''
txt="""
file1.txt
file_one.txt
file.txt
fil.txt
file.xml
"""
pattern=re.compile("file\w*\.txt")
x=pattern.findall(txt)
print(x)
pattern=re.compile("file\d+\.txt")
y=pattern.findall(txt)
print(y)
'''
'''
txt="""
123454
432
5647
4436
123
87
122345
"""



pattern=re.compile("\d{,4}")
x=pattern.findall(txt)
print(x)
'''

'''
string = "bhavanee is aunty,harini is aunty,bhavanee is getting promotion"
pattern = re.compile(r'^b*e')
x = re.findall(pattern,string)
print(x)
'''

'''
import sys
while True:
    print("type exit")
    response=input()
    if response=="exit":
        #sys.exit()
        break
    print('you typed'+response+'.')

'''







'''
date=input("enter the date")
pattern=re.compile(r"\d{2}[/][A-Z]{3}[/]\d{4}")
p=pattern.search(date)
print(p)
#\d{2}[/]\[A-Z]{3}[/]\d{4}
#\d\d[/](JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC)[/]\d\d\d\d")

'''


'''
import re
phonenumREgex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#phonenumREgex.search("my num is 423-768-3443")
mo=phonenumREgex.findall(resume)
#mo.group()
'''


'''
vowelREgex=re.compile(r'[aeiouAEIOU]')
y=vowelREgex.findall("robocop eats bayby food.")
print(y)                 
atREgex=re.compile(r'.{1,2}at')
k=atREgex.findall("the cat in the hat sat at the eating thr rat")
print(k)

'''
'''
find-------
'First name:AI Last name:ML'
'First name:AI Last name:ML'
>>> 'First name:AI Last name:ML'.find(':')
10
>>> 'First name :AI Last name:ML'.find(':')
11
>>> 'First name :AI Last name:ML'.find(' ')
5
'''

#nameRegex=re.compile(r'First name: (.*) Last name: (.*)
'''
serve='<To serve humans> for dinner.>'
nongreedy=re.compile(r'<(.*?)>')
i=nongreedy.findall(serve)
print(i)
nongreedy=re.compile(r'<(.*)>')
j=nongreedy.findall(serve)
print(j)
print(serve)
'''

'''
name=re.compile(r'Agent \w+')
t=name.findall('Agent alice gave the secret document to Agent bob')
print(t)
u=name.sub('reacted','Agent alice gave the secret document to Agent bob')
print(u)
name=re.compile(r'Agent (\w)\w*')
p=name.findall('Agent alice gave the secret document to Agent bob')
print(p)
t=name.sub(r'Agent \1****','Agent alice gave the secret document to Agent bob')
print(t)

'''

'''
number= re.compile(r'\d{3}-\d{3}-\d{4}')
pattern = number.search('My number is 417-555-4242.')
print('Phone number found: ' + pattern.group())

'''

'''
txt="abbc is the bbba of the ababbbacd"
pattern=re.compile(r'd{3}\w+')
x=pattern.findall(txt)
print(x)

'''


'''
txt="the adventures of batman and the batman are appreciable"
pattern=re.compile(r'bat(wo)?man')
x=pattern.findall(txt)
print(x)
'''



'''
count=0
pattern=re.compile("ab")
match=pattern.finditer("abaababa")
for m in match:
    print(m.start(),"...",m.end(),"...",m.group())
    count+=1

print(count)

#print(m.start(),"...",m.end(),"...",m.group())
'''

'''
#match=re.finditer("[abc]","a7Sb@k9#Az")
#match=re.finditer("[^abc]","a7Sb@k9#Az")
#match=re.finditer("[a-z]","a7Sb@k9#Az")
#match=re.finditer("[A-Z]","a7Sb@k9#Az")
#match=re.finditer("[0-9]","a7Sb@k9#Az")
#match=re.finditer("[a-zA-Z]","a7Sb@k9#Az")
#match=re.finditer("[a-zA-Z0-9]","a7Sb@k9#Az")
match=re.finditer("[^a-zA-Z0-9]","a7Sb@k9#Az")
for m in match:
 print(m.start(),"....",m.end(),"..",m.group())

'''

'''
#match=re.finditer("\s","a7Sb @k 9#Az")
#match=re.finditer("\S","a7Sb @k 9#Az")
#match=re.finditer("\d","a7Sb @k 9#Az")
#match=re.finditer("\D","a7Sb @k 9#Az")
#match=re.finditer("\w","a7Sb @k 9#Az")
#match=re.finditer("\W","a7Sb @k 9#Az")
match=re.finditer(".","a7Sb @k 9#Az")
for m in match:
 print(m.start(),"......",m.group())
'''

'''
#match=re.finditer("a","abaabaaab")
match=re.finditer("a+","abaabaaab")
#match=re.finditer("a*","abaabaaab")
#match=re.finditer("a?","abaabaaab")
#match=re.finditer("a{2}","abaabaaab")
#match=re.finditer("a{2,3}","abaabaaab")
for m in match:
 print(m.start(),"......",m.group())
'''


'''
p=input("Enter pattern to check:")
m=re.fullmatch(p,"hyderabad")
if m!= None:
 print("Match is available at the beginning of the String")
 print("Start Index:",m.start(), "and End Index:",m.end())
else:
 print("Match is not available at the beginning of the String")
print(m)

'''


'''
p=input("Enter pattern to check: ")
m=re.search(p,"hyderabad")
if m!= None:
 print("Match is available")
 print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
else:
 print("Match is not available")
print(m)


'''
'''
l=re.findall("[0-9]","a7b9c5kz")
print(l)

print(m)

'''

'''
s=re.sub("[a-z]","#","srf42efxrf4")
print(s)
'''

'''
s=re.subn("[a-z]","#","1245")

print(s)
print("The Result String:",s[0])
print("The number of replacements:",s[1])

'''

'''
import re
l = re.split(",",
"shashi,nandan,shanvi,mohan,sruthi")
print(l)
for t in l:
 print(t)

'''

'''
import re
l = re.split("so", "www.durgasoft.com")
print(l)
#for t in l:
# print(t)[0-9][0-9][0-9]?
25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0]|[1-9][0-9]?

'''




'''
n=input("enter the number")
if re.match('(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9]\.){3}&(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])$',n):
    print("valid")
else:
    print("invalid")
'''



'''
f=open("ipaddress.txt","r")
new=open("outputs.txt","w")
new192=open("ip192.txt","w")
new192_series=open("new1p192.txt","w")
new.truncate(0)
l=f.readlines()
#out=" "
for i in l:
    
    if re.findall('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])$',i):
        l1=i.split(".")
        if l1[0]=="192":
            print(l1)
        if l1[0]=='192':
            new192_series.write(i)
            
        if "192" in i:
            new192.write(i)
        #print(i)
        #out.append(i)
        #print(out)
        #out="valid ip address is"
        #new=open("outputs.txt","a")
        new.write(i)
       
new.close()
new192.close()
new192_series.close()
'''


#('(25[0-5]|2[0-4][0-9]|(0|[1-9][0-9][0-9]*)\.){3}(25[0-5]|2[0-4][0-9]|(0|[1-9][0-9][0-9]*))',i):

#(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9]?\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9]?\.)',i):

#(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-1]|[1-9]?[0-9]?\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-1]|[1-9]?[0-9]?)',i):

#(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9]\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]|[1-9][0-9])$',i):


'''
n=input("enter the number")
if re.match('^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|(?:[0-9]|[1-9][0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|([0-9]|[1-9][0-9]))$',n):
    print("valid")
else:
    print("invalid")

'''

'''
f=open("phonenumbers.txt","r")
new=open("phnoutput.txt","w")
new.truncate(0)
l=f.readlines()
for i in l:
    if re.findall('^([6-9][0-9]{9})$',i):
                  new.write(i)
new.close()
'''

f=open("gmailids.txt","r")
new=open("gmailoutput.txt","w")
new.truncate(0)
l=f.readlines()
for i in l:
    if re.findall("\w[\.]*@gmail\.com",i):
        new.write(i)
new.close()






