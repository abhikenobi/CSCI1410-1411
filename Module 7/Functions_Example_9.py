################################################################
#
# This program demos the scope of a variable
#
# Author: Dr. Salim Lakhani
# Version: 20200827
#
################################################################

def main ():
    n = int(input('Enter an integer: '))
    total = sum(n)
    print ('total is: ', total)
    
def sum(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total

main()