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


def main():
    print("This program calculates the future value")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    count = eval (input ("Enter number of year for investment: "))

    initial_year=0
    print ('Year    Value in $')
    print ('------------------------------')
    print (initial_year, '\t', principal)

    next_year = initial_year
    
    for i in range(count):
        next_year = next_year + 1
        principal = principal * (1 + apr)
        print(next_year, '\t', principal)

    print("The value in ", count, "years is: ", principal)



