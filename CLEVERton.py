import aiml
import time
import signal

TIMEOUT = 3 # number of seconds to wait before another user input

# this is used for colored output
class colors:
    USER = '\033[92m'
    CLEVERTON = '\033[94m'

# called when user didn't input anything for some time
def timedout(signum, frame):
    print "interrupted"

signal.signal(signal.SIGALRM, timedout)

def user_input():
    try:
        input = raw_input(colors.USER + username + ": ")
        return input
    except:
        return "timedout"

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

# Loop forever, reading user input from the command
# line and printing respones
while True:
    #signal.alarm(TIMEOUT) # sets time limit for answer
    input = raw_input(colors.USER + username + ": ")
    time.sleep(0.2)     # a little bit of delay for responses makes for a more comfortable conversation
    #signal.alarm(0)     # disable alarm after getting input

    if "date" or "day" in input:
        curr_date = str(time.ctime()[0:11])
        k.setPredicate("date", curr_date)   # get current date

    if "time" in input:
        curr_time = str(time.ctime()[11:19])    # get only current hour
        k.setPredicate("time", curr_time)

    print colors.CLEVERTON + "CLEVERton: " + k.respond(input)

    if "name" or "im" in input:
        username = k.getPredicate("TalkerName")
