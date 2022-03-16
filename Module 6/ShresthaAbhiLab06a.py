# Abhi
# Shrestha
# Date: 3/2/2022
# Description: Lab 6. This lab demonstrates various functions of string datatype
def main():
    # Python translates each character to a number. The ord() function in python accepts a single character string as an argument and returns the numeric code of it.
    ch = input("Please input a single character: ")
    value = ord(ch)
    print("The numeric representation of {} is {}".format(ch,value))
    # The chr() function does the reverse. chr() function takes a integer number as an argument and returns the equivalent character.
    print(f"The equivalent character of the number {value} is {chr(value)}.")
    # The following piece of code will take a string as input and it will convert each of the character as a sequence of numbers (separated by whitespace)
    txt = input("Please enter a text: ")
    for ch in txt:
        print(ord(ch), end=" ")
    #split function splits a string into a list of substrings based on a delimiter.
    txt1 = input("\nPlease enter a string with space: ")
    listSubStrings = txt1.split(" ")
    print(listSubStrings)
    #join function joins the list of strings into one string using a delimiter
    newString = "-".join(listSubStrings);
    print(newString)

main()



