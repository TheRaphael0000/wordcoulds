import itertools
import os
import re

import nltk


p = os.path.dirname(__file__)
colormap = p + "/colormap.png"
mask = p + "/mask.png"


def get_words():
    f = open("all_apple_itunes_apps.csv", "rb").read().decode("utf8").lower()
    ls = f.split("\r\n")
    ws = [re.split(r"\W", l) for l in ls]
    words = list(itertools.chain(*ws))
    return words
