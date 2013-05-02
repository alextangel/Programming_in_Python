# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math

# initialize global variables used in your code
secret_number = 0
remaining_guesses = 7

# helper function to initial game
def init():
    range100()

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global remaining_guesses
    remaining_guesses = 7    
    
    print "\nNew game. Range is from 0 to 100"
    print "Number of remaining guesses is " + str(remaining_guesses)
    global secret_number
    secret_number = random.randrange(0, 100)
    random.seed(secret_number)
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global remaining_guesses
    remaining_guesses = 10
    
    print "\nNew game. Range is from 0 to 1000"
    print "Number of remaining guesses is " + str(remaining_guesses)    
    
    global secret_number
    secret_number = random.randrange(0, 1000)
    random.seed(secret_number)

def get_input(guess):
    # main game logic goes here

    #remaining guesses
    global remaining_guesses
    remaining_guesses -= 1
    
    
    if remaining_guesses == 0 :
        print "\nGuess was " + guess
        print "Number of remaining guesses is " + str(remaining_guesses)
        print "You ran out of guesses. The number was " + str(secret_number)
        init()
    else :
        print "\nGuess was " + guess
        print "Number of remaining guesses is " + str(remaining_guesses) 
        if int(guess) > secret_number:
            print "Lower!"
        elif int(guess) < secret_number:
            print "Higher!"
        elif int(guess) == secret_number:
            print "Correct!"
            init()
          
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a gueess", get_input, 200)

init()

# start frame
f.start()

# always remember to check your completed program against the grading rubric