import turtle

turtle.pen()
turtle.width = 3


for x in range(21):
    turtle.penup()
    turtle.goto(-200, 200 - 20 * x)
    turtle.pendown()
    turtle.goto(200, 200 - 20 * x)

for y in range(21):
    turtle.penup()
    turtle.goto(-200 + 20 * y, 200)
    turtle.pendown()
    turtle.goto(-200 + y * 20, -200)

turtle.done()
