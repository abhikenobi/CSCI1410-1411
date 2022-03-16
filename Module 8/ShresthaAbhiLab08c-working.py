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
        try:
            number = eval(input("Enter a number: "))
            numList.append(number)
        except ValueError:
            print("Invalid input. Please type in a number and not a word.")
            number = eval(input("Enter a number: "))
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
