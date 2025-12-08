import math
from re import error
from turtle import pendown
import Settings
import Objects


def formatEquation(equation, i, letter, x, y):
    prev_is_alnum = i > 0 and equation[i - 1].isalnum()
    next_is_alnum = i < len(equation) - 1 and equation[i + 1].isalnum()

    if prev_is_alnum and next_is_alnum:
        equation = equation[:i] + "*(" + str(x) + ")*" + equation[i + 1:]
        i += len("*(%s)*" % x) - 1

    elif next_is_alnum:
        equation = equation[:i] + "(" + str(x) + ")*" + equation[i + 1:]
        i += len("(%s)*" % x) - 1

    elif prev_is_alnum:
        equation = equation[:i] + "*(" + str(x) + ")" + equation[i + 1:]
        i += len("*(%s)" % x) - 1

    else:
        equation = equation[:i] + "(" + str(x) + ")" + equation[i + 1:]
        i += len("(%s)" % x) - 1

    return equation


def formatToPython(equation):
    equation = equation.replace("^", "**")
    equation = equation.replace("e", "math.e")
    equation = equation.replace("pi", "math.pi")
    equation = equation.replace("sin", "math.sin")
    equation = equation.replace("cos", "math.cos")
    equation = equation.replace("tan", "math.tan")
    equation = equation.replace("asin", "math.asin")
    equation = equation.replace("acos", "math.acos")
    equation = equation.replace("atan", "math.atan")
    equation = equation.replace("log", "math.log")
    equation = equation.replace("ln", "math.log")
    equation = equation.replace("sqrt", "math.sqrt")
    equation = equation.replace("abs", "math.abs")
    equation = equation.replace("ceil", "math.ceil")
    equation = equation.replace("floor", "math.floor")
    equation = equation.replace("round", "math.round")
    equation = equation.replace("factorial", "math.factorial")
    equation = equation.replace("gcd", "math.gcd")
    equation = equation.replace("lcm", "math.lcm")

    return equation


def doMath(equation, x=None, y=None):
    equation = formatToPython(equation)

    if x or x == 0:

        i = 0

        while i < len(equation):

            letter = equation[i]

            if letter.lower() == "x":

                equation = formatEquation(equation, i, letter, x, y)

            else:
                i += 1

    if y or y == 0:

        i = 0

        while i < len(equation):

            letter = equation[i]
            if letter.lower() == "y":

                equation = formatEquation(equation, i, letter, x, y)

            else:

                i += 1

    result = "Unmathematical"

    try:
        result = eval(equation)

    except Exception as e:

        Objects.errorText.config(text=str(e))

        if Settings.debug_mode:
            print("Math eval error:", e)

    return result


def doTrigeometry(equation):
    equation = formatToPython(equation)

    points = equation.split(",")

    if len(points) % 2 == 1 or len(points) < 3:
        Objects.errorText.config(text="Not how shapes work bro...")
        return

    point_to_add = []
    new_list_of_points = []

    count = 1

    for i in range(len(points)):
        points[i] = str(points[i].strip())
        points[i] = str(points[i].replace("(", ""))
        points[i] = str(points[i].replace(")", ""))

        point_to_add.append(int(points[i]))

        if count % 2 == 0:
            new_list_of_points.append(point_to_add)
            point_to_add = []

        count += 1

    if Settings.debug_mode:
        print("Trigeometry Equation:", equation)
        print("Trigeometry Points:", new_list_of_points)
        print("Trigeometry Points Count:", len(new_list_of_points))

    for point in range(len(new_list_of_points)):
        x = eval(str(new_list_of_points[point][0]))
        y = eval(str(new_list_of_points[point][1]))

        print(x, y)

        if x == "Unmathematical" or y == "Unmathematical":
            Objects.errorText.config(text="Not how shapes work bro...")
            return

        plotPoint(x, y, drag=True)


