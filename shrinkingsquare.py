import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.right(90)
        size -= 5

i = 300
while i >= 10:
    shrinkingSquare(i)
    i-= 20
turtle.done()