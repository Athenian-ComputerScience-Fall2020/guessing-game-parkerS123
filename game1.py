'''
Colaborators: Megan

Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
import random
number = random.randint(0,10)

number_of_guesses = 1

print(number)

try:
    guess = int(input("Guess a number 0 to 10 in 5 guesses: "))
    
    while(number_of_guesses < 5): 
        if number == guess: 
            print("You guessed it!!!!")
        elif number <= guess:
            print("Your number is too high")
            guess = int(input("Guess again... "))
        else:
            print("Your number is too low")
            guess = int(input("Guess again... "))
        number_of_guesses = number_of_guesses + 1
    print("The number was " + str(number))

except: 
    guess = int(input("You have one more guess to enter a NUMBER ")) 
    if number == guess:
        print("WOW! You got it")  