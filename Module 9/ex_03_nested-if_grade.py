################################################################
#
# Convert a students numerical grade to letter grade conversion
#
# Author: Dr. Salim Lakhani
# Version: 20201015
#
################################################################

def main():
    numerical_grade = int (input ('Enter your numerical grade: '))

    #using nested if-statements
    if (numerical_grade >= 80):
        letter_grade = 'A'
    else:
        if (numerical_grade >= 60):
            letter_grade = 'B'
        else:
            letter_grade = 'C'


    print ('Your letter grade is', letter_grade)
