"""
@Author : Manish Devgan
@Github : https://github.com/gabru-md
@Language : Python 2.7
"""
import sys
sys.path.append('..//')

from nsitbot import NSITBot

"""
very first example using NSITBot Module.
in this example a test Bot is created with the 
parameters / **kwargs and the name, version and
the owner are printed out
"""

bot = NSITBot(
    name="My Bot",
    owner="Manish Devgan",
    version="0.0.1"
)

"""
Bot created above.

__name__ = "My Bot"
__owner__ = "Manish Devgan"
__version__ = "0.0.1"
"""

"""
predicting messages type
"""

pred1 = bot.predict("should i choose nsit IT or dtu it?")
pred2 = bot.predict("Hey there sir!")

"""
predictions will be returned as a list containing the 'TYPE'
so to display, use:
    print pred[0] <--- gives the string result
"""

print "Predictions for Statement 1 and Statement 2 are : "
print pred1[0]
print pred2[0]
