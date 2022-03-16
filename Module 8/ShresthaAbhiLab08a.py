# Abhi Shrestha
# Date: 3/16/22
# Description: This program shows techniques of defining function, parameter passing and function invocation

# fahrenheit to celsius function
# parameter: A temperature value in Fahrenheit
# returns equivalent temperature in Celsius
def fahrenToCel(fahren):
    result = (fahren - 32) * (5.0/9.0)
    return result

# fahrenToCelList function
# parameter: a list of temperature values in Fahrenheit
# coverts the list to equivalent temperatures in Celsius
# If you pass a list as an argument, this will change the value in calling function
def fahrenToCelList(fahrenList):
    for i in range(len(fahrenList)):
        fahren = fahrenList[i]
        celsius = (fahren -32)*(5.0/9.0)
        fahrenList[i] = round(celsius, 2)

# main function
def main():
    fval = float(input("Please enter the temperature in Fahrenheit: "))
    # call fahrenToCel function
    cval = fahrenToCel(fval)
    print("The equivalent temperature in Celsius is {0:0.2f}".format(cval))
    
    fahrenheitList = []
    # Take 5 temperature as inputs and store them in fahrenheitList
    for i in range(5):
        fahren = float(input("Enter a temperature in Fahrenheit: "))
        fahrenheitList.append(fahren)
    # call fahrenToCelList function
    fahrenToCelList(fahrenheitList)
    print("The converted temperature list")
    print(fahrenheitList)

main()