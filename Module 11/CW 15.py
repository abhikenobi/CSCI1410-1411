# Student.py
# Student class to keep track of student record
class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints
    
    def gpa(self):
        return self.qpoints/self.hours
    
    def addGrade(self, gradePoints, credits):
        self.qpoints += float(gradePoints * credits)
        self.hours += float(credits)
def main():
    # welcome message
    print("Hello! Welcome to the GPA calculator.\n")
    # prompt user for name
    studentName = input("What is your name? ")
    # create student object
    s = Student(studentName, 0, 0)
    # create loop to ask for grades
    # while loop condition
    cont = True
    while cont is True:
        # prompt user for credit hours
        studentCredits = input("How many credits was the class? ")
        while studentCredits.isnumeric() is False:
            print("Error. Incorrect input detected. Please try again.")
            studentCredits = input("How many credits was the class? ")
        else:
            studentCredits = float(studentCredits)
        # prompt user for class grades
        studentGrade = input("What grade/gradePoint did you get in the class? ")
        # try turning string into float
        if studentGrade.replace(".","",1).isdigit() is True:
            studentGrade = float(studentGrade)
            # add to student object
            s.addGrade(studentGrade,studentCredits)
        # if user input grades in letter grade format instead
        else:
            # possible grades
            grades = ["A","B","C","D","F","I"]
            # checks if input was a letter grade or something else
            while studentGrade.rstrip("+|-").upper() not in grades:
                print("Error detected. Please try again")
                studentGrade = input("What grade/gradePoint did you get in the class? ")
            else:
                if studentGrade.upper() == "A":
                    s.addGrade(4.0, studentCredits)
                elif studentGrade.upper() == "A-":
                    s.addGrade(3.7, studentCredits)
                elif studentGrade.upper() == "B+":
                    s.addGrade(3.3, studentCredits)
                elif studentGrade.upper() == "B":
                    s.addGrade(3.0, studentCredits)
                elif studentGrade.upper() == "B-":
                    s.addGrade(2.7, studentCredits)
                elif studentGrade.upper() == "C+":
                    s.addGrade(2.3, studentCredits)
                elif studentGrade.upper() == "C":
                    s.addGrade(2.0, studentCredits)
                elif studentGrade.upper() == "C-":
                    s.addGrade(1.7, studentCredits)
                elif studentGrade.upper() == "D+":
                    s.addGrade(1.3, studentCredits)
                elif studentGrade.upper() == "D":
                    s.addGrade(1.0, studentCredits)
                elif studentGrade.upper() == "D-":
                    s.addGrade(0.7, studentCredits)
                elif studentGrade.upper() == "F" or studentGrade.upper() == "I":
                    s.addGrade(0, studentCredits)
        # ask to if they'd like to continue adding grades
        ans = input("Do you have more classes & grades to add [y/n]? ")
        answers = ["yes","no","y","n"]
        while ans.lower() not in answers:
            print("Error detected please try again")
            ans = input("Do you have more classes & grades to add [y/n]? ")
        else:
            if ans.lower() == "yes" or ans.lower() == "y":
                cont = True
            else:
                cont = False
    # Display results
    print(f"Based on your input {s.getName()}, these are your results:")
    # rount gpa to 2 decimal points
    print(f"GPA: {s.gpa():.2f}")
    print(f"Total Credit Hours: {s.getHours()}")
    print(f"Total Quality Points: {s.getQPoints()}")
main()