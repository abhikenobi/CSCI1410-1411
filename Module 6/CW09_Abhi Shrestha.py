# Name: Abhi Shrestha
# Classwork 9
# Date: 2/24/22

# Question 1

# Write a function circleArea(radius) to calculate and display area of a
# cicle area=π*(r**2)
def circleArea(radius):
    # import pi from math library
    from math import pi
    # calculate area
    area = pi*(radius**2)
    # display results
    print("\nGiven the radius: {}, the subsequent circle's area would be: {:.3f}.".format(radius,area))
# Question 2

# Write a function sumN (n) to calculate and print the sum of first n
# numbers (1 + 2 + 3 + … + n)
def sumN(n):
    # initialize sum counter
    a=0
    # create for loop to iterrate through all numbers with n as the stopping point
    for i in range(n+1): # n+1 because range(n) starts at 0, stops at n-1
        a += i
    # display results
    print(f"\nThe sum of all numbers from 1 to {n} is: {a}")


# Question 3

# Write a function sumNcubs(n) to calculate and print the sum of cubes
# of first n numbers (13 + 23 + … + n3)
def sumNcubes(n):
    # Same steps as in #2 but cube i before adding
    a=0
    for i in range(n+1):
        a += i**3
    # display results
    print(f"\nThe sum of all numbers from 1 to {n} cubed is: {a}\n")

# Question 4

# Write a program to ask the user for n and use the functions in part 2
# and 3 to print the sum of n numbers and sum of cubes of n numbers
def main():
    n = (input("\nPlease input in a number: "))
    # making function dummy proof, seeing if input is an int or not
    # run the functions you made in #1-3
    if n.isdigit():
        num = int(n)
        circleArea(num)
        sumN(num)
        sumNcubes(num)
    else:
        print("\nError. You have to type in a number. Please try again")
        n = input("Please input in a number: ")
        
    # asking if user wants to run function again
    ans = input("\nWould you like to run again [Y/N]? ")
    while ans.lower() != "y" and ans.lower() != "n":
        print("\nError. Recheck input.")
        ans = input("\nWould you like to run again [Y/N]? ")
    
    if ans.lower() == "y":
        main()
    else:
        print("Thank you. Have a great day!")
    

main()