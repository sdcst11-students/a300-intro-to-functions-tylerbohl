"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
y = 96
def title():
    print("NUMBER GUESSING GAME\nYou have 10 guesses\neach wrong geuss will tell you if you too high or too low\nGood Luck")

def game():
    for i in range(10):
        x = input("Enter an integer: ")
        x = int(x)
        if x == y:
            print(f"You won in {i+1} geusses")
            break
        elif x > y: 
           print("Too high")
        elif x < y: 
           print("Too low")
        elif i == 9:
            print("Game Over")
            break

title()

game()