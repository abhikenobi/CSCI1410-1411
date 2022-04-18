# Step 1
def read_data (file_name):
    """
    Function Name: read_data
    Description: Reads a set of numbers from an input file.
    Parameter: file_name - name of the input file
    Returns list of numbers
    """
    # checking to see if parameter has .txt in parameter
    if file_name.endswith(".txt"): file_name = file_name
    else: file_name = file_name+'.txt'
    # Initializing list
    list_of_numbers = []
    # Opening file
    with open(file_name) as file:
        data = file.read().split()
        # looping through file
        for line in data:
            # checking to see if line contains numbers
            # lstrip and replace lets negatives and floats be processed by isdigit function as True
            # only doing .replace once in case file has mulit-decimal things such as IP addresses
            if line.lstrip("+|-").replace(".","",1).isdigit() == False:
                list_of_numbers.append("NA")
                print("Non-numeric data detected.")
            else:
                # # checking to see if number is a float or int
                if "." in line:
                    list_of_numbers.append(float(line))
                else:
                    list_of_numbers.append(int(line))
    print("Extraction complete")
    return list_of_numbers
# Step 2
def compute_sum(numbersList):
    """
    Function Name: compute_sum
    Description: Calculates the sum of all numbers in a list
    Parameter: numbersList - the list of numbers (can be made using read_data if you have an input file)
    """
    # initialize counter
    total = 0
    for number in numbersList:
        total += number
    return total
# Step3
def compute_mean(numbersList):
    """
    Function Name: compute_mean
    Description: Calculates the mean of all numbers in a list
    Parameter: numbersList - the list of numbers (can be made using read_data if you have an input file)
    """
    # mean = sum/length
    # calculate sum using funciton from step 2
    total = compute_sum(numbersList)
    length = len(numbersList)
    mean = total/length
    return mean
# Step 4
def compute_sd(numbersList):
    """
    Function Name: compute_sd
    Description: Calculates the standard deviation of all numbers in a list
    Parameter: numbersList - the list of numbers (can be made using read_data if you have an input file)
    """
    # initialize variables and counters
    mean = compute_mean(numbersList)
    total = 0
    # loop through list to calcuate deviation
    for num in numbersList:
        dev = num - mean
        total += (dev**2)
    # sample size
    n = (len(numbersList) - 1)
    # calculate variance
    varaince = total / n
    # standard deviaton is the squrare root of the variance
    stdev = (varaince ** 0.5)
    return stdev
# Step 5
def write_results(outputFile, sum, mean, stdev):
    """
    Function Name: write_results
    Description: Calculates the standard of all numbers in a list
    Parameter: outputFile - name of the output file you want to write to (will create one if  file with name not found)
               sum - sum of numbers calculated by compute_sum() using numbers from an input file (use read_file to create list for sum, mean, and stdev)
               mean - mean of numbers calculated by calulated by compute_mean()
               stdev - standard deviation of numbers calculated by calculated by compute_sd()
    """
    # checks to see if file parameter has .txt ending or not
    if outputFile.endswith(".txt"): outputFile = outputFile
    else: outputFile = outputFile+'.txt'
    try:
        # opening file using write method
        file = open(outputFile, 'w')
        # using print with file parameter to write to output file
        file.write(f"Sum is: {sum:.2f}\n")
        file.write(f"Mean is: {mean:.2f}\n")
        file.write(f"Standard deviation is: {stdev:.2f}")
        # closing file after done
        file.close()
        print("Writing Complete.")
        print(f"Sum is: {sum:.2f}\nMean is: {mean:.2f}\nStandard deviation is: {stdev:.2f}")
    except:
        print("Error Detected. Please try again.")
# Step 6
def main():
    """
    Function Name: main
    Descriptions: Prompts user for an input and output file name. Uses read_data function to parse input file and generate a list of numbers which is then used in compute_sum, compute_mean, and compute_sd to calculate the sum, mean, and standard deviation. Then, the write_results function is called in order to write the findinds into the user-selected output file.
    Parameter: None
    """
    # prompt user for name of input and output files
    inputFile = input("What is the name of your input file? ")
    outputFile = input("What file would you like the program to output to? ")
    # assign any data created/calculated in Steps 1-4 to a function
    numList = read_data(inputFile)
    sum = compute_sum(numList)
    mean = compute_mean(numList)
    stdev = compute_sd(numList)
    # run Step 5
    write_results(outputFile, sum, mean, stdev)
def intro():
    print("Welcome to Lab 9")
    main()
intro()
