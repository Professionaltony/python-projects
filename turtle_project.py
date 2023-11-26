import turtle
turtle.bgcolor("black")
turtle.pensize(2.5)
turtle.speed(0.5)
color = ["red", "green", "white", "gold"]
for x in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(150)
        turtle.left(10)

turtle.mainloop()
