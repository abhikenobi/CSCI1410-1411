# Find the error and fix
# def addInterest(balance, rate):
#     newBalance = balance * (1+rate)
#     balance = newBalance
# def test():
#     amount = 1000
#     rate = 0.05
#     print("Amount before call addInterest = ", amount)
#     addInterest(amount, rate)
#     print("Amount after call addInterest = ",amount)
# test()

# Solution 1
# def addInterest(balance, rate):
#     newBalance = balance * (1+rate)
#     balance = newBalance
#     return balance
# def test():
#     amount = 1000
#     rate = 0.05
#     print("Amount before call addInterest = ", amount)
#     print("Amount after call addInterest = ",addInterest(amount, rate))
# test()

# Solution 2
# def addInterest(balance, rate):
#     newBalance = balance * (1+rate)
#     balance = newBalance
#     print("Amount after call addInterest = ",balance)
# def test():
#     amount = 1000
#     rate = 0.05
#     print("Amount before call addInterest = ", amount)
#     addInterest(amount, rate)
# test()

# Solution 3
def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    balance = newBalance
    return balance
def test():
    amount = 1000
    rate = 0.05
    balance = addInterest(amount, rate)
    print("Amount before call addInterest = ", amount)
    print("Amount after call addInterest = ", balance)

