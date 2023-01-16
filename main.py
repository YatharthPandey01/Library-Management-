class Library: # masde a class library
    def __init__(self,listofbooks): # defined a constructor here with a [list] of books using self
        self.books=listofbooks

    def DisplayAvailableBooks(self): # defined a function to display available books
        print("Books present in the library are :")
        for book in self.books: # used a for loop to print books in list of books {self.books=listofbooks}
            print(f"\t* {book}") # finally printed the book name

    def BorrowBook(self,bookname): # defined a function to borrow a book from the library
        if bookname in self.books: # used an if else condition to check whether the book is available or not
            print(f"\t \nYou have been issued the book '{bookname}'. Happy reading and dont forget to return it on time. Cheers!!")
            self.books.remove(bookname)
            return True
        elif bookname !=self.books:
            print(" \n You have entered a wrong book name. Please enter it again")
        else:
            print(f"Sorry, this book #{bookname} has been issued to someone else.\n Goodluck finding another one")
            return False

    def ReturnBook(self,bookname): # used a return book function here to return the book 
        self.books.append(bookname) # used .append here so that the book which is returend should be appended back in the list 
        print(F"Thanks for returning the book #{bookname}. Hope you enjoyed")




  

class Student: # made a class student
    def reqBook(self): # used a request book function here so that a student can request a book 
        self=input("Please Enter the book you want to borrow : ")
        return self
    def returnBook(self): # similarly used a return book function here so that a student can return a book 
        self=input("Please Enter the book you want to return : ")
        return self

if __name__=="__main__":
    BiasLibrary=Library(["Python notes","c++ by harry","The night we met","Kingdom of dreams","Django"]) # defined or 
    #assigned an object here to the class Library

    student1=Student()

    while(True): # used an infinite loop here 
        welcomemessage=''' \n****** WELCOME TO THE BIAS LIBRARY ******
        Please choose an option 
        1) Display the list of books
        2) Borrowing a book 
        3) returning a book
        4) To quit the Bias library platform
        '''
        print(welcomemessage) # printed the welcome message

        a=int(input("Please enter your choice \n")) # took a user input here to enter the choice 
        if a==1:
            BiasLibrary.DisplayAvailableBooks()
        elif a==2:
            BiasLibrary.BorrowBook(student1.reqBook())
        elif a==3:
            BiasLibrary.ReturnBook(student1.returnBook())
        elif a==4:
            print("Thanks for choosing the Bias Library ")
            exit()
        else:
            print("You Have entered a wrong choice")





    
