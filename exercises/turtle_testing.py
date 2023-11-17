from turtle import Turtle, colormode, done
def draw_C(C: Turtle, x: float, y: float) -> None:
    """C."""
    C.hideturtle()
    C.speed(100)
    C.penup()
    C.goto(x, y)
    C.pendown()
    colormode(255)
    C.pencolor("blue")
    C.fillcolor("blue")
    C.begin_fill()
    for i in C:
        C.forward(250)
        C.left(90)
        
    C.forward(30)
    C.left(90)
    C.forward(220)
    C.right(90)
    C.forward(190)
    C.right(90)
    C.forward(220)
    C.left(90)
    C.forward(30)
    C.left(90)
    C.forward(250)
    C.end_fill()

def main() -> None:
    UNC: Turtle = Turtle()
    draw_C(UNC, 0, 0)

main()

input("Type any key to exit...")