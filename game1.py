'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''

import random

y = random.randint(0,10)

guess = int(input("Guess a number 0 to 10: "))

for x range(6): 
    if y == guess: 
    print("You guessed it!!!!")
    elif y <= guess:
    print("Your number is too high")
    elif y >= guess:
    print("Your number is too low")

