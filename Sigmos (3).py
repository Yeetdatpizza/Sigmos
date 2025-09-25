import turtle
import math
from turtle import Screen
from Modules import *

mango = turtle.Screen()
mango.title("Sigmos")

def plotPointsFromPointList(list_of_points, slope):
    x = 0
    y = 0
    inter = 0

    for point in list_of_points:

        point = point.split(',')

        x = point[0]
        y = point[1]
        inter = float(point[2])

        if math.floor(float(x)) != float(x) or math.floor(float(y)) != float(y):
            continue

        else:
            plotPoint(turtle, one_stud, x, y, point_color)
            plotPoint(turtle, one_stud, str(float(x) * -1), str((float(y) * -1) + (inter * 2)), point_color)

    drawLineFromSlope(turtle, slope, length_of_grid, line_color, grid_color, inter)

grid_color = "black"
y_line_color = "green"
x_line_color = "red"
line_color = "blue"
point_color = "purple"

length_of_grid = 300

one_stud = length_of_grid / 20

# Create 0, 0
turtle.speed(100)
turtle.penup()
turtle.back(one_stud / 2)
turtle.right(90)
turtle.pendown()
turtle.circle(one_stud / 2)

axisSetup(turtle, length_of_grid, x_line_color, y_line_color, grid_color)

lineSetup(turtle, length_of_grid)

axisSetup(turtle, length_of_grid, x_line_color, y_line_color, grid_color)

while True:

    action = input("What would you like to do?\n\n1 - Plot a point.\n\n2 - Plot a line.\n\n")

    if int(action) == None:
        print("Invalid action!")
        continue

    if action == "1":
        cords = getCoords()
        plotPoint(turtle, one_stud, cords[0], cords[1], point_color) 

    elif action == "2":

        mathfr = input("Enter an equation in y-intercept form (y = mx + b)\n")

        amount = int(input("How many points should be plotted?\n"))

        mathfr, slope = getReadiblePointsFromSlopePointForm(mathfr, amount)[0], getReadiblePointsFromSlopePointForm(mathfr, amount)[1]

        plotPointsFromPointList(mathfr, float(slope))

Screen().mainloop()