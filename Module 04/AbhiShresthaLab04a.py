# File AbhiShresthaLab04a.py
# this is the first part of lab4. we will be drawing some simple objects using the graphics package. In this program the user will be prompted for several key object characteristics like size, shape, color, etc

# tell python we want to use the graphics package and all the things in it 
# this package should be given to you by your instructor, and it must reside in the same directory as your code. 

from graphics import *
#time is another package we will use, it is a system package, so python will find it
import time
# define the main routine

def main():
    # Draw a colored circle at a point specified by the user
    
    # Ask user for window name
    winName = input("What would you like the name of the window to be? ")
    
    # Ask for a color
    # Note, only certain colors are valid (blue, green, yellow, red, etc)
    color1 = input("What color would you like your circle to be? ")
    
    # Asks for center cooridnates of the cirlce
    x1,y1 = eval(input("What are the x, y coordinates of the center of the cirlce? "))
    
    # Ask for radius of the circle
    radius1 = eval(input("What is the radius of the circle? "))
    
    # Create window object and draw circle
    win = GraphWin(winName, 500, 500)
    
    center1 = Point(x1, y1)
    circle1  = Circle(center1, radius1)
    circle1.setFill(color1)
    circle1.draw(win)
    
    # Repeat for input process for 2nd circle
    color2 = input ("What color would you like the second circle to be? ")
    
    x2, y2 = eval(input ("What are the x, y coordinates of the center of circle? "))
    
    radius2 = eval(input("What is the radius of the circle? "))
    
    center2 = Point (x2, y2)
    
    circle2 = Circle(center2, radius2)
    
    circle2.setFill (color2)
    
    circle2.draw (win)
    
    # Draw a line between the centers of the 2 circles
    line = Line(center1, center2)
    # Make color of line red
    line.setFill("red")
    # Draw the line
    line.draw(win)
    
    # Wait for mouse click
    win.getMouse()
    
    # this loop will now move the circle 
    for i in range (10):
         # we arbitrarily chose to move the circle 10 points in the x&y directions
        circle1.move(10,10)
        # this gets rid of the line…it doesn’t have to be in the loop!
        line.undraw()
        # tell the computer to pause so that we can see the circle moving
        time.sleep(2)
        
    # Fine center of moved circe
    newCenter = circle1.getCenter()
    
    # Draw a new line from center of first circle to center of new circle
    line = Line(newCenter, center2)
    line.setFill("red")
    line.draw(win)

main()


    
    
