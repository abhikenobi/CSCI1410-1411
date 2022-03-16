# Abhi Shrestha
# 3/16/2022
# write a function findDoubles that will take a list as a parameter and double the values of the list
def findDoubles(starterList):
    for i in range(len(starterList)):
        starterList[i] = 2*starterList[i]
def main():
    # initialize starter list
    numList = []
    # loop through to prompt user for a number and add that number to the list
    for i in range(5):
            number = input("Enter a number: ")
            # checking if input is a valid number and not just letters
            # .lstrip() in case input is a negative number
            # .isdigit() will check if input has letters (= True) or not (= False)
            while number.lstrip("+|-").isdigit() == False:
                print("Invalid input. Please try again")
                number = input("Enter a number: ")
            else:
                number = eval(number)
                numList.append(number)
    print("Your entered numbers:")
    print(numList)
    # call up findDoubles function
    findDoubles(numList)
    print("The doubles of your numbers:")
    print(numList)
try:
    main()
except:
    print("Error Occurred. Restarting ....")
    main()
