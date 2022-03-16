################################################################
#
# This program demos the scope of a variable
#
# Author: Dr. Salim Lakhani
# Version: 20200827
#
################################################################

def main ():
    a = 5
    b = 10
    print ('Value of a in main: ', a)
    print ('Value of b in main: ', b)
    function_1 (b, a)
    
def function_1 (a, b):    
    print ('Value of a in function1: ', a)
    print ('Value of b in function1: ', b)

main()