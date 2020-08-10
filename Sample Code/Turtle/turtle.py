import turtle
draw = turtle.Turtle()

def square():
    for x in range(0,4):
        draw.forward(90)
        draw.left(90)
    draw.end()

def circle():
    for x in range(0,360):
        draw.forward(2)
        draw.left(1)
    draw.end()

def triangle():
    for x in range(0,3):
        draw.forward(100)
        draw.left(120)
    draw.end()

def parallelogram():
    for x in range(0,4):
        draw.forward(100)
        draw.left(45)
        draw.forward(100)
        draw.left(135)
    draw.end()


def hexagon():
    for x in range(0,6):
        draw.forward(200)
        draw.left(60)
    draw.end()

