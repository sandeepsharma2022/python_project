# we age going to develop Library Management software 
class Library:
     def __init__(self,booklist,name):
      self.booklist=booklist
      self.name=name
      self.lendDict={}


     def displayBooks(self):
       print(f"we have following books in our library:{self.name}")
       for book in self.booklist:
         print(book)



     def lendBook(self,book,user):
       if book in self.booklist:
         if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book has been borrowed and database updated!")

         else:
            print(f"book already used by {self.lenDict[book]}")

       else:
          print("Apologise! we don't have this book in our library currently")




     def addBook(self,book):
       if book in self.booklist:
         print("book already exist in library!")
    
       else:
         self.booklist.append(book)
         bookdatabase=open(databaseName,'a')
         bookdatabase.write("\n")
         bookdatabase.write(book)
         print("Book added successfully!")


     def returnBook(self,book):
       if book in self.lendDict.keys():
          self.lendDict.pop(book)
          print("Book returned successfully")

       else:
          print("Book does not exist in lending database or you have not browwed the book")




def main():
    while(True):
        print(f"Welcome to the {library.name} library. Following are the options:")

        choice='''
        1:Display Book
        2:Lend Book
        3:Add a Book
        4:Return a Book
        '''

        print(choice)

        userInput=input("Press Q to Quit and C to Continue:")
        if userInput=="C":
            enterChoice=int(input("Select a option to continue:"))
            if enterChoice==1:
                library.displayBooks()
            elif enterChoice==2:
                book=input("Enter the book name you want to borrow: ")
                user=input("Enter the your user name:")
                library.lendBook(book,user)
            elif enterChoice==3:
                book=input("Enter the book nam eyou want to add into library:")
                library.addBook(book)
            elif enterChoice==4:
                book=input("Enter the book you want to return:")
                library.returnBook(book)
            else:
                print("please choice a valid option:")
        elif userInput=="Q":
            print("thank you!")
            break
        else:
            print("please enter the valid option")



if __name__=='__main__':
    booklist=[]
    databaseName=input("Enter the nam eof database file with the extension:")
    bookdatabase=open(databaseName,'r')

    for book in bookdatabase:
        booklist.append(book)
    library=Library(booklist,"AccurateStore")
    main()