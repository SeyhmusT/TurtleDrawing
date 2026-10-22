import turtle

drawing_table = turtle.Screen()
drawing_table.bgcolor("green")
drawing_table.title("Python Turtle")
turtle_instance = turtle.Turtle()

#star

for i in range(5):
    turtle_instance.right(144)
    turtle_instance.forward(300)
turtle.done()