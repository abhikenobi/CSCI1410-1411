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
    y = 10
    
    result1, result2 = function_1 (x, y)

    print ('sum is: ', result1)
    print ('difference is: ', result2)
    
    



def function_1 (a, b):
    
    sum = a + b
    diff = a - b

    return sum, diff

