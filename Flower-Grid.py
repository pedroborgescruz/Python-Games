"""
Flower grid generator.
March, 2022
Author: Pedro Cruz
"""
from graphics import *

def main():
    n = int(input("Enter number of white flowers across: "))

    win = GraphWin("Grid of Flowers", 500, 500)
    win.setCoords(0,0,1,1)
    win.setBackground(color_rgb(128, 255, 170))

    draw_flower(win, n, n)

    win.getMouse()

def draw_flower(win, row, col):
    """
    Purpose: This function draws a flower in a specific position in the grid.
    Parameters: "win" (graphics window), "row" (number of rows in the grid), and
        "col" (number of columns in the grid).
    Return: None.
    """
    for i in range(row):
        for j in range(col):
            flower = make_flower(row)
            dx = flower[4].getCenter().getX()*2 ## dx based on the flower stigma
            dy = flower[4].getCenter().getY()*2 ## dy based on the flower stigma
            for k in range(len(flower)): ## drawing the flower
                flower[k].move(dx*j,dy*i)
                flower[k].draw(win)

def make_flower(x):
    """
    Purpose: This function creates a list of objects composing the flower.
    Parameters: "x" (a correction factor that takes care of the proportion of
        the flower in relation to the grid.)
    Return: "flower_parts" (a list of circle objects that composes the flower.)
    """
    flower_parts = []

    ## stigma
    stigma_coords = Point(0.5/x, 0.5/x)
    stigma = Circle(stigma_coords, 0.1/x)
    stigma.setFill(color_rgb(255, 255, 102))
    stigma.setOutline(color_rgb(255, 255, 102))

    ## petal 1
    petal1_coords = Point((stigma_coords.getX() + 0.15/x), (stigma_coords.getY()
        + 0.15/x))
    petal1 = Circle(petal1_coords, 0.2/x)
    petal1.setFill("white")
    petal1.setOutline("white")

    ## petal 2
    petal2 = petal1.clone()
    petal2.move(0,-0.3/x)
    petal2.setFill("pink")
    petal2.setOutline("pink")

    ## petal 3
    petal3 = petal1.clone()
    petal3.move(-0.3/x,0)
    petal3.setFill("pink")
    petal3.setOutline("pink")

    ## petal 4
    petal4 = petal2.clone()
    petal4.move(-0.3/x,0)
    petal4.setFill("white")
    petal4.setOutline("white")

    flower_parts.append(petal1)
    flower_parts.append(petal4)
    flower_parts.append(petal3)
    flower_parts.append(petal2)
    flower_parts.append(stigma)

    return flower_parts

main()
