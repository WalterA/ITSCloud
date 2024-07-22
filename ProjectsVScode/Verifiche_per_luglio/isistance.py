# Definiamo una variabile con un valore intero
x = 10

# Verifichiamo se 'x' è un'istanza della classe 'int'
if isinstance(x, int):
    print("x è un intero")
else:
    print("x non è un intero")

# Definiamo una variabile con una lista di numeri
y = [1, 2, 3]

# Verifichiamo se 'y' è un'istanza della classe 'list'
if isinstance(y, list):
    print("y è una lista")
else:
    print("y non è una lista")
# Definiamo una variabile con un valore float
z = 3.14

# Verifichiamo se 'z' è un'istanza della classe 'int' o 'float'
if isinstance(z, (int, float)):
    print("z è un numero (intero o float)")
else:
    print("z non è un numero (intero o float)")

# Definiamo una classe base
class Animale:
    pass

# Definiamo una classe derivata
class Cane(Animale):
    pass

# Creiamo un'istanza della classe Cane
fido = Cane()

# Verifichiamo se 'fido' è un'istanza della classe 'Cane'
if isinstance(fido, Cane):
    print("fido è un cane")

# Verifichiamo se 'fido' è un'istanza della classe 'Animale'
if isinstance(fido, Animale):
    print("fido è un animale")


# Definiamo una variabile con una stringa
a = "ciao"

# Verifichiamo se 'a' è un'istanza di 'int', 'float' o 'str'
if isinstance(a, (int, float, str)):
    print("a è un tipo di dato int, float o str")
else:
    print("a non è un tipo di dato int, float o str")

