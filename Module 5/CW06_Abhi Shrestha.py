# Write a Program that:
# 1. counts the number of words in a sentence entered by an user
# 2. counts the total number of characters (not including spaces) in a sentence entered by a user
# 3. calculates the avg. word length in a sentence entered by an user

def main():
    # ask for user input of a sentence
    sentence = input("What is your sentence? ")

    # 1. count the number of words in the senteence

    # split the sentence into separate words using space as the split parameter
    wordSplit = sentence.split(" ") #Seems to work with or withour period in sentence input

    # count the length of the word
    wordCount = len(wordSplit)

    # print results
    print(f"Your sentence has {wordCount} words.")

    # 2. count the total # of character not including spaces
    # initialize variable
    characterSplit =[]
    # char for char in wordSplit

    for word in wordSplit:
        characterSplit.append(list(word)) #list() splits string into an array of characters making characterSplit an array containing arrays
        
    # Find the number of characters in list of lists
    # initialize counter
    characterCount = 0

    # loop through chracterSplit array and count the length of each array created by list() method
    for char in characterSplit:
        characterCount += len(char)

    # Print results
    print(f"Excluding spaces, your sentence has {characterCount} characters")

    # 3. calculate average word length

    # initialize counter and count the number of characters in each word
    wordSum = 0

    for word in wordSplit:
        wordSum += len(word)

    # calculate average
    averageWordLength = round((wordSum/wordCount), 2)

    # print results
    print(f"Your sentence has words with an approximate average of {averageWordLength} letters")

main()