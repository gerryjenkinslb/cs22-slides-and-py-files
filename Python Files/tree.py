import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)  # recurse next branch 15 shorter
        t.left(40)
        tree(branchLen-15, t)  # recurse next branch 15 shorter
        t.right(20) # return to start direction
        t.backward(branchLen)  # back down branch same to start pos

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()

    myWin.setup(width=300, height=300)  # line to make smaller window
    t.speed(10)  # max speed on drawing

    t.left(90)  # these line position turtle in window
    t.up()      # and point turtle 'up'
    t.backward(100)
    t.down()    # now at base of tree, lower pen
    t.color("green")  # set color of tree start
    t.width(3)
    tree(75, t)  # draw tree starting at 75 length branches
    myWin.exitonclick()

main()
