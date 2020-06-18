"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
  """Play a guessing game with a user.

  The exercise here is to rewrite the exampleGuessingGame() function
  from exercise 3, but to allow for:
  * a lower bound to be entered, e.g. guess numbers between 10 and 20
  * ask for a better input if the user gives a non integer value anywhere.
    I.e. throw away inputs like "ten" or "8!" but instead of crashing
    ask for another value.
  * chastise them if they pick a number outside the bounds.
  * see if you can find the other failure modes.
    There are three that I can think of. (They are tested for.)

  NOTE: whilst you CAN write this from scratch, and it'd be good for you to
  be able to eventually, it'd be better to take the code from exercise 2 and
  merge it with code from excercise 1.
  Remember to think modular. Try to keep your functions small and single
  purpose if you can!
  """
  low = str(-9^9)
  def not_number_rejector(message):
    numberask = str(input(message))

    while True:
        if numberask.isdigit() and int(numberask) >= int(low):
            return int(numberask)
        else:
            numberask = str(input(str(numberask) + " is not a valid bound number, \n" + message))

  print("\nWelcome to the guessing game!")
  print("You're going to guess a number between _ and _?")
  low = not_number_rejector("Please enter a lower bound: ")  
  print("You're going to guess a number between {lower} and _?".format(lower=low))
  high = not_number_rejector("Please enter an upper bound: ")
  print("You're going to guess a number between {lower} and {upper}?".format(lower=low, upper=high))

  actualNumber = random.randint(low, high)
  
  while True:
    guessedNumber = not_number_rejector("Please enter your guess: ")
    print("You guessed {},".format(guessedNumber),)
    if guessedNumber == actualNumber:
        print("Wohooo it was {}".format(actualNumber))
        return "You got it!"
    elif guessedNumber < actualNumber:
        print("Too small, try again :'(")
    else:
        print("Too big, try again :'(")
  

  # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
