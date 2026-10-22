import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.speed(10)

def shrinkingSquare(road):
    for i in range(4):
        turtle_instance.forward(road)
        turtle_instance.right(90)
        road -= 5

def makeShrinkingSquare(size):
    while size >= 10:
        shrinkingSquare(size)
        size-= 20

makeShrinkingSquare(300)
turtle.done()