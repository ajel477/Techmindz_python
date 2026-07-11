# Snake and Ladder Game

import random

WinningScore = 100
player1 = 1
player2 = 1
turn = 1

ladders = {3:11, 9:21, 17:30, 45:51, 69:90, 78:81, 88:96}
snakes = {7:2, 12:7, 31:25, 44:10, 68:60, 91:22}

print("Player starts at square 1")

while True:
    if turn == 1:
        currentPlayer = player1
        print("\nPlayer 1's Turn")
    else:
        currentPlayer = player2
        print("\nPlayer 2's Turn")

    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("Dice:", dice)

    newPosition = currentPlayer + dice

    if newPosition > WinningScore:
        print("Need an exact roll to reach 100!")
        print("Player stays at square", currentPlayer)

    else:
        currentPlayer = newPosition
        print("Player reached square", currentPlayer)

    if currentPlayer in ladders:
        print("You found a ladder!")
        currentPlayer = ladders[currentPlayer]
        print("You climbed to square", currentPlayer)
    elif currentPlayer in snakes:
        print("Oops! You got bitten by a snake")
        currentPlayer = snakes[currentPlayer]
        print(f"you slide down to {currentPlayer}")

    if currentPlayer == WinningScore:
        if turn == 1:
            print("Congratulations! Player 1 Won!")
        else:
            print("Congratulations! Player 2 Won!")
        break

    if turn == 1:
        player1 = currentPlayer
        turn = 2
    else:
        player2 = currentPlayer
        turn = 1
    