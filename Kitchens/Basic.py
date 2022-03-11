""" Main executable file to show layout options """

import turtle as t
from Tools.Shapes import rect
from Tools.Displays import normal_label


def basic_kitchen():
    """
    Configuration for normal kitchen
    """
    # back counter https://www.ikea.com/us/en/p/sektion-base-cabinet-frame-white-80265398/
    rect((-10, 12.5), 3, 2)
    normal_label((-9, 11), "$58")
    # sink https://www.ikea.com/us/en/p/hillesjoen-double-bowl-top-mount-sink-stainless-steel-s39157491/
    rect((-9.8, 12), 2.5, 1.5)
    normal_label((-9.5, 9.5), "$165")
    # corner counter https://www.ikea.com/us/en/p/sektion-base-corner-cabinet-frame-white-70265501/
    rect((-15, 12.5), 2, 3)
    rect((-15, 12.5), 3, 2)
    normal_label((-14.5, 11), "$72")
    # in between counter https://www.ikea.com/us/en/p/sektion-base-cabinet-frame-white-90265388/
    rect((-12, 12.5), 2, 2)
    normal_label((-11.5, 11), "$46")
    # stove/oven (guessing $500-$600)
    rect((-7, 12.5), 2.5, 2)
    normal_label((-6.5, 11), "$600")
    # last counter https://www.ikea.com/us/en/p/sektion-base-cabinet-frame-white-90265388/
    rect((-4.5, 12.5), 2, 2)
    normal_label((-4, 11), "$46")
    # fridge (roughly 500)
    rect((-15, 9.5), 2, 2)
    normal_label((-15, 8), "$600")
