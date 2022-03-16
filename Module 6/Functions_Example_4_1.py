################################################################
#
# This program demos the scope of a variable
#
# Author: Dr. Salim Lakhani
# Version: 20200827
#
################################################################


def main ():

    x = 5
    print ('Value of x in main before calling function: ', x)
    function_2()
    print ('Value of x in main before calling function: ', x)



def function_2 ():
    
    x = 5
    print ('Value of x at start of the function: ', x)

    x = x + 10

    print ('Value of x at end of the function: ', x)

    
    
    



