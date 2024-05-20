class Book:
    def __init__(self, book_id:str,title:str,author:str,is_borrowed:bool) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed  # Usa il valore passato al costruttore

    def borrow(self):
        if self.is_borrowed:
            print("Libro in prestito")  # Il libro è già in prestito
            return False
        else:
            self.is_borrowed = True  # Il libro viene preso in prestito
            return True

    def return_book(self):
        if not self.is_borrowed:
            print("gia consegnato")  # Il libro è già stato restituito
            return False
        else:
            self.is_borrowed = False  # Il libro viene restituito
            return True

class Member:
    def __init__(self, member_id: str, name: str, borrowed_books: list[Book] = None) -> None:
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books else []  # Inizializza con una lista vuota se non viene passata nessuna lista

    def borrow_book(self, book: Book):
        if book.borrow():  # Chiama il metodo borrow sull'oggetto Book
            self.borrowed_books.append(book)  # Aggiungi il libro alla lista dei libri presi in prestito
            print("Libro preso in prestito")
        else:
            print("Non è possibile prendere in prestito il libro")

    def return_book(self, book: Book):
        if book in self.borrowed_books and book.return_book():  # Controlla se il libro è nella lista dei libri presi in prestito e se può essere restituito
            self.borrowed_books.remove(book)  # Rimuovi il libro dalla lista dei libri presi in prestito
            print("Libro restituito")
        else:
            print("Non è possibile restituire il libro")

libro = Book("gig","il pallone","biaggio",False)
membro = Member("1", "Mario")
membro.borrow_book(libro)  # Ora dovrebbe funzionare correttamente
membro.borrow_book(libro)
