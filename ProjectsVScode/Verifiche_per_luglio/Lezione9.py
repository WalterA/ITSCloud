"""Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
Attributi:
account_id: str - identificatore univoco per l'account.
balance: float - il saldo attuale del conto.
Metodi:
deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
get_balance(): restituisce il saldo corrente del conto.
Classe Bank:
Attributi:
accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
Metodi:
create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
get_balance(account_id): restituisce il saldo del conto con l'ID specificato."""

class Account:
    def __init__(self, account_id: str, balance=0) -> None:
        # Inizializzazione dell'istanza di Account con un ID e un saldo opzionale
        self.account_id = account_id
        self.balance = balance
        
    def deposit(self, amount: float):
        # Metodo per depositare un importo sul saldo dell'account
        self.balance += amount
    
    def get_balance(self):
        # Metodo per ottenere il saldo dell'account
        return self.balance

class Bank:
    def __init__(self) -> None:
        # Inizializzazione della banca con un dizionario per memorizzare gli account
         self.accounts: dict[str, Account] = {}
        
    def create_account(self, account_id):
        # Metodo per creare un nuovo account
        if account_id in self.accounts:
            # Se l'ID dell'account esiste già nel dizionario degli account, solleva un'eccezione
            raise ValueError("Account with this ID already exists")
        else:
            # Altrimenti, crea un nuovo account e lo aggiunge al dizionario degli account
            account = Account(account_id)
            self.accounts[account_id] = account
            return account
    
    def deposit(self, account_id, amount):
        # Metodo per depositare un importo in un account esistente
        if account_id in self.accounts:
            # Se l'account esiste, chiama il metodo deposit dell'account corrispondente
            self.accounts[account_id].deposit(amount)
        else:
            # Se l'account non esiste, restituisce un messaggio di errore
            return "Id error"

    def get_balance(self, account_id):
        # Metodo per ottenere il saldo di un account
        if account_id in self.accounts:
            # Se l'account esiste, restituisce il saldo dell'account corrispondente
            return self.accounts[account_id].get_balance()
        else:
            # Se l'account non esiste, solleva un'eccezione
            raise ValueError("Account not found")
        
"""Data una stringa s e una lista di stringhe wordDict, 
restituisce True se s può essere segmentato in una sequenza separata da 
spazi di una o più parole del dizionario; False altrimenti."""

def word_break(s: str, wordDict: list[str]) -> bool:
    # Itera attraverso le parole nel dizionario
    for i in wordDict:
        # Se una parola nel dizionario è presente nella stringa,
        # la rimuove dalla stringa
        if i in s:
            s = s.replace(i, "")
    
    # Se la stringa è vuota dopo aver rimosso tutte le parole
    # del dizionario, restituisce True
    if s == "":
        return True
    # Altrimenti, restituisce False
    else:
        return False
"""Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:

Attributi:
book_id: str - Identificatore di un libro.
title: str - titolo del libro.
author: str - autore del libro
is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
Metodi:
borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
return_book()- Contrassegna il libro come restituito.
Classe Member:

Attributi:
member_id: str - identificativo del membro.
name: str - il nome del membro.
borrowed_books: list[Book] - lista dei libri presi in prestito.
Metodi:
borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
return_book(book): rimuove il libro dalla lista borrowed_books.
Classe Library:

Attributi:
books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
Methodi:
add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False  # Imposta inizialmente il libro come non preso in prestito

    def borrow(self):
        self.is_borrowed = True  # Contrassegna il libro come preso in prestito

    def return_book(self):
        self.is_borrowed = False  # Contrassegna il libro come restituito
        
    def __str__(self):
        return f"{self.title} by {self.author}"
class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # Lista dei libri presi in prestito da questo membro

    def borrow_book(self, book):
        if book.is_borrowed:
            print("Questo libro è già stato preso in prestito.")
        else:
            book.borrow()  # Contrassegna il libro come preso in prestito
            self.borrowed_books.append(book)  # Aggiunge il libro alla lista dei libri presi in prestito

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()  # Contrassegna il libro come restituito
            self.borrowed_books.remove(book)  # Rimuove il libro dalla lista dei libri presi in prestito
        else:
            print("Il libro non è stato preso in prestito da questo membro.")
class Library:
    def __init__(self):
        self.books = {}  # Dizionario che mappa l'ID del libro all'oggetto Book corrispondente
        self.members = {}  # Dizionario che mappa l'ID del membro all'oggetto Member corrispondente

    def add_book(self, book_id: str, title: str, author: str):
        if book_id in self.books:
            print("Questo libro è già presente nella biblioteca.")
        else:
            book = Book(book_id, title, author)
            self.books[book_id] = book  # Aggiunge il libro al dizionario dei libri

    def register_member(self, member_id: str, name: str):
        if member_id in self.members:
            print("Questo membro è già registrato nella biblioteca.")
        else:
            member = Member(member_id, name)
            self.members[member_id] = member  # Aggiunge il membro al dizionario dei membri

    def borrow_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)  # Permette al membro di prendere in prestito il libro
        else:
            print("ID membro o ID libro non validi.")

    def return_book(self, member_id: str, book_id: str):
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)  # Permette al membro di restituire il libro
        else:
            print("ID membro o ID libro non validi.")

    def get_borrowed_books(self, member_id: str):
        if member_id in self.members:
            borrowed_books = self.members[member_id].borrowed_books
            return [str(book) for book in borrowed_books]
        else:
            print("ID membro non valido.")
"""PRINT"""
# library = Library()

# library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
# library.add_book("B002", "1984", "George Orwell")
# library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# # Register members
# library.register_member("M001", "Alice")
# library.register_member("M002", "Bob")
# library.register_member("M003", "Charlie")

# # Borrow books
# library.borrow_book("M001", "B001")
# library.borrow_book("M002", "B002")

# print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
# print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

"""Data una lista di interi, chiamata tree, che rappresenta un albero binario,
restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

