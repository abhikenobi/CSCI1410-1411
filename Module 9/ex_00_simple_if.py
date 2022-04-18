################################################################
#
# Convert a students numerical grade to letter grade
#
# Author: Dr. Salim Lakhani
# Version: 20201015
#
################################################################

def main():
    numerical_grade = int (input ('Enter your numerical grade: '))

    #if numerical grade is above 80 then letter grade is A
    if (numerical_grade >= 80):
        letter_grade = 'A'

    #if numerical grade is above between 60 and 79 then letter grade is B
    if (60 <= numerical_grade < 80):
        letter_grade = 'B'

    #if numerical grade is beloe 60 then letter grade is C
    if (numerical_grade < 60):
        letter_grade = 'C'


    print ('Your letter grade is', letter_grade)
