""" Basic shapes to put on floorplan """

import turtle as t
from Tools.Measurments import feet


def rect(start: tuple, width: int, height: int):
    """
    Takes start coordinate (x,y) and your desired width and height
    Starts in the top left corner and goes right
    """
    t.up()
    t.goto(feet(start[0]), feet(start[1]))
    t.down()
    t.forward(feet(width))
    t.right(90)
    t.forward(feet(height))
    t.right(90)
    t.forward(feet(width))
    t.right(90)
    t.forward(feet(height))
    t.up()
    t.home()
