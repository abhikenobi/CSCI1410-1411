################################################################
#
# This python program read a set of numbers from an input file,
#calculate sum and average and displys the result on screen
#
# Author: Dr. Salim Lakhani
# Version: 20200922
#
################################################################

def main():

    count = 0
    sum = 0
    infile = open ('numbers.txt', 'r')
    for line in infile:
        num = int (line)
        sum = sum + num
        count = count + 1
    infile.close()

    average = sum / count

    print ('Number of data:', count)
    print ('Sum of numbers is:', sum)
    print ('Average is: {0:.2f}'.format(average))
    
main()