
import math

# Speed the turtle moves, 0 is fastest
sigma_speed = 0

# Color of the lines on the grid
grid_color = "gray50"

# Color of the y-axis
y_line_color = "green4"

# Color of the x-axis
x_line_color = "red"

# Random colors a line plotted can be
line_colors = ["blue", "black", "purple", "orange", "red", "cyan", "magenta", "gold"]

# Color of points plotted
point_color = "black"

# SIze of the grid, 1 is smallest.
length_of_grid = 2

# Enable Debug Mode
debug_mode = True

#Baisc math for the grid, wouldn't touch this if I were you

amount_of_lines = int(math.pow(length_of_grid, 2) * 10)

one_stud = .1 / (length_of_grid / 2)

sigma_line_width = (math.ceil(int(one_stud / 5)) + 1) * 3
