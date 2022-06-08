"""
Interactive window for drawing a spring scene.
March, 2022
Author: Pedro Cruz
"""
from graphics import *
from math import sqrt
from random import *

def main():
    win = GraphWin("Trees", 800, 800)
    win.setCoords(0,0,800,800)
    sun = make_sun(win)
    ground = make_ground(win)
    instr_coords = Point(400,60)
    instr = Text(instr_coords, "Click on center of tree")
    instr.draw(win)

    while True:
        points = []
        for i in range(3):
            if i == 0:
                instr.setText("Click on center of tree")
            if i == 1:
                instr.setText("Click on edge of tree canopy")
            if i == 2:
                instr.setText("Click on base of tree trunk")

            point = win.getMouse()
            if distance(sun.getCenter(), point) <= sun.getRadius():
                quit()
            else:
                points.append(point)

        make_tree(points, win)

def make_tree(points, win):
    """
    Purpose: This function draws a tree on points determined by the user.
    Parameters: "points", a list of points that orient the position of the tree,
        and "win", a graphics window.
    Return: None.
    """
    radius = distance(points[0], points[1])

    # canopy
    canopy = Circle(points[0], radius)
    leaf_colors = ["white", "violet", "SpringGreen1", "SpringGreen2", "yellow"]
    leaf_color = choice(leaf_colors)
    canopy.setFill(leaf_color)
    canopy.setOutline(leaf_color)

    # trunk
    t = sqrt(radius)
    b = points[2].getY()
    if b > 480:
        b = 480
    upper_coords = Point((points[0].getX()-(t/2)), points[0].getY())
    lower_coords = Point((points[0].getX()+(t/2)), b)
    trunk = Rectangle(upper_coords, lower_coords)
    trunk_colors = ["brown", "snow1", "SaddleBrown", "DarkGoldenRod4", "khaki4"]
    trunk_color = choice(trunk_colors)
    trunk.setFill(trunk_color)
    trunk.setOutline(trunk_color)

    trunk.draw(win)
    canopy.draw(win)

def distance(point1, point2):
    """
    Purpose: This function returns the distance between any two points.
    Parameters: "point1" and "point2."
    Return: "distance", the distance between any two points.
    """
    p1x = point1.getX()
    p2x = point2.getX()
    p1y = point1.getY()
    p2y = point2.getY()

    distance = sqrt((p1x-p2x)**2+(p1y-p2y)**2)

    return distance

def make_ground(win):
    """
    Purpose: This function creates the creates the ground of the scenery.
    Parameters: "win", a graphics window.
    Return: "grass", the rectangular object representing the ground.
    """
    grass_coord1 = Point(0,480)
    grass_coord2 = Point(800,0)
    grass = Rectangle(grass_coord1, grass_coord2)
    grass.setFill(color_rgb(41, 163, 41))
    grass.setOutline(color_rgb(41, 163, 41))
    grass.draw(win)

    return grass

def make_sun(win):
    """
    Purpose: This function creates the sun object in the graphics window.
    Parameters: "win" (the graphics window.)
    Return: "sun" (circle object representing the sun.)
    """
    sky_coord1 = Point(0,800)
    sky_coord2 = Point(800,480)
    sky = Rectangle(sky_coord1, sky_coord2)
    sky.setFill(color_rgb(102, 224, 255))
    sky.setOutline(color_rgb(102, 224, 255))
    sky.draw(win)

    center = Point(720, 720)
    radius = 40
    sun = Circle(center, radius)
    sun.setFill("yellow")
    sun.setOutline("yellow")
    sun.draw(win)

    return sun

main()
