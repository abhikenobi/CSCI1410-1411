"""
Name: Abhi Shrestha
Date: 4/7/2022
This program will perform the following:
- Take in an input of the number of packages purchased and then:
    - Display the discount percentage (with % sign after the value)
    - Amount of the discount (with $ sign)
    - Total cost of purchase after discount is applied (with $ sign)
"""
import numbers


def main():
    q = input("What is the number of packages you purchased? ")
    number = isNumber(q)
    while number is False:
        print("Error. Non-numerical, negative, or decimal values detected. Input should be a positive integer. Please try again")
        q = input("What is the number of packages you purchased? ")
        number = isNumber(q)
    else:
        # price per package
        cost = 99
        # number of packages purchased
        qty = int(q)
        # discount rate based on how many packages purchased
        discountRate = findDiscount(qty)
        # subtotal amount (pre discount)
        amount = qty * cost
        # amount of discount in dollars
        discountAmount = amount * discountRate
        # total after applying discount
        totalAmount = amount - discountAmount
        # display results
        print(f"For purchasing {qty} packages, you were given a {(discountRate*100):.2f}% discount dropping your total to ${totalAmount:.2f} saving you ${discountAmount:.2f}.")
        print(f"Quantity: {qty}")
        print(f"Discount Percentage: {(discountRate*100):.2f}%")
        print(f"Dicount Amount: ${discountAmount:.2f}")
        print(f"Sub-total Amount (without Discount): ${amount:.2f}")
        print(f"Total Amount (after Discount): ${totalAmount:.2f}")
    
def isNumber(x):
    """
    Function Name: isNumber
    Parameters: a string value
    Description: 
        Function takes in a string value (x) and then checks to see if the string would be a positive whole number. This eliminates strings with any negative numbers, decimals, or non-numerical characters.
        Returns a True or False Boolean result
    """
    try:
        # checks if input has just numerical digits, filters any letters, symbols, and decimals.
        if x.lstrip("+|-").isdigit() == False: return False
        else: 
            # checks to see if input is posititve or negative
            if "-" not in x and x > "0": 
                return True
    except:
        # incase of any unforseen errors
        print("Error. Please try again. P.S. Input must be a positive whole number.")
        main()
def findDiscount(y):
    """
    Function Name: findDiscount
    Description: Takes in an integer and returns a discount percentage. Returns a float value of the discount.
    Parameter: an integer
    """
    if y >= 100:
        discount = 0.50
    elif y >= 50:
        discount = 0.40
    elif y >= 20:
        discount = 0.30
    elif y >= 10:
        discount = 0.20
    else:
        discount = 0.00
    
    return discount
main()