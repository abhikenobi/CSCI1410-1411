# Write a program that should accept a file name as input and a word to be searched into the file, then print how many times the word was found into the file considering searching the  word  in lower and upper case.

# import necessary libraries
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

try:
    # fucntion to read file and search for search term
    def readFile(fileName,searchTerm,searchResults):
        # checking and adding file format to end of file name if needed
        if fileName.endswith(".txt"):
            name = fileName
        else:
            name = fileName+'.txt'
        # opening file
        with open(name,'r') as file:
        # reading data in file and storing in a variable
            data = file.read()
        # closing file after finshed reading file
        file.close()
        
        for line in data.split(" "):
            if line.lower() == searchTerm.lower():
                searchResults += 1
            elif line.upper() == searchTerm.upper():
                searchResults += 1
            else:
                searchResults = searchResults
        # display file contents)
        print("Calculating .....")
        print(f"The word {searchTerm} was found {searchResults} times in the file.")

    def main():
        # a.
        name = input("What is the name of your file? ")
        searchTerm = input("What word would you like to search for? ")
        searchResults = 0
        readFile(name,searchTerm,searchResults)
    # run main
    main()
except ValueError:
    print("This file seems to contain more than just numbers. Please recheck if you chose the correct file.")
    main()
except FileNotFoundError:
    print("Error. Unable to find your file. Please recheck if you typed in the file name correctly and the file is the correct format (.txt)")
    main()
