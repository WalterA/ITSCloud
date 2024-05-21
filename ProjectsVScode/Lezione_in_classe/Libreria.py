"""Classe Book:

    Attributi:
        book_id: str - Identificatore di un libro.
        title: str - titolo del libro.
        author: str - autore del libro
        is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
    Metodi:
        borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
        return_book()- Contrassegna il libro come restituito."""
class Book:
    def __init__(self, book_id: str, title: str, author: str, is_borrowed: bool = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
         

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            


"""
Classe Member:

Attributi:
member_id: str - identificativo del membro.
name: str - il nome del membro.
borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
return_book(book): rimuove il libro dalla lista borrowed_books.
"""
class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: list[Book] = []

    def borrow_book(self, book: Book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
            return True
        else:
            return False

    def return_book(self, book: Book):
        if book.is_borrowed and book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True and print("aggiunto")
        else:
            return False and print("go")
    

libro = Book("gig","il pallone","biaggio",True)
# libro.borrow()
# libro.borrow()
# libro.borrow()
# libro.return_book()
# libro.return_book()
# libro.return_book()
user1 = Member("1","mario")
user1.borrow_book(libro)
user1.borrow_book(libro)

