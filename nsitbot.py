import os

import io

import numpy as np

from pandas import DataFrame

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB

"""
NSIT Bot main class
"""

class NSITBot(object):
    