# Name: Abhinav Shrestha
# Class: CSCI 1411-003
# Due Date:
# Description: 
# Status:

def main():
    # first, ask the user for their first and last names
    firstName = input ("Enter your first name ")
    lastName = input ("Enter your last name ")

    # now ask them for the temperature they wish to convert
    f = (int)(input ("What is the temperature in Fahreneit? "))

    # print conversion for input degree and next ten degrees

    for i in range(11):
        #convert farenheit to celsius using f+i
        c= ((f+i)-32)*(5/9)
        
        print(firstName," ", lastName, " Farenheit temperature of ", f+i, " degrees in Celsius is ", c, " degrees.")
main()
