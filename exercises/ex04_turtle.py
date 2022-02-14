"""Open Ocean: Two Sail Boats in the open ocean, with a sun."""

__author__ = "730484603"

from turtle import Turtle, colormode, done, tracer, update


def sailboat_sail(a_sail: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws the sails of a sail boat."""
    ertle: Turtle = Turtle()
    colormode(255)
    a_sail.penup()
    a_sail.goto(x, y)
    a_sail.setheading(0.0)
    a_sail.pendown()
    i: int = 0
    a_sail.color(194, 196, 194)
    a_sail.begin_fill()
    while i < 2:
        a_sail.forward(width)
        a_sail.left(80)
        a_sail.forward(length)
        a_sail.left(100)
        i += 1
    a_sail.end_fill()
    inner_sail_design_one(ertle, x, y, 100)
    inner_sail_design_two(ertle, x, y, 100)
    a_sail.hideturtle()


def inner_sail_design_one(triangle: Turtle, x: float, y: float, sidelength: float) -> None:
    """Inner design one of the sails on the sail boat."""
    i: int = 0
    colormode(255)
    triangle.penup()
    triangle.goto(x + 30, y)
    triangle.setheading(0.0)
    triangle.pendown()
    triangle.color(155, 27, 19)
    triangle.begin_fill()
    while i < 3:
        triangle.forward(sidelength)
        triangle.left(120)
        sidelength *= .96
        i += 1
    triangle.hideturtle()


def inner_sail_design_two(triangle: Turtle, x: float, y: float, sidelength: float) -> None:
    """Inner design two of the sails on the sail boat."""
    triangle.end_fill()
    triangle.penup()
    triangle.goto(x + 30, y)
    triangle.setheading(0.0)
    triangle.pendown()
    triangle.color(110, 38, 80)
    i = 0
    triangle.begin_fill()
    while i < 8:
        sidelength *= 0.75
        triangle.forward(sidelength)
        triangle.left(120)
        i += 1
    triangle.end_fill()
    triangle.hideturtle()


def sailboat_base(a_base: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws the base of the sail boat."""
    colormode(255)
    a_base.penup()
    a_base.goto(x, y)
    a_base.setheading(0.0)
    a_base.pendown()
    i: int = 0
    a_base.color(108, 58, 2)
    a_base.begin_fill()
    while i < 2:
        a_base.forward(width)
        a_base.left(129)
        a_base.forward(length)
        a_base.left(51)
        width *= 2
        i += 1
    a_base.end_fill()
    a_base.hideturtle()


def sailboat_mast(a_mast: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws the mast of the sail boat."""
    colormode(255)
    a_mast.penup()
    a_mast.goto(x, y)
    a_mast.setheading(0.0)
    a_mast.pendown()
    i: int = 0
    a_mast.color(173, 94, 3)
    a_mast.begin_fill()
    while i < 2:
        a_mast.forward(width)
        a_mast.left(90)
        a_mast.forward(length)
        a_mast.left(90)
        i += 1
    a_mast.end_fill()
    a_mast.hideturtle()


def sun(a_sun: Turtle, x: float, y: float, radius: float, extent: float) -> None:
    """Draws the sun overlooking the open ocean."""
    colormode(255)
    a_sun.penup()
    a_sun.goto(x, y)
    a_sun.setheading(0.0)
    a_sun.pendown()
    a_sun.color(226, 245, 7)
    a_sun.begin_fill()
    a_sun.circle(radius, extent)
    a_sun.end_fill()
    a_sun.hideturtle()


def birds(a_birds: Turtle, x: float, y: float, length_one: float, length_two: float) -> None:
    """Draws the birds flying above the open ocean."""
    colormode(255)
    a_birds.penup()
    a_birds.goto(x, y)
    a_birds.setheading(0.0)
    a_birds.pendown()
    i: int = 0
    a_birds.pensize(5)
    a_birds.pencolor("white")
    while i < 2:
        a_birds.right(75)
        a_birds.forward(length_two)
        a_birds.left(75)
        a_birds.forward(length_one)
        i += 1
    i = 0 
    while i < 2:
        a_birds.forward(length_one)
        a_birds.left(75)
        a_birds.forward(length_two)
        a_birds.right(75)
        i += 1
    a_birds.hideturtle()


def background(a_background: Turtle) -> None:
    """Changes the background to dark blue to mimic the ocean."""
    a_background.screen.bgcolor("dark blue")


def waves(a_waves: Turtle, x: float, y: float, length: float) -> None:
    """Draws waves in the open ocean."""
    colormode(255)
    a_waves.penup()
    a_waves.goto(x, y)
    a_waves.setheading(0.0)
    a_waves.pendown()
    i: int = 0
    a_waves.pensize(10)
    a_waves.pencolor("light blue")
    while i < 30:
        a_waves.forward(length)
        a_waves.right(75)
        a_waves.forward(length)
        a_waves.left(75)
        a_waves.forward(length)
        i += 1
    i = 0 
    a_waves.hideturtle()


def bird_lines() -> None:
    """Creates lines of bird drawings across differnt points in the scene."""
    ertle: Turtle = Turtle()
    i: int = 0
    c: float = -320
    d: float = 200
    while i < 10:
        birds(ertle, c, d, 5, 20)
        c += 80
        d += 10
        i += 1
    i = 0
    e: float = -320
    f: float = 50
    while i < 10:
        birds(ertle, e, f, 5, 20)
        e += 80
        f += 10
        i += 1
    i = 0
    g: float = -320
    h: float = -265
    while i < 10:
        birds(ertle, g, h, 5, 20)
        g += 80
        h += 10
        i += 1
    i = 0
    j: float = -320
    k: float = -100
    while i < 10:
        birds(ertle, j, k, 5, 20)
        j += 80
        k += 10
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    ertle: Turtle = Turtle()
    background(ertle)
    i: int = 0
    a: float = -600
    b: float = -200
    while i < 11:
        waves(ertle, a, b, 10)
        a += 60
        b += 60
        i += 1
    sun(ertle, -250, 170, 80, 360)
    sailboat_base(ertle, -175, -175, 70, 120)
    sailboat_base(ertle, 100, 60, 60, 100)
    sailboat_mast(ertle, -235, -125, 30, 100)
    sailboat_mast(ertle, 60, 100, 25, 90)
    sailboat_sail(ertle, -300, -85, 160, 100)
    sailboat_sail(ertle, -5, 145, 145, 90)
    bird_lines()
    update()
    done()


if __name__ == "__main__":
    main()