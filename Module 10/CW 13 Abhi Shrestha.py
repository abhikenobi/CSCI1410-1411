# Name: Abhi Shrestha
# Classwork 13
# Date: 3/31/22
def isPositive(number):
    try:
        # checks if input has just numerical digits, filters any letters, symbols, and decimals.
        if number.lstrip("+|-").isdigit() == False: return False
        else: 
            # checks to see if input is posititve or negative
            if "-" not in number and number > "0": 
                return True
    except:
        # incase of any unforseen errors
        print("Error. Please try again")
        main()
def primeList(x):
    # positive number n > 2 is prime if no number between 2 and √n(inclusively) evenly divides n
    numList = []
    for num in range(2,x+1):
        # finding the √n and rounding for for loop
        nRoot = round(num**0.5)
        for i in range(2,nRoot+1):
            # checks what numbers between 2 and √n is a factor of n
            if (num % i) == 0: break
            # prime number factors should only be itself and 1, so any other modulo should be non-zero values
        else: numList.append(num)
    return numList
def main():
    # prompt user for number input
    num = input("Please input a postive integer: ")
    # run through to check if num is positive
    positve = isPositive(num)
    while positve == False:
        print("Error. Nonnumerical/Negative/Float input detected. Please try again")
        num = input("Please input a postive integer: ")
        positve = isPositive(num)
    else:
        num = (int(num))
        if num > 2:
            numList = primeList(num)
            print(f"These are all the prime numbers between 2 and {num}: ")
            print(numList)
        elif num == 2:
            print(f"Your input: 2 is the lowest prime number.")
        else:
            print("Your input does not meet the criteria of a prime number. A prime number must be greater than 2")
    ans = input("Would you like to rerun the program [y/n]? ")
    if ans.lower() == "y" or ans.lower() == "yes":
        main()
    else:
        thankMessage = """                                                                         
        ███▀▀██▀▀███ ██                          ▀███          ▀███▀   ▀██▀                   ██ 
        █▀   ██   ▀█ ██                            ██            ███   ▄█                     ██ 
             ██      ███████▄  ▄█▀██▄ ▀████████▄   ██  ▄██▀       ███ ▄█    ▄██▀██▄▀███  ▀███ ██ 
             ██      ██    ██ ██   ██   ██    ██   ██ ▄█           ████    ██▀   ▀██ ██    ██ ██ 
             ██      ██    ██  ▄█████   ██    ██   ██▄██            ██     ██     ██ ██    ██ ▀▀ 
             ██      ██    ██ ██   ██   ██    ██   ██ ▀██▄          ██     ██▄   ▄██ ██    ██ ▄▄ 
           ▄████▄   ████  ████▄████▀██▄████  ████▄████▄ ██▄▄      ▄████▄    ▀█████▀  ▀████▀███▄█
                                                                                
        """
        print(thankMessage)
        print("\nHave a Great Day!")
main()
