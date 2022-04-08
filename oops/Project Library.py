class person:
    def __init__(self,coustemer,age):
        self.name=coustemer
        self.age=age 

    def eligblity(self):
        if int(self.age)>18:
            print("You are eligible to lend a book")
            return True
        else:
            print("you cannot lend the book")
            return False
            
class Library(person):
    def __init__(self,books,coustemer,age):
        self.books=books
        person.__init__(self,coustemer,age)

    def show_books(self):
        print("The List of Books in the Library are below : ")
        for index, i in enumerate(self.books):
            print("{} - {}".format(index,i))

    def lend_books(self):
        if person.eligblity(self):

            book_lend=input("Please enter the name of the book you need you need to lend : ")
            if book_lend in self.books:
                self.books.remove(book_lend)
                print("The book is lended to you please return back it carefully")
            else:
                print("Enter the valid book name")

    def return_book(self):
        book_return=input("please enter the name of the book you need to return : ")
        self.books.append(book_return)

    def remove_book(self):
        book_remove=input("Please enter the name of the book you need you need to remove from the library : ")
        if book_remove in self.books:
            self.books.remove(book_remove)
        else:
            print("Enter the valid book name")

    def add_book(self):
        book_add=input("please enter the name of the book you need to add to the library : ")
        self.books.append(book_add)

if __name__=="__main__": 

    books=Library(["html","css","python"],"Prakesh","19")
    while True:
        print(f"""-------------- Welcome to the Library ----------------------
                  print('''Please choose an option:
                               1. List all the books
                               2. Lend a book
                               3. Return a book
                               4. Remove a book from library
                               5. Add a book to the library """)
        choose=int(input("Enter the number you need : "))
        if (choose==1):
            books.show_books()
        elif (choose==2):
            books.lend_books()
        elif (choose==3):
            books.return_book()
        elif (choose==4):
            books.remove_book()
        elif (choose==5):
            books.add_book()
        condition=input("-----------Enter q to exist or c to continue ---------:")
        if condition=="q":
            print("Thanks for visiting the library")
            exit()
        elif condition=="c":
            pass
            
