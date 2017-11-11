import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

size = 300
myWin.setup(width=size, height=size, startx=30, starty=30)
myTurtle.speed(10) # speed from 1 to 10

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

figsize = 100
print( myTurtle.position())
myTurtle.penup()
myTurtle.goto(-figsize/2,figsize/2)
myTurtle.pendown()

drawSpiral(myTurtle,100) # do recursion

myWin.exitonclick() # remember to click on widow to close