def axisSetup(Sigma, length_of_grid, x_line_color, y_line_color, grid_color):
    Sigma.turtlesize(5, 5)
    Sigma.home()
    Sigma.left(90)
    Sigma.pencolor(y_line_color)
    Sigma.forward(length_of_grid)
    Sigma.back(length_of_grid * 2)
    Sigma.forward(length_of_grid)
    Sigma.pencolor(x_line_color)
    Sigma.right(90)
    Sigma.forward(length_of_grid)
    Sigma.back(length_of_grid * 2)
    Sigma.forward(length_of_grid)
    Sigma.back(length_of_grid)
    Sigma.color(grid_color)
    Sigma.turtlesize(1, 1)


def goToPoint(Sigma, one_stud, x, y):
    Sigma.penup()
    Sigma.home()
    Sigma.forward(x * one_stud)

    if y < 0:
        Sigma.right(90)
        Sigma.back(y * one_stud)

    else:
        Sigma.left(90)
        Sigma.forward(y * one_stud)

    Sigma.pendown()


def plotPoint(x, y, drag=False):
    Sigma = Objects.Sigma

    currentX, currentY = Objects.current_position

    if drag:
        Sigma.pendown()

    x = float(x)
    y = float(y)

    dx = x - currentX
    dy = y - currentY

    heading = math.degrees(math.atan2(dy, dx))

    distance = math.hypot(dx, dy)

    if Settings.debug_mode:
        print(f"Current Cords: {currentX, currentX}")
        print(f"Goal Cords: {x, y}")
        print(f"Differences: {dx, dy}")
        print(f"Angle: {heading}")
        print(f"Distance: {distance}")

    Sigma.setheading(heading)

    Sigma.forward(distance * Settings.one_stud)

    Objects.current_position = [x, y]
    """

    if x <= 0: Sigma.setheading(180)
    else: Sigma.setheading(0)

    Sigma.forward(Settings.one_stud / 2)

    if x <= 0: Sigma.setheading(0)
    else: Sigma.setheading(180)

    Sigma.forward(Settings.one_stud / 2)

    if x <= 0: Sigma.setheading(270)
    else: Sigma.setheading(90)

    Sigma.forward(Settings.one_stud / 4)

    if x <= 0: Sigma.setheading(180)
    else: Sigma.setheading(0)

    Sigma.pendown()

    Sigma.pencolor(Settings.point_color)
    Sigma.fillcolor(Settings.point_color)
    Sigma.begin_fill()
    Sigma.circle(Settings.one_stud / 4)
    Sigma.end_fill()

    """

    if drag:
        Sigma.penup()


def plotPointsFromEquation(equation, prefix, actuallyBeSmart=False):
    if prefix.strip() == "Shape":
        doTrigeometry(equation)
        return

    if equation in Objects.list_of_equations:
        return

    if not actuallyBeSmart:
        Objects.list_of_equations.append([prefix, equation])

    Objects.Sigma.pensize(Settings.sigma_line_width)
    Objects.Sigma.width(Settings.sigma_line_width)

    list_of_points = []

    Objects.Sigma.color(Settings.line_colors[Objects.current_color])

    if Objects.current_color < len(Settings.line_colors) - 1:
        Objects.current_color += 1
    else:
        Objects.current_color = 0

    if prefix.strip() == "y =":
        for i in range(int(-Settings.amount_of_lines / 2),
                       int((Settings.amount_of_lines / 2) + 1)):

            points = [i, doMath(equation, i)]

            if points[1] == "Unmathematical":
                continue

            print(points[1])

            if points[1] > Settings.amount_of_lines or points[1] < -Settings.amount_of_lines:
                continue

            list_of_points.append(points)

    elif prefix.strip() == "x =":
        for i in range(int(-Settings.amount_of_lines / 2),
                       int((Settings.amount_of_lines / 2) + 1)):

            points = [doMath(equation, None, i), i]

            print(points)

            if points[0] == "Unmathematical":
                continue

            if points[0] > Settings.amount_of_lines or points[
                0] < -Settings.amount_of_lines:
                continue

            list_of_points.append(points)

    else:
        print(prefix.strip())

    isFirst = True

    for point in list_of_points:

        if isFirst:
            Objects.Sigma.penup()
        else:
            Objects.Sigma.pendown()

        if point[0] == "Unmathematical" or point[1] == "Unmathematical":
            continue

        plotPoint(point[0], point[1])

        isFirst = False

    Objects.Sigma.pensize(1)
    Objects.Sigma.width(1)