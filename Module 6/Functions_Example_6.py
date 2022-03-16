################################################################
#
# This program demos the scope of a variable
#
# Author: Dr. Salim Lakhani
# Version: 20200827
#
################################################################


def main ():

    y = 5
    print ('Value of y in main before calling function: ', y)
    function_1(y)
    print ('Value of y in main before calling function: ', y)
    
    



def function_1 (x):
    
    print ('Value of x at start of the function: ', x)

    x = x + 10

    print ('Value of x at end of the function: ', x)
