# To write a program for HangMan Game (Assigment - 4)

import random

words = ["apple", "orange", "mango", "banana", "kiwi"]

autoChoice = random.choice(words)
# print(autoChoice)

guessWord = ""

totalChance = 6

print('"__Welcome to the Hangman Game__"')

while totalChance > 0:
    guessedLetter = input("Enter the letter: ").lower()

    if len(guessedLetter) != 1:
        print("Please enter only one letter.")
        continue

    if guessedLetter not in autoChoice:
        totalChance = totalChance - 1
        print("Wrong Guess!")

    guessWord = guessWord + guessedLetter

    complete = True

    for i in autoChoice:
        if i in guessWord:
            print(i, end=" ")
        else:
            print("_", end=" ")  
            complete = False
    print()

    print(f"chances left:- {totalChance}")

    if complete:
        print("Congrats. You won the game!")
        break

if totalChance == 0:
    print("Game Over! You lose")
    print("The word was:", autoChoice)




