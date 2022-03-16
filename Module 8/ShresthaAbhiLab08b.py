# Abhi Shrestha
# 3/16/22
# Convert date from mm/dd/yyyy to month day and year (01/03/2022 = January 3, 2022)
# Write function dateConvert that will take a date in mm/dd/yyyy format as parameter and return the date in Month Day, Year format
def dateConvert(date):
    # use split to split mm/dd/yyyy using / as parameter
    dateSplit = date.split("/")
    month = dateSplit[0]
    day = dateSplit[1]
    year = dateSplit[2]
    # conver mm into month using conditionals
    if month == "1" or month == "01": month = "January"
    elif month == "2" or month == "02": month = "February"
    elif month == "3" or month == "03": month = "March"
    elif month == "4" or month == "04": month = "April"
    elif month == "5" or month == "05": month = "May"
    elif month == "6" or month == "06": month = "June"
    elif month == "7" or month == "07": month = "July"
    elif month == "8" or month == "08": month = "August"
    elif month == "9" or month == "09": month = "September"
    elif month == "10": month = "October"
    elif month == "11": month = "Novemeber"
    else: month = "December"
    # put it all back together
    convertedDate = month+" "+day+", "+year
    # display result
    print(convertedDate)
    return convertedDate

def main():
        # prompt user for date
        date = input("Please enter a date (mm/dd/yyyy): ")
        # call up dateConvert funciton to convert the date into Month Day, Year format
        dateConvert(date)
# Using try except clauses in case user input results in error of somekind
try:
    main()
except:
    # When error happens prompt user to use correct date format and restart program
    print("Error. Please try again. Try entering the date in mm/dd/yyyy format")
    main()

    
