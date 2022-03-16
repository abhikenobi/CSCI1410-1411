from graphics import *

#win = GraphWin("Click Me!",600,600) #default is 200, 200

#p = win.getMouse()

#i = 1

#while i == 1:
#    p = win.getMouse()

#    print(f"you clicked {p.getX()} {p.getY()}")

#    if p.getX() > 100:
#        break
#    if p.getY() > 100:
#        break

def triangle():
    #make your window
    winObj = GraphWin("Making a Triangle!",600,600)

    #get and draw 3 vertices of a triangle
    p1 = winObj.getMouse() #wait for an event

    #print coordinates of your point
    print(f"p1.X = {p1.getX()} and p1.Y = {p1.getY()}")

    #draw point on window
    p1.draw(winObj) #places point physically in window at point of mouse click

    #repeat for p2 and p3
    p2 = winObj.getMouse()

    print(f"p2.X = {p2.getX()} and p2.Y = {p2.getY()}")

    p2.draw(winObj)


    p3 = winObj.getMouse()

    print(f"p3.X = {p3.getX()} and p3.Y = {p3.getY()}")

    p3.draw(winObj)

    #put vertices in list
    vertices = [p1,p2,p3]

    triangle = Polygon(vertices)

    triangle.setFill("red")

    triangle.setOutline("black")

    triangle.setWidth(4)

    triangle.draw(winObj)

    winObj.getMouse() # pauses code until you click mouse

    winObj.close() #closes window after you click mouse
    
#execute program
triangle()

    
    
