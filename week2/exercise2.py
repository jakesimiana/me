"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
Remember that all files must also pass the
linter with no errors or warnings!
"""

import string

#Define a function 'getLetter' which has the input variable 'index'
def getLetter(index):
    alphabet = string.ascii_lowercase + " " # Creates a variable alphabet which equals a string (in lowercase) + a space ' '
    return alphabet



def week2exersise2():
    indices = [12, 2, 26, 7, 0, 12, 12, 4, 17]
    wordArray = list(map(getLetter, indices))
    wordArray[0] = wordArray[0].upper()
    wordArray[1] = wordArray[1].upper()
    wordArray[3] = wordArray[3].upper()
    secret_word="".join(wordArray)
    print(secret_word)
    return secret_word


if __name__ == "__main__":
    print(week2exersise2())