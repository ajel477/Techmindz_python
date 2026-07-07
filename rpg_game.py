# To create an rpg game
#player vs enemy

# player vs enemy

import random

playerHP = 100
enemyHP = 100

player = input("Enter name of first player: ")
enemy = input("Enter the name of second player: ")

damage = random.randint(1,20)
turn = 1

while playerHP > 0 and enemyHP > 0:
    print(f"turn {turn}")
    print(f"{enemy} attacks {player}")
    playerHP = playerHP - damage
    print(f"player hp of {player} is {playerHP}")
    print(f"{player} strikes back")
    enemyHP = enemyHP - damage
    print(f"enemy hp of {enemy} is {enemyHP}")

    turn = turn+1
    if playerHP <= 0:
        print(f"{enemy}, won")
        break
    elif enemyHP <= 0:
        print(f"{player}, won")

