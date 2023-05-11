'''
import pprint
message="it was a bright day.It is so lovely"
count={}
for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1
pprint.pprint(count)
'''
'''
birthdays={"harini":"april","SRivani":"oct","ravi":"nov"}
n=input("enter name")
for n in birthdays:
    birthdays.keys)
'''
'''
#updating
birthday={"hari":"april","sri":"oct","dev":"june"}
n=input("enter the name")
if n in birthday:
        print("name exist in the dict and its value is ",birthday.get(n))
        
else:
        print("not matched")
        option=input("enter yes or no")
        if option=="yes":
            month=input("enter the month")
            birthday.update({n:month})
            print(birthday)
        else:
            print("no need")
'''

'''
#birthday={"hari":"april","sri":"oct","dev":"june"}

#print(k)
#updating dict using fun and taking input from user
def birthday():
    dict={"hari":"april","sri":"oct","dev":"june"}
    '''
'''
    dict={}
    r=int(input("enter a num"))
    
    for i in range(r):
          name=input("enter the name")
          month=input("enter the month")
          dict[name]=month
    print(dict)
    '''
'''
    n=input("enter the name")
    if n in dict:
          print("name exist in the dict and its value is ",dict.get(n))
        #break
    else:
          print("not matched")
        #break
          option=input("enter yes or no")
          if option=="yes":
              month=input("enter the month")
              dict.update({n:month})
              return(dict)
          else:
              print("quit")
k=birthday()
print(k)

'''


'''

birthdays = { "Harini" : "April 13" , "Srivani" : "Oct 13" , "Ravi" : "Nov 13"}


str = input("Enter Name:")
if str in birthdays.keys():
    print(birthdays[str])
else:
    print("name is not in list")

    user_input = input(' Do you want to update Birthdays (yes/no): ')
    if user_input.lower() == 'yes':
        date = input("Enter Birthday")
        birthdays[str]= date
        print('added to data base')
    elif user_input.lower() == 'no':
        print('Thank You')
    else:
        print('Type yes or no')

print(birthdays)
'''
'''
dict={"fruit":"chickoo","dance":"folk","music":"soothing"}
i=input("enter value")
if i in dict:
    print("yes")
else:
    print("no")
'''

'''
d1={"fruit":"chickoo","dance":"folk","music":"soothing"}
d2={"hari":"april","sri":"oct","dev":"june"}
d3=d1.copy()
d3.update(d2)
print(d3)
'''
'''
dict={"fruit":"chickoo","dance":"folk","music":"soothing"}
#for dict_keys,dict_values in dict.items():
#   print(dict_keys,"is", dict_values)
for value in dict.items():
    print(dict[value])
'''



'''


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
 print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
 print('-+-+-')
 print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
 print('-+-+-')
 print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

'''


'''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
     print('-+-+-')
     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
     print('-+-+-')
     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
     printBoard(theBoard)
     print('Turn for ' + turn + '. Move on which space?')
     move = input()
     theBoard[move] = turn
     if turn == 'X':
         turn = 'O'
     else:
         turn = 'X'
printBoard(theBoard)

'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
 print("Inventory:")
 item_total = 0
 for k, v in inventory.items():
     print(str(v) + ' ' + k)
     item_total += v
 print("Total number of items: " + str(item_total))
displayInventory(stuff)















