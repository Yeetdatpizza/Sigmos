import math

def getCoords():
    x = input("Enter an x number\n")
    y = input("Enter an y number\n")
    return x, y

def axisSetup(turtle, length_of_grid, x_line_color, y_line_color, grid_color):

    turtle.home()

    turtle.left(90)

    turtle.pencolor(y_line_color)

    turtle.forward(length_of_grid)
    turtle.back(length_of_grid * 2)
    turtle.forward(length_of_grid)

    turtle.pencolor(x_line_color)

    turtle.right(90)

    turtle.forward(length_of_grid)
    turtle.back(length_of_grid * 2)
    turtle.forward(length_of_grid)

    turtle.back(length_of_grid)

    turtle.color(grid_color)

def goToPoint(turtle, one_stud, x, y):
    turtle.penup()
    turtle.home

    turtle.forward(x * one_stud)

    if y < 0:
        turtle.right(90)
        turtle.back(y * one_stud)
    else:
        turtle.left(90)
        turtle.forward(y * one_stud)
    turtle.pendown

def plotPoint(turtle, one_stud, x, y, point_color):

    x = float(x)
    y = float(y)

    turtle.penup()
    turtle.home()
    
    turtle.forward(x * one_stud)

    if y < 0:
        turtle.right(90)
        turtle.back(y * one_stud)
    else:
        turtle.left(90)
        turtle.forward(y * one_stud)

    turtle.setheading(90)
    turtle.right(90)
    turtle.forward(one_stud / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(point_color)
    turtle.fillcolor(point_color)
    turtle.begin_fill()
    turtle.circle(one_stud / 2)
    turtle.end_fill()

def lineSetup(turtle, length_of_grid):

    amount_of_lines = 40

    for i in range(amount_of_lines):
        turtle.left(90)
        turtle.forward(length_of_grid)
        turtle.back(length_of_grid * 2)
        turtle.forward(length_of_grid)
        turtle.right(90)
        turtle.forward(length_of_grid / 20)

    turtle.home()

    turtle.left(90)

    turtle.forward(length_of_grid)

    turtle.right(180)

    for i in range(amount_of_lines):
        turtle.left(90)
        turtle.forward(length_of_grid)
        turtle.back(length_of_grid * 2)
        turtle.forward(length_of_grid)
        turtle.right(90)
        turtle.forward(length_of_grid / 20)



def getReadiblePointsFromSlopePointForm(equation, amount):

    list_of_points = []

    y_intercept = 0

    equation = equation.replace(" ", "")
    equation = equation.replace("y=", "")

    if equation[-1] != "x":

        y_intercept = equation[-1]

        y_intercept = equation[-2] + y_intercept
            
    
    y_intercept = float(y_intercept)

    slope = equation[0:equation.index("x")]
    rise = "0"
    run = "1"

    if '/' in slope:
        rise = slope[0:equation.index("/")]
        run = slope[equation.index("/") + 1:len(slope)]

        slope = float(rise) / float(run)

    else:
        rise = slope

    rise, run = float(rise), float(run)


    for i in range(amount):

        print(str(run * i),str((i * rise) + y_intercept),str(y_intercept))
        list_of_points.append(str(run * i) + "," + str((i * rise) + y_intercept) + "," + str(y_intercept))

    return list_of_points, slope

def drawLineFromSlope(turtle, slope, size, line_color, grid_color, y_int):

    turtle.penup()
    turtle.home()

    angle = math.degrees(math.atan(slope))

    if y_int < 0:
        turtle.right(90)
    else:
        turtle.left(90)

    print(angle)
    
    turtle.forward(math.fabs(y_int) * (size / 20))
    
    turtle.setheading(0)
    
    turtle.pendown()

    turtle.color(line_color)
    turtle.left(angle)
    turtle.forward(size * 2)
    turtle.backward(size * 4)
    turtle.color(grid_color)
    turtle.penup()

    turtle.home()
