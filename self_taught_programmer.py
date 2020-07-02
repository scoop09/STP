# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('hello world')

for i in range(100):
    print("Hello World")
    
    #increment built in 
x=10
x+=1
x
11

hi="Hello world"

conditional 
x=30

if x<10:
   print("woot")
else:
    print("dino")
 ----------------------------------------  

#CH 4: Functions 
def f(x):
    return x*2

f(2)

#store result of function in a variable
def f(x):
    return x*2
z=f(4)

if z==8:
    print("ay its 8 mate")
else:
    print("fook what number?")

#accept more than one paramter
def f(x,y,z):
    return x+y+z
f(1,2,3)

age = input("Enter your age:")
int_age=int(age)
if int_age <21:
    print("yung buck!")
else:
    print("old tymer")

    #Reuse a function  by encapsulating functionality want to reuse 
def even_odd():
    n= input("type a number:")
    n=int(n) 
    if n%2 ==0:
        print("even")
    else:
        print("oddball")
even_odd()

#optional parameters 
def f(x=2):
    return x**x
print(f())
print(f(4))

#global and local scope 
#global 
x=1

#local
def f():
    x=1
    y=2
    print(x,y)
f()

#exception handling 
a=input("type a number:")
b=input("type another:")
a=int(a)
b=int(b)
try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero.")

#take a number as input and return it squared 
num=input("insert a number:")
int_num=int(num)
print(int_num**2) 
#print a sting
def f(x):
    a=str(x)
    print(a)
f(2)

#function 1: take integar as parameter and return result of integar divided by2 
def f(x):
    return x/2

f(4)



#function2: take an integer as parameter and return result of integer multiplied by 4 
def f(y):
    return y*4

f(4)

#call first function save the result as a variable and pass it as a parameter to the second function 
def f(x):
    return x/2

a=f(4)
a

def f(y):
    return a*4

f(4)

#converts a string to a float and returns the result. use exception to to catch 
def f(string_to_float):
    """
    returns float when given a string
    uses float function with parameter string_to_float
    """
    return float(string_to_float)
f("2")

--------------------------------------------
#CH 5: CONTAINERS 
#Lists 
fruit=["Bannana","Apple"]
fruit.append("Pomegranttttt")

#add to a list 
fruit[2]="derrr"

#dictionary 
rhymes={"1":"fun","2":"blue"}
n=input("type a number:")
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else: 
    print("not here bud")

#containers stored in other containers - list in list 

lists=[]
rap=["Kanye","HOV","Killa Mike"]
rock=["TP","Jim Page"]
lists.append(rap)
lists.append(rock)
print(lists)
rap=lists[0]
print(rap)
#append new item to rap list 
rap.append("Kendrick Lamar")
print(rap)

#dictionary within a list
bday={"Ricky":"6_19","Natalie":"7_9"}
my_list=[bday]
print(my_list)

#program user ask your height, fave color and returns result from dictionary 


Ricky={
       "height":"6_2",
       "color":"blue"
       }
answer= input("height, color")
if answer in Ricky:
    result=Ricky[answer]
    print(result)

#2)acollect 2 strings 
name="rickson"
job="dancer"
"{} was born to be a {}.".format(name,job)

#3)use a method to make string capitalizing first letter
sentence="rickson seaweed walked the line"
new=sentence.replace("rickson","Rickson")
#OR
"rickson seaweed walked the line".capitalize()

#4) split sentence 
sent="where now? who now? when now?".split("?")
print(sent)
#5)  
fox=["the","fox","jumped"]
fox=" ".join(fox)
fox=fox[0:-2]+"."
print(fox)

#6) replace s 
sent="a screaming comes"
sent.replace("s","")

#create string
name=woot woot
str(name)

#find index
name="Hemingway"
name.index("m")
#STRING MANIP
author="Kafka"
author[0]
#immutable so have to create new string
r="Rickson"
r="Ricksonia"
#concatdog
"r" + "ickson"
#multiply
"rickson"*3

#upper method to make all UPPER CASE  .upper()

#.format() method looks for occcurence in {} in string and replaces with parameters passed
"Ricky {}".format("Siewers")
last="Siewers"
"Ricky {}".format(last)

#{} multiple times
last="Siewers"
month="June"
"Ricky {} was born in {}".format(last,month)

#format useful with user input
place=input("Enter place:")
thing=input("Enter thing:")
r="""Ricky went to {} with a {}
""".format(place,thing)


print(r)

#Split
"Rickson_Scintillator!".split("_")

#pull ech letter 
each="Woof"
each[0]
each[1]

#Join 
first="Rickson"
result=":)".join(first)
    
#replace method to replace occurence of string 
equal="all animals son equales"
equal=equal.replace("a","heeeee")
print(equal)

#slicing return new iterable from a subset of items in another iterable 
books=["Harry Potter","Narnia","Soft james"]
books[:2] 

#FOR LOOPS 
people={"musician":"Jimi","athlete":"bird"}
for person in people:
    print(person)
    
person=["Jimi","Janis"]
i=0
for him in person: 
    new=person[i]
    new=new.upper()
    person[i]=new
    i=+1
print(person)

#ENUMERATE
person=["Jimi","Janis"]
for i,show in enumerate(person):
    new=person[i]
    new=new.upper()
    person[i]=new
print(person)

#Append multiple lists 
musician=["Jimi","Janis"]
athlete=["Tom","Tiger"]
all_famous=[]

for famous in musician: 
    famous=famous.upper()
    all_famous.append(famous)

for famous in athlete:
    famous=famous.upper()
    all_famous.append(famous)
