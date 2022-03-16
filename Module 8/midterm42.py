# Write a parameterized function that takes in a file name as a parameter, reads the file, calculates the factorial of each number, and displays a formatted output as follows:

try:
    def nFactorial(fileName,nfactorial):
        if fileName.endswith(".txt"):
            name = fileName
        else:
            name = fileName+'.txt'
        # opening file and reading data in file and storing in a variable
        with open(name,'r') as data:
            for x in data:
                num = int(x)
                nfactorial = 1
                for i in range(num,0,-1):
                    nfactorial = nfactorial * i
                print(f"The factorial of {num} is: {nfactorial}")
        return nfactorial
                
        
    def main():
        # a.
        name = input("What is the name of your file? ")
        nfactorial = 1
        nFactorial(name,nfactorial)
    # run main
    main()
except ValueError:
    print("This file seems to contain more than just numbers. Please recheck if you chose the correct file.")
    main()
except FileNotFoundError:
    print("Error. Unable to find your file. Please recheck if you typed in the file name correctly and the file is the correct format (.txt)")
    main()
