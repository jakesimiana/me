# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.
"""
import string
import time


def string_please() -> str:
    """Returns a string, anything you like."""
    
    return 'Hi Ben'


def list_please() -> list:
    """Returns a list, anything you like."""
    cool_list = list(range(10))
    
    return cool_list


def dictionary_please() -> dict:
    """Returns a dictionary, anything you like."""
    cool_big_dic = {'dog' :' the best' , 'cat' :'not bad' , "ferret" : 'god'}
    
    return cool_big_dic


def is_it_5(some_number) -> bool:
    """Returns True if the argument passed is 5, otherwise returns False."""
    well_is_it = False
    if some_number == 5:
        well_is_it = True
    else:
        well_is_it = False
    
    return well_is_it


def take_five(some_number) -> int:
    """Subtracts 5 from some_number."""
    new_number = int(some_number) - 5
    
    return new_number


def greet(name="Towering Timmy"):
    """Return a greeting.
    return a string of "Hello " and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    message = 'Hello ' + str(name)
    return message


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = input_list.count(3)

    return count


def n_counter(search_for_this, input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of times search_for_this shows up in the input_list.
    Return an integer.
    """
    count = input_list.count(search_for_this)
    
    return count


def fizz_buzz():
    """Do the fizzBuzz.

    This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
    from https://blog.codinghorror.com/why-cant-programmers-program/
    
    Return a list that has an integer if the number isn't special, 
    and a string if it is. E.g. 
        [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 
         'Fizz', 'Buzz',  11, 'Fizz', 13, 14, 
         'FizzBuzz', 16, 17, ...]
    """
    fizzBuzzList = []
    # your code here
    cool_list = list(range(1,101))
    for i in cool_list:
        if i%3==0 and i%5==0:
            fizzBuzzList.append("FizzBuzz")
        elif i%3==0:    
            fizzBuzzList.append("Fizz")
        elif i%5==0:    
            fizzBuzzList.append("Buzz")  
        else:
            fizzBuzzList.append(i)

    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.
    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: strings are pretty much lists of chars. 
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """
    bars = "".join(["|" + input_string[i] for i in range(len(input_string))] +["|"])

    return bars




def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'"""
    # fmt: off
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    # fmt: on
    filtered = []

    for pet in pets:
        if pet.find(letter) >=0:
            filtered.append(pet)
        else:
            pass
    
    return filtered


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.
    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string

    the_alphabet = string.ascii_lowercase
    popular_letter = ""
    max = -1

    #Searching through pet names using pet_filter 
    for i in range(len(the_alphabet)):
        letter = str(the_alphabet[i])
        new = len(pet_filter(letter))

        #Updating Maximum
        if new > max:
            max = new
            popular_letter = the_alphabet[i]
        else:
            pass

    return popular_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4 
    If we set minLength=18 and maxLength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    """

    import requests

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    
    wd = {
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }

    #Going through word lengths
    for wordlength in range(3,8):
        fullurl = url.format(len=wordlength)
        templist =[] 

        #searching the url
        for i in range(0,3):
            pull = requests.get(fullurl)

            # this retrives the word from the url
            if pull.status_code is 200:         
                word = str(pull.content)
                dict_entry = word[2:len(word)-1]

            templist.append(dict_entry) 

        wd[wordlength]=templist

    return wd


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    import random

    my_dict = make_filler_text_dictionary()
    words =[]

    #searching for words    
    for i in range(0,number_of_words):

        big_words = random.randint(3,7)
        small_words = random.randint(0,2)
        words.append(my_dict[big_words][small_words])

    return(', '.join(words))


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.
    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the 
    dictionary into and out of the file. Be careful when you read it back in, 
    it'll convert integer keys to strings.
    If you get this one to work, you are a Very Good Programmer™!
    """
    import random
    import os
    import json

    fname = "dict_racey.json"
    word_list =[]

    #Checking for Json File and make_filler_text_dictionary
    if os.path.isfile(fname):
        print("loading from file")
    else:
        dictt = make_filler_text_dictionary()
        f = open(fname, "w")
        abba = json.dumps(dictt)
        f.write(abba)
        f.close
    
    #Opening Json File
    f=open(fname, "r")
    content= f.read()
    temp_dict = json.loads(content)

    #Searching for Words
    for i in range(0,number_of_words):
        big_words = str(random.randint(3,7))
        small_words = random.randint(0,2)
        word_list.append(temp_dict[big_words][small_words].capitalize())
    
    return (', '.join(word_list)+".")


if __name__ == "__main__":
    print("string_please", type(string_please()) == str)
    print("list_please", type(list_please()) == list)
    print("dictionary_please", type(dictionary_please()) == dict)
    print("is_it_5", is_it_5(5))
    print("is_it_5", is_it_5(6))
    print("take_five", take_five(5))
    print("take_five", take_five(3))
    print("greet:", greet())
    print("three_counter:", three_counter())
    print("n_counter:", n_counter(7))
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", put_behind_bars())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(10):
        print(i, fast_filler())
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
