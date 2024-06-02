class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Titolo: {self.title}, Autore: {self.author}, ISBN: {self.isbn}"

    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(", ")
        return cls(title, author, isbn)

class Member:
    def __init__(self,name:str, member_id:str):
        self.name = name
        self.member_id = member_id
        self.borrowed_book:list[Book] = []

    def borrow_book(self, book:Book):
        if book in self.borrowed_book:
            print("Questo libro è già stato preso in prestito.")
        else:
            self.borrowed_book.append(book)
    def return_book(self, book:Book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
        else:
            print("Il libro non è stato preso in prestito da questo membro.")

    def __str__(self) -> str:
        return f"Nome: {self.name}, ID: {self.member_id}"
    @classmethod
    def from_string(cls, member_str):
        name, member_id = member_str.split(", ")
        return cls(name, member_id)

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.total_books = 0

    def add_book(self,book:Book):
        if book in self.books:
            print("Questo libro è già presente nella biblioteca.")
        else:
            self.books.append(book)
            self.total_books += 1
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            self.total_books -= 1
        else:
            print("Questo libro non è presente nella biblioteca.")

    def register_member(self, member:Member):
        if member in self.members:
            print("Questo membro è già registrato nella biblioteca.")
        else:
            self.members.append(member)
    def lend_book(self,book, membro):
        if membro in self.members:
            if book in self.books:
                membro.borrow_book(book)
                print(f"Il libro {book} è stato preso in prestito da {membro}.")
            else:
                print("Questo libro non è presente in bibbloteca.")
        else:
            print("Questo membro non è registrato nella biblioteca.")

    def __str__(self) -> str:
        elenco = ""
        for book in self.books:
            elenco += str(book) + "\n"

        elenco_m = ""
        for member in self.members:
            elenco_m += str(member) + "\n"

        return f"La biblioteca contiene {self.total_books} libri e {len(self.members)} membri.\nCatalogo libri:\n{elenco}\nLista membri:\n{elenco_m}\n"

# Define the Book, Member, and Library classes here

# Create instances of books using class methods
book1 = Book.from_string("1984, George Orwell, 9780451524935")
book2 = Book.from_string("Il Signore degli Anelli, J.R.R. Tolkien, 9780618640157")
book3 = Book.from_string("Il Piccolo Principe, Antoine de Saint-Exupéry, 9780156013987")

# Create instances of members using class methods
member1 = Member.from_string("Mario Rossi, M001")
member2 = Member.from_string("Luigi Bianchi, M002")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register members to the library
library.register_member(member1)
library.register_member(member2)

# Display the state of the library before lending
print("Stato della biblioteca prima del prestito:")
print(library)

# Lend books to members
library.lend_book(book1, member1)
library.lend_book(book2, member2)

# Display the state of the library after lending
print("Stato della biblioteca dopo il prestito:")
print(library)

# Return books to the library
member1.return_book(book1)
member2.return_book(book2)

# Display the state of the library after returning books
print("Stato della biblioteca dopo il ritorno dei libri:")
print(library)
