import random
import sys


def fx(r):
    while True:
        q= input("enter your number: ")
        
        u = int(q)
        if r==u:
            print("you guessed right\n")
            user = input("this program will start again if u press y/ n respectively: ").lower()
            if(user =="y"):
                re()
            else:
                sys.exit()
        if not q.isdigit():
            print("enter valid num and try again.")
        elif(u>r):
            print("you guessed higher hehe")
        elif(u<r):
            print("u gussed lower lol")
        
        fx(r)
    
    
def re():
    print("hello, this is a game where u have to guess number\n")
    x=int(input("enter the range for start: "))
    y =int(input("enter the range for end: "))
    ran = random.randint(x,y)
    fx(ran)



re()