from turtle import Turtle, colormode, done
leo: Turtle = Turtle ()
leo.penup()
leo.goto(45,60)
leo.pendown()
leo.speed(100)
leo.hideturtle()

side_length: int = 300

i: int = 0
i_side: int = 0
colormode(255)
leo.pencolor(99,204,250)
leo.fillcolor(99,204,250)
leo.begin_fill()
while (i < 23):
    leo.forward(side_length)
    leo.left(120)
    i += 1
    side_length -= 10
leo.end_fill()


input("Press any key to exit...")