# import any libraries needed
from graphics import *

def main():
    winName = "Lab 4 - Shrestha Abhi"
    
    # Create a graphWin of size (500,500)
    win = GraphWin(winName, 500, 500)
    
    # Ask for color of circle 1
    color1 = input("What color would you like your circle to be? ")
    # Ask of x, y of center of circle 1
    x1,y1 = eval(input("What are the x, y coordinates of the center of the cirlce? "))
    # Ask for radius of circle 1
    radius1 = eval(input("What is the radius of the circle? "))
    # Draw the circle
    center1 = Point(x1, y1)
    circle1  = Circle(center1, radius1)
    circle1.setFill(color1)
    circle1.draw(win)
    
    # Create 2nd circle
    radius2 = (radius1/2)
    color2 = "green"
    x2 = x1
    # distance between centers of circles is 2*radius1
    circleDistance = 2*radius1
    y2 = (y1-(circleDistance))
    center2 = Point(x2,y2)
    circle2 = Circle(center2, radius2)
    circle2.setFill(color2)
    circle2.draw(win)
    
    # Draw red line between center of 2 circles
    lineColor = "red"
    line = Line(center1, center2)
    line.setFill(lineColor)
    line.draw(win)
    
    # Prompt user to start circle movement
    print("Click on the window to rotate the green circle!")
    win.getMouse()
    
    # Move circle 2 to the right of cirlce 1
    circle2.move(circleDistance,circleDistance)
    # this gets rid of the line…it doesn’t have to be in the loop!
    line.undraw()
    # Fine center of moved circe
    newCenter = circle2.getCenter()
    # Draw a new line from center of first circle to center of new circle
    line = Line(newCenter, center1)
    line.setFill(lineColor)
    line.draw(win)
    
    print("Click on the window to rotate the green circle!")
    win.getMouse()
    
    # Move circle 2 to right below cirlce 1
    circle2.move((-1*circleDistance),circleDistance)
    
    # undraw and redraw the line
    line.undraw()
    newCenter = circle2.getCenter()
    line = Line(newCenter, center1)
    line.setFill(lineColor)
    line.draw(win)
    
    print("Click on the window to rotate the green circle!")
    win.getMouse()
    
    #  Move circle 2 to left for cirlce 1
    circle2.move((-1*circleDistance),(-1*circleDistance))
    
    # undraw and redraw the line
    line.undraw()
    newCenter = circle2.getCenter()
    line = Line(newCenter, center1)
    line.setFill(lineColor)
    line.draw(win)
    
    print("Click on the window to rotate the green circle!")
    win.getMouse()
    
    # Move circle 2 back to top of circle 1
    # Method 1
    circle2.move(circleDistance,(-1*circleDistance))
    
    # undraw and redraw the line
    line.undraw()
    newCenter = circle2.getCenter()
    line = Line(newCenter, center1)
    line.setFill(lineColor)
    line.draw(win)
    
    # # Method2
    # circle2.undraw()
    # circle2 = (center2, radius2)
    # circle2.setFill(color2)
    # circle2.draw(win)
    # # undraw and redraw the line
    # line.undraw()
    # newCenter = circle2.getCenter()
    # line = Line(newCenter, center1)
    # line.setFill(lineColor)
    # line.draw(win)
    
    print("Click to close the window!")
    win.getMouse()
    win.close()
main()
