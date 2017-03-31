import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.forward(100)
    brad.speed(2)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    window.exitonclick()

draw_square()
