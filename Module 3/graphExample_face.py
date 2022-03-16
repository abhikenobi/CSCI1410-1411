#import graphics
from graphics import *
def main():
    # constructing a face with basic shapes
    
    #       Sintax = GraphWin("windowName", width, heigh)
    win = GraphWin("My window",400,400)

    # Point(X,Y) - cartesian coordinate inside the window

    #Circle(Point,radius) - Point to the center of the Circle
    p1 = Point(40,100)
    head = Circle(p1, 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    #Circle(Point,radius)
    eye1 = Circle(Point(30, 105), 5)
    # fill the cicle with blue
    eye1.setFill('blue')
    # draw the circle in the window
    eye1.draw(win)

    # Line(Point,Point) -    # The second eye is a line
    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints

    # setWidth(n) - Set line weight to width
    eye2.setWidth(3)

    # draw the line on the windows
    eye2.draw(win)

    # build the mouth
    # Oval(Point, Point)
    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box

    # fill the oval with red
    mouth.setFill("red")

    #draw the mouth in the window
    mouth.draw(win)

    # Display some text in the window
    # Text(Point, 'message')
    label = Text(Point(100, 120), 'A face')

    #draw the label on the window
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()  # wait until click the mouse
    win.close()



main()

    
