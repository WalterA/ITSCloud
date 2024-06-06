# Definiamo due liste
nomi = ["Alice", "Bob", "Charlie"]
eta = [25, 30, 35]

# Utilizziamo zip per combinare le due liste
combinazione = zip(nomi, eta)

# Iteriamo sulla combinazione e stampiamo le tuple
for nome, eta in combinazione:
    print(f"Nome: {nome}, Età: {eta}")

# Definiamo tre liste
nomi = ["Alice", "Bob", "Charlie"]
eta = [25, 30, 35]
citta = ["Roma", "Milano", "Torino"]

# Utilizziamo zip per combinare le tre liste
combinazione = zip(nomi, eta, citta)

# Iteriamo sulla combinazione e stampiamo le tuple
for nome, eta, citta in combinazione:
    print(f"Nome: {nome}, Età: {eta}, Città: {citta}")
    

# Definiamo due stringhe
stringa1 = "ABC"
stringa2 = "123"

# Utilizziamo zip per combinare le due stringhe
combinazione = zip(stringa1, stringa2)

# Iteriamo sulla combinazione e stampiamo le tuple
for carattere1, carattere2 in combinazione:
    print(f"Carattere 1: {carattere1}, Carattere 2: {carattere2}")

# Definiamo due liste
chiavi = ["nome", "età", "città"]
valori = ["Alice", 25, "Roma"]

# Utilizziamo zip per combinare le liste e creare un dizionario
dizionario = dict(zip(chiavi, valori))

print(dizionario)


#    Definiamo una lista di tuple
tuples = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]

# Utilizziamo zip per scomprimere la lista di tuple
nomi, eta = zip(*tuples)

print("Nomi:", nomi)
print("Età:", eta)

# Definiamo due liste di lunghezza diversa
numeri = [1, 2, 3, 4, 5]
lettere = ["a", "b", "c"]

# Utilizziamo zip per combinare le due liste
combinazione = zip(numeri, lettere)

# Iteriamo sulla combinazione e stampiamo le tuple
for numero, lettera in combinazione:
    print(f"Numero: {numero}, Lettera: {lettera}")

