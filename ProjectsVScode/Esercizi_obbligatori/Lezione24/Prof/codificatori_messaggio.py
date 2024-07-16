from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        """Metodo astratto per codificare un messaggio."""
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        """Metodo astratto per decodificare un messaggio."""
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave: int = chiave  # int: chiave di scorrimento per la codifica

    def codifica(self, testoInChiaro: str) -> str:
        """Codifica il testo spostando ogni lettera di 'chiave' posizioni."""
        testo_codificato = ""
        for c in testoInChiaro:
            testo_codificato += self._sposta_carattere(c)
        return testo_codificato

    def _sposta_carattere(self, c: str) -> str:
        """Sposta un singolo carattere di 'chiave' posizioni nell'alfabeto."""
        alfabeto_minuscole: str = "abcdefghijklmnopqrstuvwxyz" # alfabeto minuscolo
        alfabeto_maiuscole: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto maiuscolo
        c_codificato: str = ""

        # Trova la nuova posizione della lettera spostata di 'chiave' posizioni

        if c in alfabeto_maiuscole:
            # Trova la posizione corrente del carattere c nell'alfabeto delle maiuscole e aggiunge la chiave di scorrimento
            new_posizione: int = alfabeto_maiuscole.index(c) + self.chiave

            if new_posizione < len(alfabeto_maiuscole):
                # Verifica se la nuova posizione è minore della lunghezza dell'alfabeto
                c_codificato = alfabeto_maiuscole[new_posizione]
            else:
                # Se la posizione è maggiore della lunghezza dell'alfabeto, calcola la posizione circolare, ovvero calcola il nuovo indice a partire dall'inizio dell'alfabeto
                new_posizione = new_posizione - len(alfabeto_maiuscole)
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_codificato = alfabeto_maiuscole[new_posizione]
        
        if c in alfabeto_minuscole:
            # Trova la posizione corrente del carattere c nell'alfabeto delle minuscole e aggiunge la chiave di scorrimento
            new_posizione: int = alfabeto_minuscole.index(c) + self.chiave
            # Verifica se la nuova posizione è minore della lunghezza dell'alfabeto
            if new_posizione < len(alfabeto_minuscole):
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_codificato = alfabeto_minuscole[new_posizione]
            else:
                 # Se la posizione è maggiore della lunghezza dell'alfabeto, calcola la posizione circolare, ovvero calcola il nuovo indice a partire dall'inizio dell'alfabeto
                new_posizione = new_posizione - len(alfabeto_minuscole)
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_codificato = alfabeto_minuscole[new_posizione]
        
        return c_codificato

    def decodifica(self, testoCodificato: str) -> str:
        """Decodifica il testo spostando ogni lettera di 'chiave' posizioni."""
        testo_decodificato = ""
        for c in testoCodificato:
            testo_decodificato += self._decodifica_carattere(c)
        return testo_decodificato


    
    def _decodifica_carattere(self, c: str) -> str:
        """Metodo che compie un'azione inversa al metodo sposta_carattere().Sposta un singolo carattere di 'chiave' posizioni nell'alfabeto."""
        alfabeto_minuscole: str = "abcdefghijklmnopqrstuvwxyz" # alfabeto minuscolo
        alfabeto_maiuscole: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # alfabeto maiuscolo
        c_decodificato: str = ""

        # Trova la nuova posizione della lettera spostata di 'chiave' posizioni

        if c in alfabeto_maiuscole:
            # Trova la posizione corrente del carattere c nell'alfabeto delle maiuscole e toglie la chiave di scorrimento
            new_posizione: int = alfabeto_maiuscole.index(c) - self.chiave
             # Verifica se la nuova posizione non va oltre la posizione 0
            if new_posizione >= 0:
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_decodificato = alfabeto_maiuscole[new_posizione]
            else:
                # Se la nuova posizione è minore di 0, dunque, va oltre la posizione 0 del primo carattere, calcola la posizione circolare, ovvero calcola il nuovo indice a partire dall'ultima lettera dell'alfabeto'
                new_posizione = len(alfabeto_maiuscole) - new_posizione
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_decodificato = alfabeto_maiuscole[new_posizione]
        
        if c in alfabeto_minuscole:
            # Trova la posizione corrente del carattere c nell'alfabeto delle minuscole e aggiunge la chiave di scorrimento
            new_posizione: int = alfabeto_minuscole.index(c) - self.chiave
            # Verifica se la nuova posizione non va oltre la posizione 0
            if new_posizione >= 0:
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_decodificato = alfabeto_minuscole[new_posizione]
            else:
                 # Se la nuova posizione è minore di 0, dunque, va oltre la posizione 0 del primo carattere, calcola la posizione circolare, ovvero calcola il nuovo indice a partire dall'ultima lettera dell'alfabeto'
                new_posizione = len(alfabeto_minuscole) - (new_posizione * -1) # poichè new_posizione è un valore negativo, essendo per ipotesi <0, devo invertire il suo segno motliplicando new_posizione per -1. Poi sottraggo new_posizione a len(alfabeto)
                # Assegna il carattere corrispondente dalla nuova posizione nell'alfabeto
                c_decodificato = alfabeto_minuscole[new_posizione]
        
        return c_decodificato

    def leggi_da_file(self, file_path: str) -> str:
        """Legge il contenuto di un file e lo restituisce come stringa."""
        with open(file_path, 'r') as file:
            return file.read()

    def scrivi_su_file(self, testo: str, file_path: str) -> None:
        """Scrive una stringa in un file."""
        with open(file_path, 'w') as file:
            file.write(testo)


