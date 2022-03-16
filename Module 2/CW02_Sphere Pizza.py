# Write a program to calculate the volume and surface area of a sphere from its radius, given as an input
# Import necessary libraries
import math

# Define pi using the math library
pi = math.pi


def sphereStats():

    # Ask for the radius as an input
    radius = eval(input("What is the radius of your sphere? "))

    # Calculate the volume
    volume = (4*pi*(radius**3))/3

    # Calculate the surface area
    surfaceArea= (4*pi*(radius**2))

    # Print your results
    print(f"Given the radius, {radius}")
    print(f"The volume of the sphere would be: {round(volume, 3)} units cubed")
    print(f"The surface area of the sphere would be: {round(surfaceArea, 3)} units squared")

    main()


# Write a program to calculate cost per square inch of a circular pizza given it's diameter and price

def pizzaCost():

    # Ask for the diameter of the pizza
    diameter = eval(input("What is the diameter of the pizza you ordered in inches? "))

    # Ask for the price of the pizza
    price = eval(input("How many dollars did you pay for the pizza? $ "))

    # Calculate the radius from the diameter
    radius = diameter/2

    # Calculate the area of the pizza
    area = (pi*(radius**2))

    # Calculate cost per square inch
    cost = price/area

    # Print results
    print(f"Given that you bought a {diameter} in. pizza for ${price}")
    print(f"The cost per square inch was: ${round(cost, 2)} dollars per square inch")

    main()

def main():
    print("Would you like the [Sphere Stats] or [Pizza Calculator]?")
    ans = input("Type [1] for Sphere Stats and [2] for Pizza Calculator: ")

    while ans != "1" and ans != "2":
        print("Error. Please recheck input")
        ans = input("Type [1] for Sphere Stats and [2] for Pizza Calculator: ")
    else:
        if ans == "1":
            sphereStats()
        elif ans == "2":
            pizzaCost()

main()
    
