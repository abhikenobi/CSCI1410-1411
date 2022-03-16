# Abhi
# Shrestha
# Date: 02/23/22
# Description: Lab 5. This lab shows various operations of String datatype

def main():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    
    # Calculate teh size/length of string using len() function
    length1 = len(firstName)
    print(f"\nThe length of your first name is: {length1} letters")
    length2 = len(lastName)
    print(f"The length of your last name is: {length2} letters")
    
    # "+" operator is used to concatebate 2 strings
    fullName = firstName+" "+lastName
    print(f"\nYour full name is : {fullName}\n")
    
    # "*" operator is used as a repitition to make multi. copies of a string
    n = int(input("Enter a number: "))
    print("Repeating your first name {n} times")
    print((firstName+" ")*n,'\n')
    
    # Iterate through the characters using a for loop
    print("Printing the full name using a for loop:")
    for ch in fullName:
        print(ch,end="")
    
    # A string is a sequence of character. Each individual character can be accessed by using index. In Python index starts from 0.
    # Here is an example how we can run a loop to access all characters from a string.
    
    print("\nPrinting the name in reverse order:")
    for i in range(-1,-(len(fullName)+1),-1):
        print(fullName[i],end="")
    
    # Slicing operator is used to access a contiguous sequence of characters or substring.
    # Following is an example of generating username from using the first 3 characters of the last name combined with the first 3 characters of the first name.
    
    userName = lastName[0:3]+firstName[0:3]
    print(f"\nYour username is: {userName}")

main()
    