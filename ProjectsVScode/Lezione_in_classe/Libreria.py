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
    def __init__(self, book_id:str,title:str,author:str,is_borrowed:bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = True

    def borrow(self):
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            return print("Libro in prestito")
    def return_book(self):
        if self.is_borrowed:
            return print("gia consegnato")
        else:
            self.is_borrowed = True
            return print("consegnato")

class Member:
    def __init__(self,
                 member_id: str,
                 name: str,
                 borrowed_books: list[Book]) -> None:
        self.member_id = member_id
        self.name = name
        
        
                
        
libro = Book("gig","il pallone","biaggio",True)
libro.borrow()
libro.borrow()
libro.borrow()
libro.return_book()
libro.return_book()
libro.return_book()

