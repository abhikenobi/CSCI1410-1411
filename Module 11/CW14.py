"""
Classwork 14
Name: Abhi Shrestha
Date: 4/14/2022

Write a class to represent a square. It must be able to store its size and contain the following functions:
    - getArea
    - getSize
    - getPerimeter
Write a class to represent a book. 
    Data to keep track of:
    - author
    - title
    - publisher
    (Include and set methods for each of the instance variables)

"""
class Square:
    def __init__(self, size):
        self.size = eval(size)
    def getArea(self):
        return (self.size**2)
    def getSize(self):
        return self.size
    def getPerimeter(self):
        return(4*self.size)
class Book:
    def __init__(self, author, title, publisher):
        self.author = author
        self.title = title
        self.publisher = publisher
    def getAuthor(self):
        return self.author
    def getTitle(self):
        return self.title
    def getPublisher(self):
        return self.publisher
def squareMaker():
    units = input("What is the unit of measurement you are using? ")
    side = input("What is the length of the sides of your square (without the unit)? ")
    while side.replace(".","",1).isdigit() == False:
        print("Error Detected. Please try again.")
        side = input("What is the length of the sides of your square (without the unit)? ")
    else:
        s = Square(side)
        size = s.getSize()
        area = s.getArea()
        perimeter = s.getPerimeter()
        print("-------------------Square Statistics-------------------")
        print(f"The length and size of your square: {size} {units}")
        print(f"The area of your square: {area} {units} squared")
        print(f"The perimeter of your square: {perimeter} {units}")
        main()
def bookList():
    cont = True
    authors = []
    titles = []
    publishers = []
    while cont is True:
        author = input("Who is the author of the book? ")
        title = input("What is the title of the book? ")
        publisher = input("Who is the publisher of the book? ")
        book = Book(author,title,publisher)
        authors.append(book.author)
        titles.append(book.title)
        publishers.append(book.publisher)
        ans = input("Do you have any more books left [Y/N]? ")
        answers = ["y","yes","no","n"]
        while ans.lower() not in answers:
            print("Invalid input detected please try again")
            ans = input("Do you have any more books left [Y/N]? ")
        else:
            if ans == "y" or ans == "yes":
                cont = True
            else:
                cont = False
    else: print("Program ending ...")
def main():
    inp = input("Press [1] for square maker or [2] to make a book list: ")
    while inp != "1" and inp != "2":
        print("Invalid input detected. PLease try again")
        inp = input("Press [1] for square maker or [2] to make a book list: ")
    else:
        if inp == "1":
            squareMaker()
        else:
            bookList()
main()