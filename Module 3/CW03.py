# Name: Abhi Shrestha
# Table of Contents
# Use these functions to see the answers
# 1. question1()
# 2. question2()
# 3. bikeShop()
# 4. changeCalculator()

# Question 1

def question1():
    # 1. range(5)
    print("1. range(5) would generate the following numbers: ")
    for i in range(5):
        print(i)
    print(" ")

    # 2. range(3, 10)
    print("2. range(3, 10) would generate the following numbers: ")
    for i in range(3, 10):
        print(i)
    print(" ")

    # 3. range(4, 13, 3)
    print("3. range(4, 13, 3) would generate the following numbers: ")
    for i in range(4, 13, 3):
        print(i)
    print(" ")

    # 4. range (15, 5, -2)
    print("4. range(15, 5, -2) would generate the following numbers: ")
    for i in range(15, 5, -2):
        print(i)
    print(" ")


    # 5. range (5, 3)
    print("5. range(5, 3) would generate the following numbers: ")
    for i in range(5, 3):
        print(i)
    print("The step is not specified as -1, therefore, nothing will print.")
    print(" ")

    #6. range (1, 10, -1)
    print("6. range(1, 10, -1) would generate the following numbers: ")
    for i in range(1, 10, -1):
        print(i)
    print("The step is -1 but the start step is less than end step, so nothing will print.")

    main()

# Question 2

def question2():
    print("4 π r2 in python code can be translated to: 4*(math.pi)*(r**2)")

    main()

# Qestion 3

def bikeShop():
    # initial variables
    costHelmets = 50
    costBikes = 250

    # ask for number of bikes sold
    bikes = eval(input("How many bikes do you expect to sell this month? "))

    # 1 helmet sold for every 5 bikes sold, calculate given input bike sales
    helmets = bikes // 5

    # calculate total expected revenue
    revenue = (bikes*costBikes) + (helmets*costHelmets)

    # print out your results/findings
    print(f"Given that you expect to sell {bikes} bike(s) over the course of next month,")
    print(f"You can expect to sell {helmets} helmet(s) as well.")
    print(f"And since bikes cost $250 and helmets $50, ")
    print(f"The total revenue would then be: ${bikes*costBikes} + ${helmets*costHelmets} equalling ${revenue}")

    main()

# Question 4

def changeCalculator():
    # ask for the amount of change owed to customer
    change = eval(input("How many cents is owed to the custormer? "))

    # calculate number of coins
    quarters = change // 25
    remainder1 = change % 25
    dimes = remainder1 // 10
    remainder2 = remainder1 % 10
    nickels = remainder2 // 5
    pennies = remainder2 % 5

    # Print results
    print(f"Given your input, the customer is owed {change} cents")
    print(f"Hand out {quarters} quarters with {remainder1} cents remaining")
    print(f"Hand out {dimes} dimes with {remainder2} cents remaining")
    print(f"Hand out {nickels} nickels with {pennies} cents remaining")
    print(f"Hand out {pennies} pennies")

    main()

def main(): 
    print("Table of Contents")
    print("------------------")
    print("1. question1() ")
    print("2. question2() ")
    print("3. bikeShop() ")
    print("4. changeCalculator() ")

main()
