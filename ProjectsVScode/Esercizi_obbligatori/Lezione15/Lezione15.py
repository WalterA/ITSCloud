"""Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')"""

class FileManager:
    def __init__(self, filename, mode):
        """Inizializza il FileManager con il nome del file e la modalità."""
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Apre il file e ritorna l'oggetto file."""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Chiude il file, gestendo eventuali eccezioni."""
        if self.file:
            self.file.close()
        # Gestione delle eccezioni:
        # Se ritorniamo True, sopprimiamo l'eccezione
        # Se ritorniamo False o None, l'eccezione viene propagata
        return False

# Esempio di utilizzo:
with FileManager('ProjectsVScode\Esercizi_obbligatori\Lezione15\example.txt', 'w') as f:
    f.write('Hello, world!')
"""Crea un context manager che permette di calcolare il tempo che viene impiegato ad eseguire le istruzioni che si trovano nel with

with Timer():

    time.sleep(1)

time elapsed: 1.00000

in questo esempio il tempo passato non sarà mai uguale a 1"""
import time
from contextlib import contextmanager

@contextmanager
def timer():
    
    start = time.time()
    time.sleep(1)
    
    yield
    
    print("__exit__")
    end = time.time()
    elapsed_time = end -start
    
    print(f"time elapsed: {elapsed_time}")
    
    
if __name__ == "__main__":
    
    
    with timer() as t:
        print(t)