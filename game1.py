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

play_again = 0
#allows the user to play again if they enter 0 at the end
while play_again == 0:

#controls the range of the number being guessed
    lowest_number = int(input("Enter the lowest number you would like to guess from: "))
    highest_number = int(input("Enter the highest number you would like to guess from: "))
#range doesn't include last number so add 1 to highest number
    highest_number = highest_number + 1

    number = random.randint(lowest_number,highest_number)
    number_of_guesses = 1
# User controls how many turns they have to guess
    turns = int(input("Enter the number of turns you would like to guess: "))
    # print(number)

    try:
        guess = int(input("Guess a number! If you get it on the first try your AMAZING: "))
    # number_of_guesses < turns because they already had 1 guess
        while(number_of_guesses < turns): 
            if number == guess: 
                print("You guessed it!!!!")
                break 
            elif guess < lowest_number or guess >= highest_number:
                print("That guess was out of range")
                guess = int(input("Guess again... "))
            elif number <= guess:
                print("Your number is too high")
                guess = int(input("Guess again... "))
            else:
                print("Your number is too low")
                guess = int(input("Guess again... "))
            number_of_guesses = number_of_guesses + 1
        print("The number was " + str(number))

    except: 
        guess = int(input("You have one more guess to enter a NUMBER: ")) #allows them 1 more guess if they enter a string
        if number == guess:
            print("WOW! You got it") 
        else: 
            print("The number was " + str(number)) 
    
    play_again = int(input("If you want to play again enter 0, if you would like to stop enter 1: ")) #play again or no

if play_again == 1: 
    print("tHaAk YoU fOr PlAyInG!")