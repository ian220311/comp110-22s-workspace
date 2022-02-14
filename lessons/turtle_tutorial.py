from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -75)
leo.pendown()

leo.speed(50)
leo.hideturtle()

leo.color(51, 220, 255)

i: int = 0
leo.begin_fill()
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-150, -75)
bob.pendown()

bob.speed(90)
bob.hideturtle()

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i += 1

side_length = 300
bob.color(0, 0, 0)

i: int = 0
bob.begin_fill()
while (i < 6):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.95
    i += 1
bob.end_fill()
done()

def inner_sail_design(triangle: Turtle, triangle_two: Turtle, sidelength: float) -> None:
    """Inner design of the sails on the sail boat."""
    ertle: Turtle = Turtle()
    i: int = 0
    triangle.color(215, 8, 66)
    triangle.begin_fill()
    while i < 3:
       triangle.forward(sidelength)
       triangle.left(120)
       sidelength *= .96
       i += 1
    triangle.end_fill()
    triangle_two.color(215, 8, 131)
    i = 0
    triangle_two.begin_fill()
    while i < 8:
        sidelength *= .96
        triangle_two.forward(sidelength)
        triangle_two.left(120)
        i += 1
    triangle_two.end_fill()

    sailboat_base(ertle, 50, 50, 220, 200)
    sailboat_base(ertle, 50, 50, 220, 200)
    sailboat_mast(ertle, 50, 50, 100, 100)
    sailboat_mast(ertle, 50, 50, 100, 100)
    sailboat_sail(ertle, 50, 100, 220, 200)
    sailboat_sail(ertle, 50, 100, 220, 200)