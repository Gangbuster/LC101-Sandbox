import turtle


def draw_line(length, angle):
    mike = turtle.Turtle()
    mike.left(angle)
    mike.forward(length / 2)
    mike.forward(-length)
    mike.left(90)
    mike.forward(length / 2)
    mike.forward(-length)
    mike.right(90)
    mike.forward(length / 2)
    mike.left(90)
    mike.forward(length)
    mike.left(90)
    mike.forward(length / 2)
    mike.forward(-length)
    mike.left(90)
    mike.forward(length)
    mike.right(90)
    mike.forward(length / 2)


def square(lines):
    for angle in range(0, 180, int(180 / lines)):
        draw_line(200, angle)


square(10)