print(all_famous)

#Range 
for num in range(1,12):
    print(num)
    
#WHILE 
x=10
while x>0: 
    print('{}'.format(x))
    x-=1
print("Happy New Year!")

#BREAK 
for i in range(0,100):
    print(i)
    break

qs=["q1","q2","q3"]
n=0
while True: 
    print("type q to quit")
    a=input(qs[n])
    if a=="q":
        break
    n= (n+1)%3
    
#CONTINUE - use continue statement or while loop 
i=1
while i<=5:
    if i==3:
        i+=1
        continue 
    print(i)
    i+=1
    
#NESTED LOOPS 
for i in range(1,5):
    print(i)
    for letter in ("y","z"):
        print(letter)
        
#for loops to append with a nest 
list1=["MJ","Scottie"]
list2=["Bird","Russell"]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)

#Challenges 
shows=["Dexter","Altered Carbon","Black Mirror"]
for show in shows:
    print(show)
    

for i in range(25,50):
    print(i)
    
shows=["Dexter","Altered Carbon","Black Mirror"]
for i, show in enumerate(shows):
    new=shows[i]
    new=new.upper()
    shows[i]=new
print(shows)
shows[0]


#infinite loop (with optio to type q to quit) and a list of numbers ***
numbers=[1,5,6]
while True:
    answer=input("Guess a number or type q to quit:")
    if answer=="q":
        break
    try:
        answer=int(answer)
    except ValueError:
        print("pls type a number or q to quit")
    if answer in numbers:
        print("Correcto!!!!!")
    else:
        print("nope!")
    
    
    
name=["tobias","shuban","kiley"]
while True:
    answer=input("guess name or q to quit:")
    if answer=="q":
        break
    try:
        answer=str(answer)
    except ValueError:
        print("type string or q")
    if answer in name:
        print("boom")
    else:
        print("again mate!")
        
#multiply numbers and append to third list 
list1=[9,2,3]
list2=[100,1000,10000]
list3=[]

for i in list1:
    for j in list2:
        list3.append(i*j)
print(list3)

#CH 8 MODULES
 import random

random.randint(0,100)

#CH 10 Hangman
https://github.com/calthoff/self_taught/blob/master/python_ex239.py/
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")

#guess random letter 
from random_word import RandomWords
r = RandomWords()
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman(r.get_random_word())

#another way to do random but with a word list you choose 
  
import random


def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()



def hangman(word):
    wrong=0 # tracks player 2 misses 
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters=list(word)  # list containing char in word that tracks each letter left
    board=["__"*len(word)] #creates board that is length of the hangman word
    win=Flase
    print("Welcome to hangman!")
    
    while wrong < len(stages) -1: #loops: games continues as long as wrong < length stages - 1 
        print("\n") #prints a blank for wrong guess
        msg="guess a letter" #output interactive message 
        char=input(msg) #input a letter to guess 
        if char in rletters : #if letter guess is in list containing word 
            cind=rletters.index(char) #get first index of letter player 2 guessed
            board[cind]=char #update board w/ correct letter guess
            rletters[cind]='$' #only returns the first index of character in word so need $ to find the next occurence in the next loop around
        else: 
            wrong +=1 #adds a miss
        print((" ".join(board))) #print scoreboard
        e=wrong+1 #gives you current hangman, need +1  since end slice not included in result 
        print("\n".join(stages[0:e])) #print hangman 
        if "__" not in board: #check if won game
            print("you win!")
            print(" ".join(board))
            win=True #breaks out of the loop 
            break 
        if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")

#1) define the hangman function 
def hangman(word):#player 2 has to guess this word 
    wrong=0 #variable tracks player 2 misses 
    stages=["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]#ze hangmon,mon!
    reltters=list(word) #list containing each char in word that tracks letters left 
    board=["__"]*len(word)#stores scoreboard
    win=False
    print("Welcome to Hangmon, mon!" )

#2) Loop to keep game going 

while wrong < len(stages)-1: #loop game continues as long as length of stages > wrong guesses
    print("\n")
    msg="Guess a letter"
    char = input(msg)
    if char in rletters:
        cind=rletters.index(char)
        board[cind] = char
        rletters[cind] = char
        rletters[cind] = '$' #if guessed correct add letter/ $ to ensure only first if multiple of that letter in word
    else:
        wrong +=1 #increment wrong by 1 
    print((" ".join(board)))
    e = wrong + 1 
    print("\n".join(stages[0:e]))
    if "__" not in board:
        print("you win!")
        print("".join(board))
        win=True
        break
    
    
##WAR  skeleton 
from random import shuffle 

class Card:
    

class Deck: 
    

class Player: 
    

class Game:
    
#WAR 
from random import shuffle 

from random import shuffle


class Card:
    #2 class variables: suits/values 
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    #2 instance variables: suits/values 
    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] +\
            " of " + \
            self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,
                     p1c,
                     p2n,
                     p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,
                      p1c,
                      p2n,
                      p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,
                         self.p2)
        print("War is over.{} wins"
              .format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()

import re

text= """ humans roamed the __NOUN__ since the beginning of ___PROPER_NOUN__"""
def mad_libs(mls):
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """
    hints = re.findall("__.*?__",
                      mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}"\
                   .format(word)
            new = input(q)
            mls = mls.replace(word,
                              new,
                              1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)

import re
string="two too."
f=re.findall("t[ow]o",string,re.IGNORECASE)
print(f)

import re

match = re.findall(".oo", "The ghost that says boo haunts the loo.")
print(match)


The Zen of Python


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!