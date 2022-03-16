# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    count = eval (input ("Enter number of year for investment: "))

    print ('Yea', 'Value')
    print ('--------------------------')
    print ('0', principal)

    for i in range(count):
        principal = principal * (1 + apr)
        print ((i+1),principal)

    print("The value in 10 years is:", principal)

main()
