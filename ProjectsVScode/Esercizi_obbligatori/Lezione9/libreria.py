class Book:
    def __init__(self,book_id:str,title:str,author:str,is_borrowed:bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    def borrow(self)->None:
        if self.is_borrowed == True:
            self.is_borrowed = False
    def return_book(self)->None:
        if self.is_borrowed == False:
            self.is_borrowed = True
class Member:
    def __init__(self,member_id:str,name:str,borrowed_books:list[Book]) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books
        
    def borrow_book(self,book:Book)->None:
        if book.is_borrowed == True:
            self.borrowed_books.append(book)
    def return_book(self,book:Book)->None:
        if book.is_borrowed == False:
            self.borrowed_books.remove(book)
class Library:
    def __init__(self) -> None:
        self.books:dict[str, Book] = {}
        self.members:dict[str, Member] = {}
        
    def add_book(self,book_id:str,title:str,author:str)->None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.books[book_id] = [title,author]
        
    def register_member(self, member_id:str, name: str)->None:
        self.member_id = member_id
        self.name = name
        self.members[member_id] = [name]
    def borrow_book(self,member_id: str, book_id: str)->None:
        if member_id in self.members.items():
            if book_id in self.books.items():
                self.rimosso = self.books.pop(book_id)
                self.assegno =[member_id,self.rimosso]
                
    def return_book(self,member_id: str, book_id: str)->None:
        if member_id in self.member_id:
            self.members[book_id] = [self.rimosso.title,self.rimosso.author]
            
    def get_borrowed_books(self,member_id:str)->list[Book]:
        prestito:list = []
        self.borrow_book(member_id,self.book_id)
        prestito.append[self.title]
        return prestito
            
library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']
        