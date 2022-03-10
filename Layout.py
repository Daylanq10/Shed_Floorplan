""" Basic layout of things that are pre determined """

from Tools.Displays import normal_label
from Tools.Shapes import rect


def absolute():
    """
    These are the pieces of the shed that are exact atm
    """
    # whole room
    rect((-15, 12.5), 30, 25)
    normal_label((0, 0), '30x25')
    # top door
    rect((-1.5, 13), 3, 1)
    # side door
    rect((14.5, 1.5), 1, 3)
    # top left windows
    rect((-10.5, 12.75), 4, 0.5)
    # bottom windows
    rect((-2, -12.25), 4, 0.5)
    # garage
    rect((-15.5, 4), 1, 8)
    # bathroom
    rect((-15, -6.5), 10, 6)
    normal_label((-14, -7.5), 'Bathroom')
    normal_label((-13.5, -8.5), '10x6')
    # bathroom door
    rect((-10, -6), 2.5, 1)
    # loft
    rect((5, 12.5), 10, 8)
    normal_label((7, 10), 'Loft w/ Stairs')
    normal_label((7.5, 9), '12x8')
    # stairs
    for stair in range(7):
        rect((3, 6 + (stair)), 2, 0.5)
    # furnace
    rect((7, -7), 3, 2)
