class Book:
    def __init__(self,book_id:str,title:str,author:str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = True
        
    def borrow(self)->None:
        if self.is_borrowed == True:
            self.is_borrowed = False
    def return_book(self)->None:
        if self.is_borrowed == False:
            self.is_borrowed = True
class Member:
    def __init__(self,member_id:str,name:str) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        
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
        book = Book(book_id,title,author)
        self.books[book.book_id]= book
        
    def register_member(self, member_id:str, name: str)->None:
        member = Member(member_id,name)
        self.members[member.member_id] = member
    def borrow_book(self,member_id: str, book_id: str)->None:
        if member_id in self.members:
            if book_id in self.books:
                book = self.books.get(book_id)
            else:
                raise ValueError("Member not found")
            member = self.members.get(member_id)
        else:
            raise ValueError("Book not found")
        if book.is_borrowed == True:
            member.borrowed_books.append(book.title)
            book.is_borrowed = book.borrow()
        else:
            raise ValueError("Book is already borrowed")
                
    def return_book(self,member_id: str, book_id: str)->None:
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if book.title in member.borrowed_books:
            member.borrowed_books.remove(book.title)
            book.is_borrowed = False
        else:
            raise ValueError("Book not borrowed by this member")
            
    def get_borrowed_books(self,member_id:str)->list[Book]:
        if member_id in self.members:
            member = self.members.get(member_id)
            return member.borrowed_books
        else:
            raise ValueError("Member not found")
            
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

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))