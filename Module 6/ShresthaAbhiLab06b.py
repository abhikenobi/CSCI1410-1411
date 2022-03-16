# Abhi
# Shrestha
# Date: 3/2/2022
# Description: Lab 6. This lab demonstrates various functions of string datatype
def main():
    try:
        # Ask user for string input
        txt = input("Please input a sentence: ")
        subtxt = txt.split(" ")
        newtxt = "-".join(subtxt)
        # Ask user for a key input(integer)
        key = int(input("Please input in a number for your key: "))
    except ValueError:
        print("Error detected. Please try again. Make sure you input in a whole number.")
        key = int(input("Please input in a number for your key: "))
    encodedString = ""
    print("\nEncoding ...")
    print("Your sentence using the key you gave was encoded to: ")
    for ch in newtxt:
        ch = chr(ord(ch)+key)
        encodedString += ch
        print(ch,end="")
    print("\nDecoding ...")
    print("Your sentence was decoded to: ")
    for ch in encodedString:
        ch = chr(ord(ch)-key)
        if ch == "-":
            ch = " "
        print(ch,end="")
main()