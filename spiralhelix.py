import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("black")

turtle_colors = ["blue","red","yellow","orange","light blue","white","brown"]

for i in range(10):
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.right(i*2)
    turtle_instance.color(turtle_colors[i % 7])

turtle.mainloop()
#turtle.done() = turtle.mainloop() ikisi de aynı işlevi görür.