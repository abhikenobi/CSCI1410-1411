# A program to convert temperature values in Celsius to Farenheit
def convTemp():
    # Display/Ask for the temp. in Celsius
    celsius = eval(input("What is the temperatue in Celsius? "))

    #Take input celsius and covert to farenheit
    farenheit = (9/5)*celsius + 32

    #Display farenheit as output
    print(f"The temperature is: {farenheit} degrees Farenheit")

