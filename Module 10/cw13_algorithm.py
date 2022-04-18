import math
def main():
    # input a number x
    num = eval(input("Please input in a number: "))
    # create an empty list prime_list
    prime_list = []
    # create a outloop (use while loop) will iterate variable <i> from 2 to the given number x
    i = 2
    while i <= num:
        # set a boolean variable to assume i is prime (ex: is_prime=True)
        is_prime = True
        # Create Inner loop (for loop) from 2 to sqrt(i):
        for j in range(2,round(math.sqrt(i))+1):
            # i is a prime number if it cannot be divided by any number between 2 and sqrt of (i)
            # use modullus operator for division %
            if i % j == 0: 
                is_prime = False
                break
            # if i is not prime set is_prime = False 
        else:
            if is_prime is True: prime_list.append(i)
        # if i is prime then append i to prime_list
        # if is_prime == True:   
        i = i+ 1
    # show prime_list
    print(prime_list)
main()