class Contatore:
    def __init__(self) -> None:
        """ un intero che conserva il valore del conteggio, inizializzato a 0."""
        self.conteggio = 0
    def setZero(self): 
        """Imposta il conteggio a 0"""
        self.conteggio = 0
    def add1(self): 
        """Incrementa il conteggio di 1"""
        self.conteggio += 1
    def sub1(self): 
        """Decrementa il conteggio di 1, 
        ma non permette che il conteggio diventi negativo. Se il conteggio è già 0, 
        stampa un messaggio di errore."""
        
        self.conteggio -= 1
        if self.conteggio <= 0:
            self.conteggio = 0
            return print("Non è possibile eseguire la sottrazione")
    def get(self): 
        """Restituisce il valore corrente del conteggio."""
        return f"{self.conteggio}"
    def mostra(self): 
        """Stampa a schermo il valore corrente del conteggio."""
        print(f"Conteggio attuale: {self.conteggio}")