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
printing the bot's characteristics
"""

print "Bot Name: ", bot.__name__

print "Bot Verrsion: ", bot.__version__

print "Bot Owner: ", bot.__owner__
