import turtle

turtle.pen()
turtle.width(5)
colors = ["red", "black", "yellow", "green"]

for x in range(10):
    turtle.penup()

    turtle.goto(0, -15 * x)
    turtle.pendown()
    turtle.color(colors[x % 4])
    turtle.circle(100 + x*15)

turtle.done()