L'elemento in posizione 0 corrisponde alla radice
Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti 
precedenti, significa che il nodo che corrisponde a quell'indice è una foglia."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric_tree(tree):
    # Funzione interna per verificare la simmetria tra due sottoalberi
    def is_mirror(left, right):
        # Se entrambi i sottoalberi sono vuoti, sono simmetrici
        if not left and not right:
            return True
        # Se uno dei due sottoalberi è vuoto e l'altro no, non sono simmetrici
        if not left or not right:
            return False
        # I due sottoalberi sono simmetrici se i loro valori sono uguali
        # e se i sottoalberi sinistri e destri dei due alberi sono simmetrici
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    # Se l'albero è vuoto, è simmetrico
    if not tree:
        return True
    # Chiamata alla funzione di verifica della simmetria dei sottoalberi
    return is_mirror(tree.left, tree.right)
"""PRINT"""
# # Creazione dell'albero di esempio
# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(2)
# tree.left.left = TreeNode(3)
# tree.left.right = TreeNode(4)
# tree.right.left = TreeNode(4)
# tree.right.right = TreeNode(3)

# # Stampa del risultato della verifica di simmetria
# print(is_symmetric_tree(tree))  # Output atteso: True 

"""Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
in genere utilizzando tutte le lettere originali esattamente una volta."""

def anagram(s: str, t: str) -> bool:
    # Trasforma entrambe le stringhe in minuscolo e rimuove gli spazi
    t = t.lower().replace(" ", "")
    s = s.lower().replace(" ", "")
    
    # Verifica se le due stringhe sono anagrammi confrontando le loro versioni ordinate
    if sorted(t) == sorted(s):
        return True
    else:
        return False
    
"""Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita."""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    result = []  # Inizializza una lista vuota per contenere gli elementi della lista invertita
    current = head  # Imposta il nodo corrente all'inizio della lista
    while current:
        result.append(current.val)  # Aggiunge il valore del nodo corrente alla lista risultato
        current = current.next  # Passa al nodo successivo
    return result[::-1]  # Restituisce la lista invertita

"""PRINT"""
# # Test dei casi
# head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
# print(reverse_list(head))
# head = ListNode(val=1, next=ListNode(val=2))
# print(reverse_list(head))


"""Determina se una tavola Sudoku 9 x 9 è valida.
Solo le celle compilate devono essere convalidate secondo le seguenti regole:

Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.
Nota:

Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
Solo le celle riempite devono essere convalidate secondo le regole menzionate."""

def valid_sudoku(board: list[list[str]]) -> bool:
    # Controllo delle righe
    for row in board:
        if not is_valid_unit(row):  # Controlla se la riga è valida
            return False
    
    # Controllo delle colonne
    for col in range(9):
        column = [board[row][col] for row in range(9)]  # Estrae la colonna corrente
        if not is_valid_unit(column):  # Controlla se la colonna è valida
            return False
    
    # Controllo dei sottoriquadri 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]  # Estrae il sottoriquadro corrente
            if not is_valid_unit(square):  # Controlla se il sottoriquadro è valido
                return False
    
    return True

def is_valid_unit(unit: list[str]) -> bool:
    seen = set()  # Inizializza un set per tenere traccia dei numeri visti
    for num in unit:
        if num != '.':  # Ignora le celle vuote
            if num in seen:  # Se il numero è già stato visto, la unità non è valida
                return False
            seen.add(num)  # Aggiunge il numero visto al set
    return True  # Se non ci sono ripetizioni, la unità è valida

"""PRINT"""
# # Test
# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# print(valid_sudoku(board))

# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# print(valid_sudoku(board))

