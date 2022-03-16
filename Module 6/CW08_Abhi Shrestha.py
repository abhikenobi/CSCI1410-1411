# Classwork 8
# Name: Abhinav Shrestha

# import necessary libraries
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

def question1():
    # Open a file for reading
    fileName = 'words.txt'
    
    file = open(fileName,'r')
    
    data = file.read()
    
    # Close file (necessary step if you need to reitirate through file)
    file.close()
    
    # Keeps count accurate but still reads new line
    # lines = [line.strip() for line in file]
    # print(lines)
    
    # lines = [line for line in data.split('\n')]
    # Possible Solution
    # file.read().replace('\n', ' ')
    lines = data.split("\n")
    
    # intialize variables and counters
    totalWords = 0
    totalCharacters = 0
    totalWordLength = 0
    averageWordLength = 0
       
    # Read one line at a time
    for line in lines:
        # print('\n')
        print(line)
        
        # Count the number of words in the line:
        # Split line/sentence using space parameter and split method
        wordSplit = line.split()
        
        # Loop through split array to find the length of each word (for future average calculation)
        for word in wordSplit:
            # Add to letter/length counter
            totalWordLength += len(word)
        
        # Number of words is length of split array since each index is 1 word
        wordCount = len(wordSplit)
        
        # Add to total word counter
        totalWords += wordCount
        
        # Count the total number of characters (w/o spaces) in the line
        characterCount = len(line) - line.count(" ")
        # Add to total character (w/o space) counter
        totalCharacters += characterCount
        # >>>>>>>Same as totalCharacters = totalCharacters + characterCount<<<<<<<
        
        # Print results
        # print(f"\n{totalWordLength} letters")
        if wordCount != 0 or characterCount != 0:
            print(f"\nThis line has: {wordCount} words")
            print(f"\nThis line has: {characterCount} characters not including spaces")
    
    # Calculate average word length
    # Total # of Letters / Total # of Words
    averageWordLength = totalWordLength/totalWords
    
    # Print results for total word/character count and average word size
    # print(f"\n total word length is : {totalWordLength} letters")
    print(f"\nThe file has a total of: {totalWords} words")
    print(f"\nThe file has a total of: {totalCharacters} characters")
    print(f"\nThe file had words with an average of {averageWordLength:.2f} letters")

    main()

def question2():
    
    print("This program will take the data from you input file and calculate your future value of your investment. To check results, open the output file \n")
    
    # Open your input file
    fileName = 'futval_data.txt'
    
    inputFile = open(fileName,'r')
    
    # Assign text in file to your variables
    principal = eval(inputFile.readline())
    apr = eval(inputFile.readline())
    count = eval(inputFile.readline())
    
    # Open/Create an output file
    outputFileName = "future_projections.txt"
    outputFile = open(outputFileName, 'w')
    
    # Initial Variables
    initial_year=0
    
    print (f'\nYear \t Value in $', file=outputFile)
    print ('------------------------------', file=outputFile)
    # Added an int() incase the user inputted a decimal changed to f"" string and formatted to 2 decimal points
    print (f"{int(initial_year)} \t $ {principal:.2f}", file=outputFile)

    next_year = initial_year
    
    for i in range(count):
        next_year += 1
        principal = principal * (1 + apr)
        # changed to f"" string and formatted to 2 decimal points
        print(f"{next_year} \t $ {principal:.2f}", file=outputFile)

    # changed to f"" string and formatted to 2 decimal points
    print(f"\nThe value in {count} years is: $ {principal:.2f}", file=outputFile)
    
    # Close files
    inputFile.close()
    outputFile.close()
    main()


def main():
    print(f"\n                     Welcome to Classwork 8                    \n")
    print(f"---------------------------------------------------------------\n")

    ans = input("What question would you like to see [1] or [2]? ")
    possibleAnswers = ["1", "2", "one", "two"]

    while ans not in possibleAnswers:
        print("Please recheck your input. Please type in either the number or word [1/one] or [2/two]")
        ans = input("What question would you like to see [1] or [2]? ")

    if ans == "1" or ans == "one":
        question1()
    elif ans == "2" or ans == "two":
        question2()
    else:
        print("Error")

main()