################################################################
#
# This program demos the scope of a variable
#
# Author: Dr. Salim Lakhani
# Version: 20200827
#
################################################################


def main ():

    list = ['Apple', 'Mango']
    x = 2
    print (x, list)
    change_list (x, list)
    print (x, list)
    
    



def change_list (x, list):
    list.append ('Apple')
    x = x + 1

