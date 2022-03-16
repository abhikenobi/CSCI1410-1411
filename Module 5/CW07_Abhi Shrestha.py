# Classwork 07
# Name: Abhinav Shrestha

# Problem Set 1
# Show the string that would result from each of the following formatting operations:
def question1():
    # Print each string statement from Question 1
    print("Number 1:")
    print("\nLooks like {1} and {0} for breakfast".format("eggs","spam"))

    print("\nNumber 2:")
    print("\nThere is {0} {1} {2} {3}".format(1, "spam", 4, "you"))

    print("\nNumber 3:")
    print("\nHello {0}".format("Susan", "Compuwell"))

    print("\nNumber 4:")
    print("\n{0:0.2f} {0:0.2f}".format(2.3, 2.3468))

    print("\nNumber 5:")
    # print("{7.5f} {7.5f}".format(2.3, 2.3468))
    print("\nIndexError: Replacement index 7 out of range for positional args tuple")
    print("\nIncorrect Syntax, the string is missing a `:` between the index and format specifier")
    print("\nAlso there are only 2 values in the format parameters, Index 7 would be looking for the 8th value in the list.")

    print("\nNumber 6:")
    print("\nTime left {0:02}:{1:05.2f}".format(1, 37.374))

    print("\nNumber 7:")
    # print("{1:3}".format("14"))
    print("\nIndexError: Replacement index 1 out of range for positional args tuple")
    print("\nThe print statement is looking for index 1 when there is only one item. It should be index 0.")

    main()

def question2():
    # Copy over futval.py code and make necessary changes
    
    # futval.py
    #    A program to compute the value of an investment
    #    carried 10 years into the future

    # expected output format example:
    # ========================
    # Enter the initial principal: 34000.45
    # Enter the annual interest rate: 3.56
    # Enter number of year for investment: 4
    # Year    Value
    # ---------------
    # 0    $ 34000.45
    # 1    $ 155042.05
    # 2    $ 706991.76
    # 3    $ 3223882.41
    # 4    $ 14700903.80
    # The value in 4 years is: $ 14700903.80
    
    print("This program calculates the future value")

    principal = eval(input("Enter the initial principal: $ "))
    apr = eval(input("Enter the annual interest rate (APR): "))
    count = eval (input("Enter number of year(s) for investment: "))

    initial_year=0
    print (f'\nYear \t Value in $')
    print ('------------------------------')
    # Added an int() incase the user inputted a decimal changed to f"" string and formatted to 2 decimal points
    print (f"{int(initial_year)} \t $ {principal:.2f}")

    next_year = initial_year
    
    for i in range(count):
        next_year += 1
        principal = principal * (1 + apr)
        # changed to f"" string and formatted to 2 decimal points
        print(f"{next_year} \t $ {principal:.2f}")

    # changed to f"" string and formatted to 2 decimal points
    print(f"The value in {count} years is: $ {principal:.2f}")

    main()


def main():

    print(f"\n\n\n                     Welcome to Classwork 7                    \n")
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
