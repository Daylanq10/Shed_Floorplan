""" Labelling options """

import turtle as t
from Tools.Measurments import feet


def normal_label(position: tuple, name: str):
    """
    Takes start coordinate (x,y) and the label name
    """
    t.up()
    t.goto(feet(position[0]), feet(position[1]))
    t.write(name, font=('Arial', 12, 'normal'))
    t.up()
    t.home()
