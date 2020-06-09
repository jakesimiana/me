"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will create a list of strings called some-words
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# These lines of codes makes a variable called word, which is any string in somewords, and prints the list off
for word in some_words:
    print(word)

# These lines of codes makes a variable called x, which is also any string in somewords, and prints the list off
for x in some_words:
    print(x)

# This line prints all the strings in the list some_words
print(some_words)

# This line checks if the amount of words in the some_words list are greater than 3, and if there is, it will print the string 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words')


# This line defines a function called usefulFunction
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    #This line runs plat.uname which fetched the users system details including Windows verion, device name, software etc. It then prints it out.
    print(platform.uname())

usefulFunction()
