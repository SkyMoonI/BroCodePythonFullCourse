# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts.
import messages
import messages as msg
from messages import hello, bye
from messages import *  # import all the content

messages.hello()
msg.bye()
hello()
bye()

# help("modules")  # shows all the modules that python has
