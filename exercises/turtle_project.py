"""TODO: Describe your scene program."""

__author__ = "730651254"

from turtle import Turtle, colormode, done


def draw_U(U: Turtle, x: float, y: float) -> None:
    """U."""
    colormode(255)
    U.speed(100)
    U.pencolor("blue")
    U.fillcolor("blue")
    U.penup()
    U.goto(x, y)
    U.pendown()
    U.hideturtle()
    U.begin_fill()
    U.setheading(270)
    U.forward(250)
    U.left(90)
    U.forward(150)
    U.left(90)
    U.forward(250)
    U.left(90)
    U.forward(30)
    U.left(90)
    U.forward(220)
    U.right(90)
    U.forward(90)
    U.right(90)
    U.forward(220)
    U.left(90)
    U.forward(30)
    U.end_fill()


def draw_N(N: Turtle, x: float, y: float) -> None:
    """N."""
    N.hideturtle()
    N.speed(100)
    colormode(255)
    N.pencolor("blue")
    N.fillcolor("blue")
    N.begin_fill()
    N.penup()
    N.goto(-200, 300)
    N.pendown()
    N.setheading(270)
    N.forward(250)
    N.left(90)
    N.forward(30)
    N.left(90)
    N.forward(220)
    N.right(150)
    N.forward(254)
    N.left(60)
    N.forward(30)
    N.left(90)
    N.forward(250)
    N.left(90)
    N.forward(30)
    N.left(90)
    N.forward(220)
    N.right(150)
    N.forward(254)
    N.left(60)
    N.forward(30)
    N.end_fill()


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
    i: int = 0
    while i < 3:
        C.forward(250)
        C.left(90)
        i += 1
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


def draw_c(c: Turtle, x: float, y: float, z: int) -> None:
    """Draw c."""
    c.penup()
    c.speed(100)
    c.goto(x, y)
    c.pendown()
    c.hideturtle()
    colormode(255)
    c.pencolor("blue")
    c.setheading(180)
    c.pensize(z)
    i: int = 0
    while i < 3:
        c.forward(100)
        c.left(90)
        i += 1


def draw_o(o: Turtle, x: float, y: float, z: int) -> None:
    """Draw o."""
    o.penup()
    o.speed(100)
    o.goto(x, y)
    o.pendown()
    o.pensize(z)
    o.hideturtle()
    colormode(255)
    o.pencolor("blue")
    o.setheading(270)
    i: int = 0
    while i < 4:
        o.forward(100)
        o.left(90)
        i += 1


def draw_m(m: Turtle, x: float, y: float, z: int) -> None:
    """Draw m."""
    m.penup()
    m.speed(100)
    m.goto(x, y)
    m.pendown()
    m.pensize(z)
    m.hideturtle()
    colormode(255)
    m.pencolor("blue")
    m.setheading(90)
    i: int = 0
    while i < 2:
        m.forward(100)
        m.right(90)
        m.forward(100)
        m.right(90)
        m.forward(100)
        m.setheading(450)
        i += 1


def draw_p(p: Turtle, x: float, y: float, z: int) -> None:
    """Draw p."""
    p.penup()
    p.speed(100)
    p.goto(x, y)
    p.pendown()
    p.pensize(z)
    p.hideturtle()
    colormode(255)
    p.pencolor("blue")
    p.setheading(90)
    p.forward(200)
    i: int = 0
    while i < 3:
        p.right(90)
        p.forward(100)
        i += 1


def draw_1(one: Turtle, x: float, y: float, z: int) -> None:
    """Draw 1 for twice."""
    one.penup()
    one.speed(100)
    one.goto(x, y)
    one.pendown()
    one.hideturtle()
    colormode(255)
    one.pencolor("blue")
    one.pensize(z)
    one.setheading(270)
    one.forward(200)


def draw_0(zero: Turtle, x: float, y: float, z: int) -> None:
    """Draw 0."""
    zero.penup()
    zero.speed(100)
    zero.goto(x, y)
    zero.pendown()
    zero.hideturtle()
    zero.pensize(z)
    zero.setheading(180)
    colormode(255)
    zero.pencolor("blue")
    i: int = 0
    while i < 2:
        zero.forward(100)
        zero.right(90)
        zero.forward(200)
        zero.right(90)
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    UNC: Turtle = Turtle()
    draw_U(UNC, -450, 300)
    draw_N(UNC, -200, 300)
    draw_C(UNC, 365, 300)
    draw_c(UNC, -550, -150, 30)
    draw_o(UNC, -450, -150, 30)
    draw_m(UNC, -250, -250, 30)
    draw_p(UNC, 50, -350, 30)
    draw_1(UNC, 350, -50, 30)
    draw_1(UNC, 450, -50, 30)
    draw_0(UNC, 650, -250, 30)


main()


input("type any key to exit...")