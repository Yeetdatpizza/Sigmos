import math
import Modules
import Objects
import Settings

Objects.root.title("Sigmos")

Objects.root.attributes("-fullscreen", True)

Objects.screen.setworldcoordinates(-Settings.length_of_grid, -Settings.length_of_grid, Settings.length_of_grid,
                                   Settings.length_of_grid)

value = Objects.Alpha.StringVar(Objects.root, "y = ")

equation = Objects.Alpha.StringVar(Objects.root)

menu = Objects.Alpha.OptionMenu(Objects.root, value, "y = ", "x = ", "NA")
menu.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

field = Objects.Alpha.Entry(Objects.root, textvariable=equation)
field.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)


def axisSetup(Sigma, length_of_grid, x_line_color, y_line_color, grid_color):
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


def lineSetup(Sigma, length_of_grid):
    for i in range(Settings.amount_of_lines):
        Sigma.left(90)
        Sigma.forward(length_of_grid)
        Sigma.back(length_of_grid * 2)
        Sigma.forward(length_of_grid)
        Sigma.right(90)
        Sigma.forward(Settings.one_stud)

    Sigma.left(90)
    Sigma.forward(length_of_grid)
    Sigma.back(length_of_grid * 2)

    Sigma.penup()
    Sigma.home()
    Sigma.pendown()
    Sigma.left(90)
    Sigma.forward(length_of_grid)
    Sigma.right(180)

    for i in range(Settings.amount_of_lines):
        Sigma.left(90)
        Sigma.forward(length_of_grid)
        Sigma.back(length_of_grid * 2)
        Sigma.forward(length_of_grid)
        Sigma.right(90)
        Sigma.forward(Settings.one_stud)

    Sigma.left(90)
    Sigma.forward(length_of_grid)
    Sigma.back(length_of_grid * 2)

    Sigma.penup()
    Sigma.home()
    Sigma.pendown()


def startScreen(isReseting = True):
    if not Objects.isEnslaved:

        Sigma = Objects.Sigma

        Sigma.clear()

        print(67)

        Objects.isEnslaved = True

        Sigma.penup()
        Sigma.home()
        Sigma.speed(Settings.sigma_speed)

        Sigma.back(Settings.one_stud / 2)
        Sigma.right(90)
        Sigma.pendown()
        Sigma.circle(Settings.one_stud / 2)

        axisSetup(Sigma, Settings.length_of_grid, Settings.x_line_color, Settings.y_line_color, Settings.grid_color)
        lineSetup(Sigma, Settings.length_of_grid)
        axisSetup(Sigma, Settings.length_of_grid, Settings.x_line_color, Settings.y_line_color, Settings.grid_color)

        Sigma.penup()
        Sigma.home()
        Objects.current_position = [0, 0]
        Sigma.pendown()

        if not isReseting:
            for maths in Objects.list_of_equations:
                print(maths)
                Modules.plotPointsFromEquation(maths[1], maths[0], True)

        Objects.isEnslaved = False

        Sigma.penup()
        if isReseting:
            Objects.list_of_equations = []
        Objects.current_position = [0, 0]
        Sigma.home()
        Sigma.pendown()


def friendlyListener():
    Modules.plotPointsFromEquation(equation.get(), value.get())


def sizeIncrease():
    if Objects.isEnslaved:
        return

    Settings.length_of_grid += 1
    Settings.amount_of_lines = int(math.pow(Settings.length_of_grid, 2) * 10)
    Settings.one_stud = .1 / (Settings.length_of_grid / 2)
    Settings.sigma_line_width = int(Settings.one_stud / 10)

    startScreen(False)


def sizeDecrease():
    if Objects.isEnslaved or Settings.length_of_grid == 1:
        return

    Settings.length_of_grid -= 1
    Settings.amount_of_lines = int(math.pow(Settings.length_of_grid, 2) * 10)
    Settings.one_stud = .1 / (Settings.length_of_grid / 2)
    Settings.sigma_line_width = int(Settings.one_stud / 10)

    startScreen(False)


plot_button = Objects.Alpha.Button(Objects.root, text = "Plot!", command = friendlyListener)
plot_button.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

clear_button = Objects.Alpha.Button(Objects.root, text = "Clear!", command = startScreen)
clear_button.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

size_increase_button = Objects.Alpha.Button(Objects.root, text = "Increase Size!", command = sizeIncrease)
size_increase_button.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

size_decrease_button = Objects.Alpha.Button(Objects.root, text = "Decrease Size!", command = sizeDecrease)
size_decrease_button.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

errorText = Objects.Alpha.Label(Objects.root, text = "This is where I will put your mistakes.")
errorText.pack(side = Objects.Alpha.LEFT, padx = 10, pady = 10)

Objects.errorText = errorText


def resize():
    Objects.screen.setworldcoordinates(-Settings.length_of_grid, -Settings.length_of_grid, Settings.length_of_grid, Settings.length_of_grid)