import turtle

t = turtle.Turtle() # create turtle named t
win = turtle.Screen() # setup window

win.setup(width=400, height=400) # line to make smaller window
win.setworldcoordinates(-80, -80, 80, 80) # zoom in

t.forward(50)
t.right(90)
t.forward(50)
t.color("red")
t.left(45)
t.back(50)
t.right(90)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)
t.down()
t.forward(10)
t.up()
t.forward(10)

win.exitonclick() # setup to close on click

