import random
def game(comp,user):
    if comp==user:
        return None
    elif(comp=='s'):   
        if user=='w':
            return False
        elif user=='g':
            return True
    elif(comp=='w'):   
        if user=='g':
            return False
        elif user=='s':
            return True
    elif(comp=='g'):   
        if user=='s':
            return False
        elif user=='w':
            return True
     

print("Welcome to Snake, Water, Gun game")
i=1
compscore=0
userscore=0
while(i>0):
    user=input("Enter s for Snake\nEnter w for Water\nEnter g for Gun\nEnter q to quit\n")
    if user=='q':
        break
    randomno=random.randint(1,3)
    if randomno==1:
        comp="s"
    elif randomno==2:
        comp='w'
    else:
        comp='g'
    a=game(comp,user)
    print(f"Computer choose {comp}")
    print(f"You choose {user}")
    if a==None:
        print("Its Tie")
    elif a:
        print("You Win")
        userscore=userscore+1
    else:
        print("You Lose")
        compscore=compscore+1
if(userscore>compscore):
    print("You won:)")
    print(f"scores are\nUser={userscore}\nComp={compscore}")   
elif(compscore>userscore):
    print("You loose:(")
    print(f"scores are\nUser={userscore}\nComp={compscore}")  
else:
    print("Its a Tie")
print("Thankyou for playing")    
        