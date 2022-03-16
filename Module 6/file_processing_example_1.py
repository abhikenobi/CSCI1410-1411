################################################################
#
# This python program will demonstarte three different ways to
# read data from a file.
#   First method: read the whole file using read method.
#   Second method: read one line at a time using readline method
#   Third method: read all lines as a list using readlines method
#
# Author: Dr. Salim Lakhani
# Version: 20200922
#
################################################################
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def main():

    print ('Read the whole file using read method:')
    infileName = askopenfilename()
    infile = open (infileName, 'r')
    data = infile.read()
    print(data)
    infile.close()
    print()
    
    print ('Read one line at a time')
    infileName = askopenfilename()
    infile = open (infileName, 'r')
    data = infile.readline()
    print(data)
    infile.close()
    print()

    print ('Read all lines using readlines method.')
    infileName = askopenfilename()
    infile = open (infileName, 'r')
    list = infile.readlines()
    print (list)
    infile.close()
    print()



    print ('Read one line at a time using loop')
    infileName = askopenfilename()
    infile = open (infileName, 'r')
    for line in infile:
        print(line, end='')
    infile.close()
    print()
    
main()