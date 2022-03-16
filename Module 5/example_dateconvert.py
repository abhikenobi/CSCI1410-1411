# dateconvert.py
#    Converts a date in form "mm/dd/yyyy" to "month day, year" 

def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    # indexes      [0]           [1]                [2]           [3]        [4]        [5]      [6]         [7]               [8]                  [9]             [10]              [11]         
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)
    

main()
