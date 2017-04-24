#!/usr/bin/python

import aiml
import time
import signal
import re

# this is used for colored output
class colors:
    USER = '\033[92m'
    CLEVERTON = '\033[94m'

def uppercase(matchobj):
    return matchobj.group(0).upper()

def capitalizeAfterPunctuation(s):
    # essa bosta nao eh de deus
    return re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, s)

# returns a list of strings that should be capitalized when formatting responses
def retrieveNames():
    with open('KnowledgeBase/names.txt') as f:
        names = f.read().splitlines()

    return names

# The Kernel object is the public interface to the AIML interpreter.
k = aiml.Kernel()

# Use the 'learn' method to load the contents of an AIML file into the Kernel.
k.learn("KnowledgeBase/startup.xml")

# Use the 'respond' method to compute the response
# to a user's input sring. respond() returns the
# interpreter's response, which in this case we
# ignore
k.respond("load aiml cn")

username = "User"     # "User" by default
k.setPredicate("TalkerName", username)

names = retrieveNames()

# Loop forever, reading user input from the command
# line and printing respones
print colors.CLEVERTON + 'CLEVERton: ' + "Hello, human, I'm a chatbot specialized in 2017's Oscar, want to talk about it?"
while True:
    input = raw_input(colors.USER + username + ": ")
    time.sleep(0.2)     # a little bit of delay for responses makes for a more comfortable conversation

    if "date" or "day" in input:
        curr_date = str(time.ctime()[0:11])
        k.setPredicate("date", curr_date)   # get current date

    if "time" in input:
        curr_time = str(time.ctime()[11:19])    # get only current hour
        k.setPredicate("time", curr_time)

    response = k.respond(input)
    # if response is all caps we need to reformat it
    if response.isupper():
        response = response.capitalize()
        for name in names:
            if name.lower() in response:
                response = response.replace(name.lower(), name) # replaces lowercase name with capitalized one
        # after fixing own names, fix for punctuation
        response = capitalizeAfterPunctuation(response)

    print colors.CLEVERTON + "CLEVERton: " + response

    if "name" or "im" in input:
        username = k.getPredicate("TalkerName")
