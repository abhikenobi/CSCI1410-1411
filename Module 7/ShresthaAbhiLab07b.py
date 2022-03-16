# Abhi Shrestha
# 3/15/22
# This program will calculate the average scores of the students
import re
def main():
    try:
        # Ask user for input file name
        infileName = input("Please type in the name of yourfile containing the students' scores: ")
        # Ask user for output file name
        outfileName = input("Please enter the name of your output file: ")
        print("Calculating .........................")
        # checking and adding file format to end of file name if needed
        if infileName.endswith(".txt"): infileName = infileName
        else: infileName = infileName+'.txt'
        if outfileName.endswith(".txt"): outfileName = outfileName
        else: outfileName = outfileName + '.txt'
        # Open input and output files
        data = open(infileName, 'r')
        output = open(outfileName, 'w')
        # iterrate through input file
        for line in data:
            # splite lines to separate each value
            line = line.replace("\n", "")
            lineSplit = re.split(r' ',line)
            # Get the username of the students
            name = lineSplit[0]
            # Convert all numbers into integers
            for i in range(1,len(lineSplit)): lineSplit[i]=eval(lineSplit[i])
            # Calculate their avg scores
            # This will sum all the scores and skip the name at 0th index
            sumScores = sum(lineSplit[1:])
            # number of scores in case it is different per student, - 1 is to avoid counting username
            scoreCount = len(lineSplit)- 1
            avgScore = sumScores/scoreCount
            # Write results to output file
            print(f"{name}: {avgScore}", file=output)
        # Close files
        data.close()
        output.close()
        print(f"Done! Your average scores have been calculated and stored in {outfileName}! Have a great day!")
    except FileNotFoundError:
        print("Error. Unable to find your file. Please recheck if you typed in the file name correctly and the file is the correct format (.txt)")    
main()
