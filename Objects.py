import tkinter as Alpha
from tkinter import BOTTOM
from turtle import TurtleScreen, RawTurtle

root = Alpha.Tk()
root.title("Sigmos")

screen_height = root.winfo_screenheight()

canvas = Alpha.Canvas(root, width = screen_height, height = screen_height - int(screen_height / 10), bg = "white")
canvas.pack(side = Alpha.BOTTOM)

# Create a TurtleScreen around the canvas and a RawTurtle that draws on it
screen = TurtleScreen(canvas)
Sigma = RawTurtle(screen)

# Track current drawing color index
current_color = 0

# Bool for checking if the turtle is currently moving
isEnslaved = False

# List Of Equations
list_of_equations = []

# Current Position Of The Turtle
current_position = [0, 0]

# Error message box.
errorText = Alpha.Label(root, text = "Not even real, overwritten by ScreenSetup.py")