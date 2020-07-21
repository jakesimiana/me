import math


# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    numbers = list(range(9,0,-1))
    for a in numbers:
        print("Getting ready to start in " +str(a))
    print("Let's go!")

    base = 3
    height = 4
    hypotenuse = base**2 + height**2
    area = int(base*height/2)
    print("area = " + str(area))
    print("side lengths are:")
    print("base: "+str(base))
    print("height: "+str(height))
    print("hypotenuse: "+str(hypotenuse))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    numbers = list(range(start-stop+1,stop-stop,-1))
    for a in numbers:
        print(message+ " " +str(a))
    print(completion_message)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    return math.sqrt(base**2 + height**2)


def calculate_area(base, height):
    return base*height/2


def calculate_perimeter(base, height):
    return base + height + math.sqrt(base**2 + height**2)



def calculate_aspect(base, height):
    if height > base:
        return "tall"
    elif height < base:
        return "wide"
    else:
        return "equal"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    
    
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    area=calculate_area
    perimeter=calculate_perimeter
    aspect=calculate_aspect
    if facts_dictionary["aspect"] == "tall":
        diagram = tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        diagram = wide.format(**facts_dictionary)
    else:
        diagram = equal.format(**facts_dictionary)
    facts = pattern.format(**facts_dictionary)
    return( diagram + "\n" + facts)


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    f=get_triangle_facts(base, height)
    d=tell_me_about_this_right_triangle(f)
    if return_diagram and return_dictionary:
        return {"diagram": d, "facts":f}
    elif return_diagram:
        return d
    elif return_dictionary:
        return f
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid(api_key):
    import requests

    baseURL = (
        "http://api.wordnik.com/v4/words.json/randomWords?"
        "api_key={api_key}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(api_key="", length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list


def get_a_word_of_length_n(length):
    NumberPyramid = []
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    
    #Go through all the numbers and search the word length of each number in the table
    fullurl = url.format(len=length)
    #Search URL
    pull = requests.get(fullurl)   
    #Pull the word data and change it to text     
    data = pull.text
    NumberPyramid.append(data)
    return NumberPyramid


def list_of_words_with_lengths(list_of_lengths):
    NumberPyramid = []
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    
    #Go through all the numbers and search the word length of each number in the table
    fullurl = url.format(len=length)
    #Search URL
    pull = requests.get(fullurl)   
    #Pull the word data and change it to text     
    data = pull.text
    NumberPyramid.append(data)
    return NumberPyramid


if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
