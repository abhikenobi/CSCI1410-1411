#import any libraries needed
from math import ceil
#initial variables
segment_length = 12
price_segment = 1.88

def main():

    # Ask the user the length, in inches, of the box
    length = (eval(input("What is the length, in inches, of the box? ")))

    # Ask the user the width, in inches, of the box
    width = (eval(input("What is the width, in inches, of the box? ")))

    # Calculate the perimeter of the box and print out
    perimeter = (2*length)+(2*width)

    print(f"Thank you, it appears your box has a perimeter of: {perimeter} inches.")

    # Calculate the number of segments (one segment is 12 inches) needed to trim the box (go around the perimeter) and print results

    #int result
    trim1 = ceil(perimeter/segment_length)
    #float result
    trim2 = perimeter/segment_length

    print(f"You will need: {trim1} trim boards.")

    # Calculate cost and print
    cost = price_segment*trim1

    print(f"This will cost: ${round(cost, 2)}.")

    # Calculate waste and print
    wastedTrim = (trim1-trim2)*segment_length

    wastedCost = price_segment*(trim1-trim2)

    print(f"You will waste {round(wastedTrim, 2)} inches of trim which equals to a waste of ${round(wastedCost, 2)}.")

main()