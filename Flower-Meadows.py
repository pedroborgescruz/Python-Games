"""""
An interactive program to make a meadow of unique flowers.
Using mouse clicks, the program allows the user to specify the location and
    height of as many flowers as they’d like. When they are done making flowers
    they can quit the program by clicking on the black border at the bottom of
    the window.

Author: Pedro Cruz
October 20th, 2021
"""""

from graphics import *

def makeGrass(window):
    """
    This function creates the lovely grass of our landscape. Parameter 'window',
    which refers to the graphics window, is required.
    """

    p1 = Point(0, 50)
    p2 = Point(100, -50)

    grass = Rectangle(p1, p2)
    grass.setFill("lawn green")
    grass.setOutline("lawn green")
    grass.draw(window)

def makeBorder(window):
    """
    This function creates the border that the user can click in order to quit
    the program. Parameter 'window', which refers to the graphics window, is
    required.
    """

    p1 = Point(0, -5)
    p2 = Point(100, 5)

    rectangle = Rectangle(p1,p2)
    rectangle.setFill("black")
    rectangle.setOutline("black")
    rectangle.draw(window)

def makeFlower(window, click1):
    """
    This function draws the flowers based on the user's clicks. Parameters
    'window', which refers to the graphics window, and 'click1', the first click
    made by the user, are required.
    """

    import random

    colors = ["red", "blue", "yellow", "pink", "purple", "green", "brown",
    "tomato", "bisque", "cyan", "slate blue", "turquoise", "hot pink"]

    # flower
    blossom = Circle(click1, 5)
    blossom.setFill(random.choice(colors))
    blossom.draw(window)

    innerCircle = Circle(click1, 2)
    innerCircle.setFill(random.choice(colors))
    innerCircle.draw(window)

    # stem
    click2 = window.getMouse()
    stem = Line(click1, click2)
    stem.setWidth(3)
    stem.draw(window)

    blossom.redraw()
    innerCircle.redraw()

    # leaves
    stemCenter = stem.getCenter()
    stemCenterX = stemCenter.getX()
    stemCenterY = stemCenter.getY()

    leftLeaf = Oval(stemCenter, Point((stemCenterX+-10), (stemCenterY+5)))
    leftLeaf.setFill("green")
    leftLeaf.draw(window)

    rightLeaf = Oval(Point(stemCenterX, stemCenterY-5), Point((stemCenterX+10),
    (stemCenterY)))
    rightLeaf.setFill("green")
    rightLeaf.draw(window)

def main():
    """
    Here, we are just putting the building blocks together. No parameters
    required for main.
    """

    # creating the graphics window and setting the basics
    win = GraphWin("Meadow of Flowers", 800, 800)
    win.setBackground("lightblue")
    win.setCoords(0, 0, 100, 100)
    makeGrass(win)
    makeBorder(win)

    # setting when the program should quit + running makeFlower function
    click = win.getMouse()
    height = click.getY()

    while height > 5:
        makeFlower(win,click)
        click = win.getMouse()
        height = click.getY()

    win.close()

main()
