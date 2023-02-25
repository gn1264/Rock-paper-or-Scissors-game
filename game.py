import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose R
    elif comp == 'R':
        if you=='S':
            return False
        elif you=='P':
            return True
    
    # Check for all possibilities when computer chose P
    elif comp == 'P':
        if you=='R':
            return False
        elif you=='S':
            return True
    
    # Check for all possibilities when computer chose S
    elif comp == 'S':
        if you=='P':
            return False
        elif you=='R':
            return True

print("Comp Turn:Rock(R) Paper(P) or Scissors(S)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 'R'
elif randNo == 2:
    comp = 'P'
elif randNo == 3:
    comp = 'S'

you = input("Your Turn: Rock(R) Paper(P) or Scissors(S)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")