""" Main executable file to show layout options """

import turtle as t
from Tools.Shapes import rect


def basic_kitchen():
    """
    Configuration for normal kitchen
    """
    # back counter
    rect((-13, 12.5), 11, 2)
    # side counter
    rect((-15, 12.5), 2, 5)
    # sink
    rect((-11, 12.5), 2, 1.5)
    # fridge
    rect((-15, 7.5), 2, 2.5)
    # stove
    rect((-7, 12.5), 3, 2)
