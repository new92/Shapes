import turtle
from turtle import * 
name=input("Please insert your name: ")
print("Hello "+str(name)+" and welcome to the Shares program. In this program you insert the shape you want to draw and the program draws it.")
shapes = ["star", "sun", "square", "hexagon", "triangle"] 
for s in shapes:
          print (s)
choice=input("Please type the shape and hit enter for the program to draw: ")
"star" == "star"
"sun" == "sun"
"square" == "square"
"hexagon" == "hexagon"
"triangle" == "triangle"
if "sta" == "star":
    from turtle import * 
    ws = turtle.Screen()
    geekyTurtle = turtle.Turtle()
    for i in range(5):
        geekyTurtle.forward(100)
        geekyTurtle.right(144)

elif "su" == "sun":
    color("red","yellow")
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

elif "square" == "square":
    import turtle
    def form_sq(side):
        for i in range(4):
            my_pen.fd(side)
            my_pen.left(90)
            side -= 5
    tut = turtle.Screen()
    tut.bgcolor("green")
    tut.title("Turtle")

    my_pen = turtle.Turtle()
    my_pen.color("orange")

    tut = turtle.Screen()

    side = 200

    for i in range(10):
        form_sq(side)
        side -= 20

elif "hexagon" == "hexagon":
    import turtle
    def form_hex(side):
        for i in range(6):
            my_pen.fd(side)
            my_pen.left(300)
            side -= 2

    tut = turtle.Screen()
    tut.bgcolor("green")
    tut.title("Turtle")

    my_pen = turtle.Turtle()
    my_pen.color("orange")

    tut = turtle.Screen() 

    side = 120
    for i in range(5):
        form_hex(side)
        side -= 12

elif "triangle" == "triangle":
    def form_tri(side):
        for i in range(3):
            my_pen.fd(side)
            my_pen.left(120)
            side -= 10

    tut = turtle.Screen()
    tut.bgcolor("green")
    tut.title("Turtle")

    my_pen = turtle.Turtle()
    my_pen.color("orange")

    tut = turtle.Screen()

    side = 300
    for i in range(10):
        form_tri(side)
        side -= 30 
