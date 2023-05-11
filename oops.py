'''
#class,object,reference variable
class student:
    """this is oops concept"""
    #constructor to declare the variables
    def __init__(self):
        print("construtor executed")
        #below are variables
        self.name="shorty"
        self.num=73
        self.marks=99
    #to access the variables
    def talk(self):
        print("hello I'm ",self.name)
        print("my num ",self.num)
        print("my marks are",self.marks)

#creation of obj and s is the ref var
s1=student()
s2=student()
print(s1.name)
print(s2.num)
#calling method and passing argument but python vitual machine default takes it
s1.talk()
        
#print(student.__doc__)
#help(student)
#for the syntax purpose the above program

'''



'''
class student:
    """this is oops concept"""
    def __init__(self,name,num,marks):
        print("construtor executed")
        self.name=name
        self.num=num
        self.marks=marks
    def talk(self):
        print("method executed")
        print("hello I'm ",self.name)
        print("my num ",self.num)
        print("my marks are",self.marks)
s=student('shortyy',73,100)
print(s.name)
s.talk()

s1=student('hameed',87,100)
s1.talk()

s2=student('surendra',78,100)
s2.talk()

'''

'''
class student:
    """this is oops concept"""
    def __init__(self):
        print(id(self))
        
s1=student()
print(id(s1))

s2=student()
print(id(s2))

'''


'''
#multiple constructors
class Test:
    def __init__(self):
        print('no arg')
    def __init__(self,x):
        print("arg")

t1=Test(20)
t2=Test(10)

'''

'''
 
class student:
    cname='srkr'
    def __init__(self,x,y,z):
        print("construtor executed")
        self.name=x
        self.num=y
        self.marks=z

    #using obj related data-instance method
    def display(self):
        print("method executed")
        print("hello I'm ",self.name)
        print("my num ",self.num)
        print("my marks are",self.marks)
    #using only class level data-class method 
    @classmethod
    def getcollegename(cls):
        print('college name is ',cls.cname)

    #not related to class and object-static method
    #@staticmethod
    def findavg(x,y):
        print('avg is',(x+y)/2)


s=student('shortyy',73,100)

s.display()
s1=student('hameed',87,100)
s1.display()

s2=student('surendra',78,100)
s2.display()

student.getcollegename()

student.findavg(10,15 )

#s.findavg(2,5) 

'''

'''
#instance variables
class student:
    def __init__(self,name,num,clg):
        self.name=name
        self.num=num
        self.clg=clg
    def info(self):
        #one of the instance var only if it called by the obj ref
        self.marks=100
        #it will be overwritten by the obj ref age 
        self.age=25
        #access instance var from inside using obj ref
        print("my name is ",self.name)
    #del the instance var within class
    def delete(self):
        del self.clg,self.name

s1=student('shortyy',73,'srkr')
#here inst.var is called
s1.info()
s1.num=47
s1.age=24
#calling the dele method
s1.delete()
#del outside the class
#del s1.num

print(s1.__dict__)
#access instance var from outside using obj ref
#print(s1.name)


s2=student('gundu',23,'srkr')
s2.wife='begham'
#print(s2.name,s2.wife)
print(s2.__dict__)

'''

'''
class test:
    a=10
    def __init__(self):
        print(test.a)
        print(self.a)
        self.a=20
    def m1(self):
        print('inside inst method')
        print(test.a)
        print(self.a)

    @classmethod
    def m2(cls):
        print('inside class method')
        print(test.a)
        print(cls.a)

    @staticmethod
    def m3():
        print('inside static method')
        print(test.a)

t=test()
t.m1()
t.m2()
t.m3()
#below print statement for accessing from outside
print(test.a)
print(t.a)

'''


'''
#modifying the static variable
class test:
    a=10
    def __init__(self):
        test.a=20

    @classmethod
    def m1(cls):
        cls.a=30
        test.a=40
    @staticmethod
    def m2():
        test.a=50

t=test()
t.m1()
t.m2()
test.a=60
print(test.a)
print(t.a)
#creating an instance var
t.a=70
print(t.a)

'''



'''
class student:
    def __init__(self,name,num,marks):
        self.name=name
        self.num=num
        self.marks=marks
    def display(self):
        print("hi I'm",self.name)
        print("my num is",self.num)
        print("my marks are ",self.marks)
        
    def grade(self):
        if self.marks>=60:
            print("passed")
        elif self.marks>=50:
            print("second passed")
        else:
            print("failed")
    
n=int(input("enter no.of students"))
for i in range(n):
      name=input("enter the student name")
      num=int(input("enter the num"))
      marks=int(input("enter the marks"))
      s=student(name,num,marks)
      s.display()
      s.grade()
      print('*'*20)
'''

#setter and getter methods


class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks

    def grade(self):
        if self.marks>=60:
            print("passed")
        elif self.marks>=50:
            print("second passed")
        else:
            print("failed")
    
n=int(input("enter no.of students"))
for i in range(n):
      name=input("enter the student name")
      num=int(input("enter the num"))
      marks=int(input("enter the marks"))
      s=student()
      s.setName(name)
      s.setmarks(marks)
      s.grade()
      print("hi I'm",s.getName())
      print("my marks are ",s.getmarks())
      print('*'*20)






































































































































































































































