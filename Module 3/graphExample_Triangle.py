#import graphics
from graphics import *
# Example of how to build a triangle using graphics 
def main():
    # winVar = GraphWin("windowName", width, heigh)
    winObj = GraphWin("My window",400,400) # 200,200
    # Get and draw three vertices of triangle
    p1 = winObj.getMouse()  # wait for an event
    print("p1.X=", p1.getX(), " p1.Y=", p1.getY())
    
    p1.draw(winObj)

    p2 = winObj.getMouse()
    print("p2.X=", p2.getX(), " p2.Y=", p2.getY())
    p2.draw(winObj)

    p3 = winObj.getMouse()

    print("p3.X=", p3.getX(), " p3.Y=", p3.getY())
    
    p3.draw(winObj)

    vertices = [p1, p2, p3]
    triangle = Polygon(vertices)
    triangle.setFill('green')
    triangle.setOutline('red')
    triangle.setWidth(4) # Set line weight to width
    triangle.draw(winObj)
    winObj.getMouse() # wait for an event
    winObj.close()


main()

    
