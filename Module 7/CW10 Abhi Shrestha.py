# Classwork 10
# Name: Abhinav Shrestha

# import necessary libraries
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

try:
    # #1. Write a function that will read a set of integers in file and return the list, pass file name as parameter
    def readFile(fileName,dataList):
        # checking and adding file format to end of file name if needed
        if fileName.endswith(".txt"):
            name = fileName
        else:
            name = fileName+'.txt'
        # opening file
        with open(name,'r') as file:
        # reading data in file and storing in a variable
            data = file.readlines()
        # closing file after finshed reading file
        file.close()
        # append data into list
        for line in data:
            dataList.append(int(line))
        # display file contents
        print(f"\nYour file contains the following:\n")
        print(dataList)

    # #2. Write a function that adds all the number in a list and returns the result. List is passed as a parameter
    def sumN(dataList):
        # initialize counter
        finalsum = 0
        # use for loop to iterate through list
        for i in dataList:
            finalsum += i
        # display sum
        print(f"\nThe sum of the numbers in your file added up to: {finalsum}")

    # #3. Write a main function that will ask:
        # a. user for name of input file
        # b. calls function from #1 to read numbers from input file
        # c. calls function from #2 to calculate sum of integers
        # d. displays sum of integers
    def main():
        # a.
        name = input("What is the name of your file? ")
        dataList = []
        # b.
        readFile(name,dataList)
        # c and d.
        sumN(dataList)
    # run main
    main()
except ValueError:
    print("This file seems to contain more than just numbers. Please recheck if you chose the correct file.")
    main()
except FileNotFoundError:
    print("Error. Unable to find your file. Please recheck if you typed in the file name correctly and the file is the correct format (.txt)")
    main()
