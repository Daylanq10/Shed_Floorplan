import turtle as t

def feet(num: int) -> int:
    """
    Takes your desired measurment in feet and converts to turtle length
    """
    return num * 15
    

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

def label(position: tuple, name: str):
    """
    Takes start coordinate (x,y) and the label name
    """
    t.up()
    t.goto(feet(position[0]), feet(position[1]))
    t.write(name, font=('Arial', 12, 'normal'))
    t.up()
    t.home()

def permenent():
    """
    These are the pieces of the shed that are exact atm
    """
    #whole room
    rect((-15, 12.5), 30, 25)
    label((0,0), '30x25')
    #top door
    rect((-1.5, 13), 3, 1)
    #side door
    rect((14.5, 1.5), 1, 3)
    #top left windows
    rect((-10.5, 12.75), 4, 0.5)
    #bottom windows
    rect((-2, -12.25), 4, 0.5)
    #garage
    rect((-15.5, 4), 1, 8)
    #bathroom
    rect((-15, -6.5), 10, 6)
    label((-14, -7.5), 'Bathroom')
    label((-13.5, -8.5), '10x6')
    #bathroom door
    rect((-10, -6), 2.5, 1)
    #loft
    rect((5, 12.5), 10, 8)
    label((7, 10), 'Loft w/ Stairs')
    label((7.5, 9), '12x8')
    #stairs
    for stair in range(7):
        rect((3, 6+(stair)), 2, 0.5)
    #furnace
    rect((7, -7), 3, 2)

def normal_kitchen():
    """
    Configuration for normal kitchen
    """
    #back counter
    rect((-13, 12.5), 11, 2)
    #side counter
    rect((-15, 12.5), 2, 5)
    #sink
    rect((-11, 12.5), 2, 1.5)
    #fridge
    rect((-15, 7.5), 2, 2.5)
    #stove
    rect((-7, 12.5), 3, 2)

def partitioned_kitchen():
    pass
    

if __name__ == '__main__':
    t.speed("fastest")
    t.hideturtle()
    permenent()
    normal_kitchen()
    
        
