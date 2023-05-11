'''
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    print(ham)
    print(eggs)
spam()
'''
'''
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
'''

'''
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


'''


'''
import random
messages = ['It is certain',
 'It is decidedly so',
 'Yes definitely',
 'Reply hazy try again',
 'Ask again later',
 'Concentrate and ask again',
 'My reply is no',
 'Outlook not so good',
 'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])

'''

'''
spam = ['apples',
 'oranges',
                 'bananas',
'cats']
print(spam)

'''


'''
import copy
spam=[0,4,3,2,[9,8]]
cheese=copy.copy(spam)
cheese[0]="hii"
print(spam,cheese)
cheese=copy.deepcopy(spam)
cheese[0]="hii"
print(spam,cheese)

'''


'''
grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]
print(*grid,sep='\n')
'''



birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
print(birthdays)
for k in birthdays.keys():
    print(k)
for v in birthdays.values():
    print(v)
for i in birthdays.items():
    print(i)






'''
def number(num):
    #num=input()#415-555-4242
    if len(num)!=12:
        return False
    for i in range(3):
        if not num[i].isdecimal():
            return False
    if num[3]!='-':
        return False
    for i in range(4,7):
        if not num[i].isdecimal():
            return False
    if num[7]!='-':
        return False
    for i in range(8,12):
        if not num[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if number(chunk):
        print('Phone number found: ' + chunk)
#print('Done')
'''





































































































