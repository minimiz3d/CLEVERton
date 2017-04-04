import aiml
import time

# this is used for colored output
class colors:
    USER = '\033[92m'
    CLEVERTON = '\033[94m'

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
    input = raw_input(colors.USER + username + ": ")

    if ("date" or "time") in input:
        curr_time = str(time.ctime())
        k.setPredicate("date", curr_time)

    print colors.CLEVERTON + "CLEVERton: " + k.respond(input)

    if "name" in input:
        username = k.getPredicate("TalkerName")
