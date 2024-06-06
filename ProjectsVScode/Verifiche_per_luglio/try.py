# Definiamo due variabili
a = 10
b = 0

try:
    # Proviamo a dividere 'a' per 'b'
    risultato = a / b
    print("Risultato:", risultato)
except ZeroDivisionError:
    # Gestiamo l'eccezione di divisione per zero
    print("Errore: Divisione per zero non consentita.")


# Definiamo una lista di numeri
numeri = [1, 2, 3]

try:
    # Proviamo ad accedere a un elemento con un indice non valido
    elemento = numeri[5]
    print("Elemento:", elemento)
except IndexError:
    # Gestiamo l'eccezione di indice non valido
    print("Errore: Indice non valido.")


# Definiamo due variabili
a = 10
b = 2

try:
    # Proviamo a dividere 'a' per 'b'
    risultato = a / b
except ZeroDivisionError:
    # Gestiamo l'eccezione di divisione per zero
    print("Errore: Divisione per zero non consentita.")
else:
    # Questo blocco viene eseguito solo se non si verifica alcuna eccezione
    print("La divisione è riuscita. Risultato:", risultato)


# Definiamo una variabile
file_path = "non_esistente.txt"

try:
    # Proviamo ad aprire un file che non esiste
    file = open(file_path, "r")
except FileNotFoundError:
    # Gestiamo l'eccezione di file non trovato
    print("Errore: File non trovato.")
finally:
    # Questo blocco viene sempre eseguito
    print("Operazione completata.")


# Definiamo due variabili
a = 10
b = "zero"

try:
    # Proviamo a dividere 'a' per 'b' convertendo 'b' in un intero
    risultato = a / int(b)
except ZeroDivisionError:
    # Gestiamo l'eccezione di divisione per zero
    print("Errore: Divisione per zero non consentita.")
except ValueError:
    # Gestiamo l'eccezione di valore non valido
    print("Errore: Valore non valido per la conversione in intero.")
    

# Definiamo una variabile
valore = "abc"

try:
    # Proviamo a convertire 'valore' in un intero
    numero = int(valore)
except Exception as e:
    # Gestiamo qualsiasi eccezione e stampiamo il messaggio di errore
    print("Errore:", e)

