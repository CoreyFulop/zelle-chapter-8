# regression_line.py

from graphics import *

def draw_point(x, y, win):
    point = Circle(Point(x, y), 1)
    point.setOutline("cyan")
    point.setFill("cyan")
    point.draw(win)

def main():

    # Set up window
    window_width = 1000
    window_height = 1000

    win = GraphWin("Regression Line", window_width, window_height)
    win.setCoords(-10, -10, 110, 110)
    win.setBackground("white")

    # Axes
    axis_x = Line(Point(0, 0), Point(100, 0))
    axis_x.draw(win)
    axis_y = Line(Point(0, 0), Point(0, 100))
    axis_y.draw(win)

    intro_message = Text(Point(50, 105), "Click on the data points")
    intro_message.draw(win)

    # End button
    done_rectangle = Rectangle(Point(-8, -1), Point(-2, -8))
    done_rectangle.setFill("red")
    done_rectangle.draw(win)
    
    done_message = Text(Point(-5, -4.5), "Done")
    done_message.draw(win)

    # Get data
    data = win.getMouse()
    x = data.getX()
    y = data.getY()

    x_sum = 0
    y_sum = 0
    x_squared_sum = 0
    xy_sum = 0
    
    n = 0
    
    done = False

    while not done:
        if (x <= -2) and (x >= -9) and (y <= -1) and (y >= -8):
            done = True
        else: # point is valid data
            draw_point(x, y, win)
            n += 1
            x_sum += x
            y_sum += y
            x_squared_sum += x**2
            xy_sum += x*y

            data = win.getMouse()
            x = data.getX()
            y = data.getY()

    # Regression line
    # Calculate gradient of regression line
    mean_x = x_sum/n
    mean_y = y_sum/n

    numerator = xy_sum  - n * mean_x * mean_y
    denominator = x_squared_sum - n * mean_x**2

    m = numerator/denominator

    # Draw regression line
    left_regression_y = mean_y + m * (-10 - mean_x)
    right_regression_y = mean_y + m * (110 - mean_x)

    regression_line = Line(Point(-10, left_regression_y), Point(110, right_regression_y))
    regression_line.setWidth(2)
    regression_line.draw(win)

    # Exit sequence                       
    intro_message.undraw()
    exit_message = Text(Point(50, 105), "Click to exit")
    exit_message.draw(win)

    win.getMouse()
    win.close()
    
if __name__ == "__main__":
    main()
