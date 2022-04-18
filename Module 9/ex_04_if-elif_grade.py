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


    #using nested if-statements
    if (numerical_grade > 100):
        letter_grade = 'unknown'
        print (numerical_grade, 'must be less than 100')
    elif (numerical_grade >= 90):
        letter_grade = 'A'
    elif (numerical_grade >= 80):
        letter_grade = 'B'
    elif (numerical_grade >= 70):
        letter_grade = 'C'
    elif (numerical_grade >= 60):
        letter_grade = 'D'
    elif (numerical_grade >= 0):
        letter_grade = 'F'
    else:
        letter_grade = 'unknown'
        print (numerical_grade, 'must be positive')
    


    print ('Your letter grade is', letter_grade)
