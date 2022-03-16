# CW 05 Solutions
# Abhi Shrestha

#question 1
def question1():

    s1 = "spam"
    s2 = "ni!"

    a1 = s1*3+2*s2
    a2 = s1[1]
    a3 = s1+s2[-1]
    print("Question 1")
    print(a1)
    print(a2)
    print(a3)

    main()

#question 2
def question2():
    for ch in "aardvark":
        print(ch)
    main()

#question 3
#I was attempting to make a self looping score calculator
def testScore():
    score = int(input("What is the quiz score you want to grade? "))

    while score > 5:
        print("The quiz was scaled from 0-5 points only. Please recheck your input.")
        score = int(input("What is the quiz score you want to grade? "))

    if score > 4 and score <= 5:
        print(f"You input {score} points as your score. The grade is: A")
    elif score < 5 and score >= 4:
        print(f"You input {score} points as your score. The grade is: B")
    elif score < 4 and score >= 3:
        print(f"You input {score} points as your score. The grade is: C")
    elif score <3 and score >= 2:
        print(f"You input {score} points as your score. The grade is: D")
    else:
        print(f"You input {score} points as your score. The grade is: F")


    con = input("Would you like to continue to the next question [Yes] or [No]? ")
    while con != "Yes" and con != "No":
        print("Error. Recheck spelling and capitalization of your answer.")
        con = input("Would you like to continue to the next question [Yes] or [No]? ")
    if con == "Yes":
        main()
    elif con == "No":
        testScore()


def main():
    print("What solution would you like to view?")
    print("Type [one] for question 1, [two] for question 2, and [three] for quesiton 3.")
    ans = input("Which question would you like to see? ")

    while ans != "one" and ans !="two" and ans != "three":
        print("Error. Please recheck input.")
        ans = input("Which question would you like to see? ")
        if ans == "one":
            question1()
        elif ans == "two":
            question2()
        elif ans == "three":
            testScore()

    if ans == "one":
        question1()
    elif ans == "two":
        question2()
    elif ans == "three":
        testScore()


main()
    
