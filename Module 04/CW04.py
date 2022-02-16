#import
from graphics import *

def main():
    #make window
    win = GraphWin("Classwork 4")

    print('Click to show Question 1')

    #click to start
    win.getMouse()

    #question 1
    p1 = Point(130,130)

    p1.draw(win)

    print("A point should be drawn")

    print('Click to show Question 2')

    #event staller
    win.getMouse()

    #question 2
    c = Circle(Point(30,40),25)
    c.setFill('blue')
    c.setOutline('red')
    c.draw(win)

    print("A circle should be drawn")

    print('Click to show Question 3')

    #event staller
    win.getMouse()

    #question 3
    r = Rectangle(Point(20,20),Point(40,40))
    r.setFill(color_rgb(0,255,150))
    r.setWidth(3)
    r.draw(win)

    print("A rectangle should be made")

    print('Click to show Question 4')

    #event staller
    win.getMouse()

    #question 4
    l = Line(Point(100,100),Point(100,200))
    l.setOutline('red')
    l.setArrow('first')
    l.draw(win)

    print("A line should be drawn")

    print('Click to show Question 5')

    #event staller
    win.getMouse()

    #question 5
    o = Oval(Point(50,50),Point(60,100))
    o.draw(win)

    print("An oval should be drawn")

    print('Click to show Question 6')

    #event staller
    win.getMouse()

    #question 6
    shape = Polygon(Point(5,5),Point(10,10),Point(5,10),Point(10,5))
    shape.setFill('orange')
    shape.draw(win)

    print("A polygon should be created")

    print('Click to close the window')

    #event staller
    win.getMouse()

    #close window
    win.close()

#call up function
main()

