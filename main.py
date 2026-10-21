import turtle

drawing_table = turtle.Screen()
drawing_table.bgcolor("green")
drawing_table.title("Python Turtle")
turtle_instance = turtle.Turtle()

#square

turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.right(90)
turtle_instance.forward(100)
turtle_instance.begin_poly()
turtle.done()