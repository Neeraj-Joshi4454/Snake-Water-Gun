

import random

def Game(comp, you):
    if comp == you:
        return None
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
    elif comp == 'W':
        if you == 'G':
            return False
        elif you == 'S':
            return True
    elif comp == 'G':
        if you == 'S':
            return False
        elif you == 'W':
            return True

print("Computers turn Done.")

x = random.randint(1,3)

if(x == 1):
    comp = 'S'

elif(x == 2):
    comp = 'W'

elif(x == 3):
    comp = 'G'


you = input("Your turn choose Snake(S), Water(W), Gun(G) : ")

y = Game(comp, you)

# default way to print variable with string
# print("Comp choose",comp)
# print(f"You choose",you)

# Another way to print variable with string which is fstring
print(f"Comp choose {comp}")
print(f"You choose {you}")

if y == None:
    print("Game is tie !")
elif y:
    print("You Win !")
else:
    print("You Lose !")