class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n: int = n  # int: numero di volte che il messaggio sarà combinato

    def codifica(self, testoInChiaro: str) -> str:
        """Codifica il testo combinandolo 'n' volte."""
        testo: str = testoInChiaro  # str: inizia con il testo in chiaro
        for _ in range(self.n):  # Esegue 'n' combinazioni
            testo = self._combinazione(testo)  # str: testo dopo una combinazione
        return testo

    def _combinazione(self, testo: str) -> str:
        """Esegue una singola combinazione del testo."""
        meta: int = 0
        # se la lunghezza del testo è un numero pari, dividi il testo in due metà di lunghezza uguale
        if len(testo) % 2 == 0:
            meta = len(testo) // 2  # int: punto di divisione del testo, ovvero a metà. 
        else:
            # altrimenti, se la lunghezza del testo è un numero dispari, dividi il testo in due metà, di cui, la prima metà è più lunga della seconda
            meta = len(testo) // 2 + 1 # il +1 fa si che in caso di lunghezza dispari di testo, la prima metà sia più lunga della seconda metà
        
        primo: str = testo[:meta]  # str: prima metà del testo
        secondo: str = testo[meta:]  # str: seconda metà del testo
        
        # Combina alternando i caratteri delle due metà
        testo_combinato: str = ""

        for index in range(len(primo)): # la lunghezza di primo, per impostazione è maggiore di secondo
            if index < len(secondo): # finchè è possibile iterare su secondo
                testo_combinato = testo_combinato + primo[index] + secondo[index] # concatena un carattere di primo ed un carattere di secondo
            else: # quando non è più possibile iterare su secondo
                testo_combinato = testo_combinato + primo[index] # concatena i caratteri di primo rimanenti

        return testo_combinato

    def decodifica(self, testoCodificato: str) -> str:
        """Codifica il testo combinandolo 'n' volte."""
        testo: str = testoCodificato  # str: inizia con il testo in chiaro
        for _ in range(self.n):  # Esegue 'n' combinazioni
            testo = self._decodifica_combinazione(testo)  # str: testo dopo una combinazione
        return testo
    
    def _decodifica_combinazione(self, testo: str) -> str:
        """Decodifica una sola combinazione del testo."""
        # devo scomporre il testo in due metà
        primo: str = ""  # str: prima metà del testo
        secondo: str = ""  # str: seconda metà del testo
        
        # Combina alternando i caratteri delle due metà
        testo_ricombinato: str = ""

        for index in range(len(testo)): # la lunghezza di primo, per impostazione è maggiore di secondo
            # se index è pari
            if index % 2 == 0:
                primo = primo + testo[index] # nella prima metà del testo devo inserire i caratteri di indice pari del testo codificato
            else: # se index è dispari
                secondo = secondo + testo[index] # nella seconda metà del testo devo inserire i caratteri di indice dispari del testo codificato

        # ricombina il testo concatendando primo con secondo
        testo_ricombinato = testo_ricombinato + primo + secondo
        
        return testo_ricombinato
    
    def leggi_da_file(self, file_path: str) -> str:
        """Legge il contenuto di un file e lo restituisce come stringa."""
        with open(file_path, 'r') as file:
            return file.read()

    def scrivi_su_file(self, testo: str, file_path: str) -> None:
        """Scrive una stringa in un file."""
        with open(file_path, 'w') as file:
            file.write(testo)


# Test del Cifratore a Scorrimento
# Inizializzazione del cifratore con una chiave di scorrimento di 3
cifratore_scor: CifratoreAScorrimento = CifratoreAScorrimento(3)
# Lettura del testo in chiaro da un file
testo_da_file: str = cifratore_scor.leggi_da_file("./testo_da_cifrare_scorrimento.txt")
# Codifica del testo in chiaro
testo_cifrato: str = cifratore_scor.codifica(testo_da_file)
# Scrittura del testo codificato su un file
cifratore_scor.scrivi_su_file(testo_cifrato, "./testo_cifrato_scorrimento.txt")
# Stampa del testo codificato
print("Testo cifrato (scorrimento):", testo_cifrato)
# Decodifica del testo codificato
testo_decriptato: str = cifratore_scor.decodifica(testo_cifrato)
# Stampa del testo decodificato
print("Testo decifrato (scorrimento):", testo_decriptato)

# Test del Cifratore a Combinazione
# Inizializzazione del cifratore con un numero di combinazioni di 3
cifratore_comb: CifratoreACombinazione = CifratoreACombinazione(3)
# Lettura del testo in chiaro da un file
testo_da_file: str = cifratore_comb.leggi_da_file("./testo_da_cifrare_combinazione.txt")
# Codifica del testo in chiaro
testo_cifrato: str = cifratore_comb.codifica(testo_da_file)
# Scrittura del testo codificato su un file
cifratore_comb.scrivi_su_file(testo_cifrato, "./testo_cifrato_combinazione.txt")
# Stampa del testo codificato
print("Testo cifrato (combinazione):", testo_cifrato)
# Decodifica del testo codificato
testo_decriptato: str = cifratore_comb.decodifica(testo_cifrato)
# Stampa del testo decodificato
print("Testo decifrato (combinazione):", testo_decriptato)
