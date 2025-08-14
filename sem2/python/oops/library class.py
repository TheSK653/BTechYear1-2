# You are tasked with implementing a simple library system using Python classes.
# Create a Book class with encapsulated attributes for the book's title, author, and ISBN.
# Include methods to display book information and check if the book is available or checked out.
# Create an object of the Book class and demonstrate its functionality.

class Book:
    def __init__(self,title,author,ISBN):
        self.title=title
        self.author=author
        self.isbn=ISBN
        self.checked_out=False
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nChecked Out: {'Yes' if self.checked_out else 'No'}\n")
    def availablity(self):
        print(f"The book '{self.title}' is{' not' if self.checked_out else ''} available.\n")
    def check_out(self):
        if self. checked_out:
            print("Sorry, the book is alreay checked out.\n")
        else:
            self.checked_out = True
            print(f"The book '{self.title}' is now checked out.\n")
    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"The book '{self.title}' has been checked in.\n")
        else:
            print("The book is not currently checked out.\n")

book1=Book('Berserk','Kentaro Miura',9781506711980)

book1.display_info()
book1.availablity()
book1.check_out()
book1.check_in()