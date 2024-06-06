# Definiamo una lista di frutti
frutti = ["mela", "banana", "ciliegia"]

# Utilizziamo enumerate per ottenere l'indice e l'elemento
for indice, frutto in enumerate(frutti):
    print(f"Indice: {indice}, Frutto: {frutto}")

# Definiamo una lista di colori
colori = ["rosso", "verde", "blu"]

# Utilizziamo enumerate con un indice di partenza 1
for indice, colore in enumerate(colori, start=1):
    print(f"Indice: {indice}, Colore: {colore}")

# Definiamo una stringa
parola = "python"

# Utilizziamo enumerate per ottenere l'indice e il carattere
for indice, carattere in enumerate(parola):
    print(f"Indice: {indice}, Carattere: {carattere}")

# Definiamo una tupla di numeri
numeri = (10, 20, 30)

# Utilizziamo enumerate per ottenere l'indice e l'elemento
for indice, numero in enumerate(numeri):
    print(f"Indice: {indice}, Numero: {numero}")

# Definiamo una lista di numeri
numeri = [1, 2, 3, 4, 5]

# Utilizziamo enumerate per iterare e modificare la lista
for indice, numero in enumerate(numeri):
    # Aggiungiamo 10 a ogni numero nella lista
    numeri[indice] = numero + 10

print(numeri)


# Definiamo una lista di elementi
elementi = ["a", "b", "c"]

# Utilizziamo enumerate per creare un dizionario con gli indici come chiavi
dizionario = {indice: elemento for indice, elemento in enumerate(elementi)}

print(dizionario)
