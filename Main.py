""" Main executable file to show layout options """

import turtle as t
from Layout import absolute
from Kitchens.Basic import basic_kitchen


if __name__ == '__main__':
    t.speed("fastest")
    t.hideturtle()
    absolute()
    basic_kitchen()
    t.done()
