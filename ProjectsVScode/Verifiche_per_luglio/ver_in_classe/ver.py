#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
from collections import Counter
def frequency_dict(elements: list) -> dict:
    f:list = Counter(elements)
    dic:dict={}
    for i in f:
        dic[i] = f[i]    
    return dic
    
    
#print(frequency_dict(['mela', 'banana', 'mela']))

#Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
#  - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
def transform(x: int) -> int:
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 - 1

# print(transform(4))

# print(transform(-10))

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict3 = {}
    for key, val in dict1.items():
        if key in dict2:
            dict3[key] = dict1[key] + dict2[key]
        else:
            dict3[key] = val
    for key, val in dict2.items():
        if key in dict1:
            dict3[key] = dict1[key] + dict2[key]
        else:
            dict3[key] = val
    return dict3
	

# print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

#Scrivi una funzione che converta una lista di tuple (chiave, valore)
# in un dizionario. Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.
def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    diz:dict ={}
    for lettera, valore in tuples:
        if lettera in diz:
            diz[lettera].append(valore)
        else:
            diz[lettera] = [valore]
    return diz
    
    
#print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))


#Scrivi una funzione che somma tutti i numeri interi di una lista che sono maggiori di un dato valore intero definito threshold.
def sum_above_threshold(numbers: list[int], n:int) -> int:
    somma:int = 0
    for i in numbers:
        if i > n:
            somma += i
    return somma

#print(sum_above_threshold([15, 5, 25], 20))

#Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
# a) 1, 2, 3, 4, 5, 6, 7
# b) 3, 8, 13, 18, 23
# c) 20, 14, 8, 2, -4, -10
# d) 19, 27, 35, 43, 51
def print_seq(): 
    
    print("Sequenza a):")
    for i in a:
        print(i)

    print("Sequenza b):")
    for i in b:
        print(i)

    print("Sequenza c):")
    for i in c:
        print(c)

    print("Sequenza d):")
    for i in d:
        print(d)
    
    return

# print_seq()
#Scrivi una funzione che accetti un
# dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%
def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    prodotti_scontati = {}
    
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            prezzo_scontato = prezzo * 0.9  
            prodotti_scontati[prodotto] = prezzo_scontato
    
    return prodotti_scontati
#print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave 
# che corrisponde a quel valore, o None se il valore non è presente.
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for k,v in dizionario.items():
        if valore == v:
            return k
    else:
         return None
	


#print(trova_chiave_per_valore({'a': 100, 'b': 200, 'c': 300}, 200))
#Scrivi una funzione che accetti tre parametri: username, password 
# e status di attivazione dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "admin", 
# la password corrisponde a "12345" e l'account è attivo. La funzione ritorna "Accesso consentito" oppure "Accesso negato".
def check_access(username: str, password:str, is_active: bool) -> str:
    if username == "admin":
        if password == "12345":
            if is_active is True:
                return ("Accesso consentito")
            else:
                return ("Accesso negato")
        else:
            return ("Accesso negato")
    else:
        return("Accesso negato")
# print(check_access("admin", "12345", True))
# print(check_access("admin", "54321", True))
        
#Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    diz:dict = {"pari": [], "dispari":[]}
    for i in lista:
        if i %2 == 0:
            diz["pari"].append(i)
        else:
            diz["dispari"].append(i)
    return diz
            
#print(classifica_numeri([1, 2, 3, 4, 5, 6]))

#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) 
# è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
# La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA or (conditionB or conditionC):
        return ("Operazione permessa")
    else:
        return ("Operazione negata")
#print(check_combination(True, False, True))
#la gestione delle ricette in Python 
class RecipeManager:
    def __init__(self) -> None:
        self.elenco_ricette:dict[str,list]={}
        
    def create_recipe(self,name:str,ingredients:list[str])->dict:

        if name not in self.elenco_ricette:
            self.elenco_ricette[name]= ingredients
            
        else:
            return (f'esiste la ricetta:{name=}')
        return {name: self.elenco_ricette[name]}
    def add_ingredient(self,recipe_name:str,ingredient:str)->dict:
        if recipe_name in self.elenco_ricette:
            if ingredient in self.elenco_ricette[recipe_name]:
                return (f'esiste già l\'ingrediente:{ingredient=}')
            else:
                self.elenco_ricette[recipe_name].append(ingredient)
        else:
            return (f'esiste la ricetta:{recipe_name=}')
        return {recipe_name: self.elenco_ricette[recipe_name]}
    def remove_ingredient(self,recipe_name:str, ingredient:str)->dict:
        if recipe_name not in self.elenco_ricette:
            return {'error': f'La ricetta "{recipe_name}" non esiste.'}
        if ingredient not in self.elenco_ricette[recipe_name]:
            return {'error': f'L\'ingrediente "{ingredient}" non esiste nella ricetta "{recipe_name}".'}
        self.elenco_ricette[recipe_name].remove(ingredient)
        return {recipe_name: self.elenco_ricette[recipe_name]}
    
    def update_ingredient(self,recipe_name:str, old_ingredient:str, new_ingredient:str)->dict:
        if recipe_name in self.elenco_ricette:
            if old_ingredient in self.elenco_ricette[recipe_name]:
                index = self.elenco_ricette[recipe_name].index(old_ingredient)
                self.elenco_ricette[recipe_name][index] = new_ingredient
                return {recipe_name: self.elenco_ricette[recipe_name]}
            else:
                return (f'NON esiste l\'INGR:{old_ingredient=}')
        else:
            return (f'NON esiste la ricetta:{recipe_name=}')
    def list_recipes(self)->str:
        return list(self.elenco_ricette.keys())
    
    def list_ingredients(self,recipe_name:str)->list:
        if recipe_name not in self.elenco_ricette:
            return {'error': f'La ricetta "{recipe_name}" non esiste.'}
        return list(self.elenco_ricette[recipe_name])
    
    def search_recipe_by_ingredient(self,ingredient:str)->dict:
        for k,v in self.elenco_ricette.items():
            if ingredient in v:
                return {k: self.elenco_ricette[k]}
            
        return (f'NON esiste la ricetta:{ingredient=}')
#creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
class Veicolo:
    def __init__(self, marca:str,modello:str,anno:int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno
    def descrivi_veicolo(self):
        print(f'Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}')
    
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte:int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
        
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno},  Numero di porte: {self.numero_porte}")
    
class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo:str) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo : {self.tipo}")

	

# veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
# auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
# moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

# veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
# auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
# moto.descrivi_veicolo()  

#sistema di videonoleggio
class Movie:
    def __init__(self, movie_id:str, title:str, director:str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rended = False
        
    def rent(self):
        if self.is_rended is False:
            self.is_rended = True 
        else:
            return f'Il film {self.title} è già noleggiato.'
    def return_movie(self):
        if self.is_rended is True:
            return f"Il film {self.title} non è attualmente noleggiato."      
        else:
            self.is_rended = False
    
class Customer:
    def __init__(self, customer_id:str, name:str) -> None:
        self.customer_id = customer_id
        self.nome = name
        self.rented_movie:list[Movie] = []
        
    def rent_movie(self, movie:Movie):
        if movie.is_rended is True:
            self.rented_movie.append(movie)
        else:
            f'Il film {movie.title} è già noleggiato.'
    def return_movie(self,movie:Movie):
        if movie in self.rented_movie:
            self.rented_movie.remove(movie)
        else:
            f"Il film {movie.title} non è stato noleggiato da questo cliente."
class VideoRentalStore:
    def __init__(self, movie:dict[str,Movie], customers:dict[str,Customer]) -> None:            
        
                
        
        