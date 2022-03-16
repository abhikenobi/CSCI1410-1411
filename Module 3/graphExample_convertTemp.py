# convert_gui.pyw
# Program to convert Celsius to Fahrenheit using a simple
#   graphical interface.

from graphics import *

def main():

    # create a window
    # ---> GraphWin("windowName", width, heigh)
    win = GraphWin("Celsius Converter", 400, 300)

    # ==> setCoords(self, x1, y1, x2, y2)
    # Set coordinates of window to run from (x1,y1) in the
    # lower-left corner to (x2,y2) in the upper-right corner.
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    # Text(Point, "message")
    Text(Point(1,3), "   Celsius Temperature:").draw(win)

     # Text(Point, "message")
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)


    # Entry(centerPoint, width) Constructs an Entry having the given center point and width.
    #     The  width is specified in number of characters of text that can be displayed.
    inputText = Entry(Point(2.25,3), 5)

    # Set the initial value to my inputText (Entry)
    inputText.setText("0.0")

    #draw the inputText (Entry) in the window
    inputText.draw(win)
    
    #configure the coordinates for the output in the 
    outputText = Text(Point(2.25,1),"")
    outputText.draw(win)

    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)

    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    # display output and change button
    outputText.setText(round(fahrenheit,2))
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()
    
main()
