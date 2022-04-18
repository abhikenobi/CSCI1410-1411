from tkinter.messagebox import QUESTION


# Classwork 11
# Name: Abhi Shrestha
# Separated the Heading from main function so it wouldn't print each time
def intro():
    print("--------------------------Classwork 11--------------------------")
    main()
# Put anything necessary for solution selection within main to run/repeat
def main():
    print("Please pick the question number to see the solution")
    option = input("Which solution would you like to see [1], [2], or [3]? ")
    while option not in ["1","2","3"]:
        print("Please recheck your input.")
        print("Please pick the question number to see the solution")
        option = input("Which solution would you like to see [1], [2], or [3]? ")
    else:
        if option == "1":
            question1()
        elif option == "2":
            question2()
        else:
            question3()
def question1():
    print("\nQuestion 1\n")
    print("For the follwoing code:\nnum = 87\nmax = 25\n\tif (num >= max*2):\n\tprint('apple')")
    print("print('orange')\nprint('pear')\n")
    print("The code will output 'apple', 'orange', and 'pear' in the terminal because the condition of the if statement is met. The num variable (87) is greater than the max (25) * 2. If the condition was not met, the code would only output 'orange' and 'pear' to the terminal and not 'apple'.\n")
    main()
def question2():
    print("\nQuestion 2\n")
    print("For the following code:\nif (length = min_length):\n\tprint('The length is minimal')\n")
    print("There are multiple errors. First the two variables, length and min_length are not assigned any values. Also the syntax of the if statement is incorrect. The = sign is used to assign values to a variable. To show equality between 2 values/variables, a == needs to be used which will result in a boolean.\n")
    main()
def question3():
    print("\nQuestion 3\n")
    # Prompt user for hours worked this week
    totalHours = eval(input("How many hours did you work this week? "))
    hourlyRate = eval(input("How much are you paid per hour? $"))
    # Caculate total wages for the week
    # OT = 1.5 (time and a half)
    totalWage = 1
    overtimeRate = 1.5 * hourlyRate
    # if user didn't work any overtime
    if totalHours <= 40:
        totalWage = totalHours * hourlyRate
    # if user worked any overtime (hours > 40)
    else:
        totalWage = (40*hourlyRate) + ((totalHours-40)*overtimeRate)
    # display results
    print(f"Since you worked {totalHours} hours this week and are paid ${hourlyRate} per hour, your total pay (including overtime) this week will be: ${totalWage:.2f}.\n")
    main()
intro()