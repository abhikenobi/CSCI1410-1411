"""
Name: Abhi Shrestha
Date: April 12, 2022
This program will perform the following tasks:
    1) 
        a) prompt the user for a name of a text file
        b) prompt the user for a word
        c) handle any FileNotFoundError using try/except blocks
    2) count the number of times the given word appears in the file
    3) display the total number of times the word appears in the file
"""
def wordSearch(fileName,searchTerm):
    """"
    Name: wordCounter
    Description: Returns the number of times a given search term is found in the text file
    Parameter: 
        fileName - name of text file to open
        searchTerm - the search term being parsed
    """
    try:
        # open file
        with open (fileName, "r") as file:
                data = file.readlines()
                # get rid of newspace strings (\n)
                for i in range(len(data)):
                    data[i] = data[i].replace("\n","")
                # start wordcount process
                # initialize counter
                wordCount = 0
                # iterrate through lines of text
                for line in data:
                    # iterrate through words in each line
                    for word in line.split(" "):
                        # using .lower() to avoid any miss due to case sensitivity
                        # using in rather than == to avoid any punctuations (ex: this, or this. vs this)
                        if searchTerm.lower() in word.lower():
                            wordCount += 1
                        else:
                            wordCount = wordCount
        # close file
        file.close()
    except FileNotFoundError as err:
        print(f"A file with name '{fileName}' was not found. Please try again.")
        main()
    except:
        print("Unknown error detected. Restarting program ...\n")
        main()
    return wordCount
def keepGoing():
    """
    Name: keepGoing
    Description: reruns main program based on user input
    """
    ans = input("Would you like to run again [Y/N]? ").lower()
    acceptable = ["yes","y","no","n"]
    while ans not in acceptable:
        print("Error, wrong input. Please try again.")
        keepGoing()
    else:
        if ans == acceptable[0] or ans == acceptable[1]:
            main()
        elif ans == acceptable[2] or ans == acceptable[3]:
            print("   .    _  .     _____________")
            print("   |\_|/__/|    /             \ ")
            print("  / / \/ \  \  / Thank you and \ ")
            print(" /__|O||O|__ \ \    Goodbye!   / ")
            print("|/_ \_/\_/ _\ | \  ___________/ ")
            print("| | (____) | ||  |/ ")
            print("\/\___/\__/  // _/ ")
            print("(_/         ||")
            print(" |          ||\ ")
            print("  \        //_/ ")
            print("   \______// ")
            print("  __|| __|| ")
            print(" (____(____) ")
def main():
    # prompt user for file name and search word
    fileName = input("What is the name of the file? ")
    searchTerm = input("What word would you like to search? ")
    # check if user input includes file type, add if not
    if fileName.endswith(".txt"):
        pass
    else:
        fileName = fileName+".txt"
    # run wordSearch function
    searchResults = wordSearch(fileName,searchTerm)
    # display results
    print("Calculating ........ \n")
    print(f"In the file {fileName}, the word '{searchTerm}' was found {searchResults} times.")
    keepGoing()
main()
