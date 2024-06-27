import time
def decor(func):
    
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        elapsed_time = end - start 
        print(f"{elapsed_time=}" )
        
    return wrapper 


@decor
class Animal:
# Definisce la classe Animal.

    def __init__(self, name: str, species: str, age: float, height: float, width:float, preferred_habitat:str) -> None:
    # Definisce il metodo di inizializzazione (__init__) per la classe Animal.

        self.name: str = name
        # Assegna il nome dell'animale.
        
        self.species: str = species
        # Assegna la specie dell'animale.
        
        self.age: float = age
        # Assegna l'età dell'animale.
        
        self.height: float = height
        # Assegna l'altezza dell'animale.
        
        self.width: float = width
        # Assegna la larghezza dell'animale.
        
        self.preferred_habitat: str = preferred_habitat
        # Assegna l'habitat preferito dell'animale.
        
        # Calcola la salute iniziale dell'animale basata sull'età, limitata a un massimo di 100.
        self.health: float = min(round(100 * (1/self.age), 3), 100)
        
        self.fence: Fence = None
        # Inizializza il recinto dell'animale come None all'inizio.
        
    def area(self):
    # Definisce un metodo per calcolare l'area dell'animale.
        return self.height * self.width
        # Calcola e restituisce l'area dell'animale.
        
    def become_bigger(self, factor: float = 0.02) -> tuple[float, float]:
    # Definisce un metodo per far crescere le dimensioni dell'animale.
        height = self.height + self.height * factor
        width = self.width + self.width * factor
        return height, width
        # Restituisce le nuove dimensioni dell'animale.
        
    def become_healthier(self, factor: float = 0.01):
    # Definisce un metodo per migliorare la salute dell'animale.
        self.health = min(self.health + self.health * factor, 100)
        # Incrementa la salute dell'animale, limitata a un massimo di 100.
        
    def __str__(self) -> str:
    # Definisce il metodo speciale __str__ per ottenere una rappresentazione in stringa dell'oggetto Animal.
        return f'Animal(name={self.name}, species={self.species}, age={self.age}, height={round(self.height,3)}, width={round(self.width,3)}, habitat={self.preferred_habitat})'
        # Restituisce una stringa formattata che rappresenta le informazioni dell'animale.

@decor   
class Fence:
# Definisce la classe Fence.

    def __init__(self, area: float, temperature: float, habitat: str) -> None:
    # Definisce il metodo di inizializzazione (__init__) per la classe Fence.
        self.area: float = area
        # Assegna l'area del recinto.
        
        self.temperature: float = temperature
        # Assegna la temperatura del recinto.
        
        self.habitat: str = habitat
        # Assegna l'habitat del recinto.
        
        self.animals: list[Animal] = []
        # Inizializza una lista vuota per contenere gli animali nel recinto.

    def same_habitat(self, animal: Animal) -> bool:
    # Definisce un metodo per controllare se un animale ha lo stesso habitat del recinto.
        return animal.preferred_habitat.lower() == self.habitat.lower()
        # Confronta l'habitat preferito dell'animale (ignorando le maiuscole/minuscole) con l'habitat del recinto.

    def enough_space(self, animal_area: float) -> bool:
    # Definisce un metodo per verificare se c'è abbastanza spazio nel recinto per un dato animale.
        return animal_area <= self.area
        # Restituisce True se l'area dell'animale è minore o uguale all'area disponibile nel recinto.

    def update_area(self, new_animal_area: float, old_animal_area: float):
    # Definisce un metodo per aggiornare l'area del recinto dopo l'aggiunta o la rimozione di un animale.
        self.area += old_animal_area
        # Aggiunge all'area del recinto l'area occupata dall'animale che viene rimosso.
        
        self.area -= new_animal_area
        # Sottrae dall'area del recinto l'area occupata dall'animale che viene aggiunto.

    def add_animal(self, animal: Animal):
    # Definisce un metodo per aggiungere un animale al recinto.
        animal_area: float = animal.area()
        # Calcola l'area dell'animale.
        
        if self.same_habitat(animal) and self.enough_space(animal_area) and animal not in self.animals:
        # Verifica se l'animale ha lo stesso habitat del recinto, 
        # se c'è abbastanza spazio nel recinto e se l'animale non è già presente.
        
            self.animals.append(animal)
            # Aggiunge l'animale alla lista degli animali nel recinto.
            
            self.area -= animal_area
            # Sottrae l'area occupata dall'animale dall'area totale del recinto.
            
            animal.fence = self
            # Imposta il recinto dell'animale su questo recinto.

    def remove_animal(self, animal: Animal):
    # Definisce un metodo per rimuovere un animale dal recinto.
        if animal in self.animals:
        # Verifica se l'animale è presente nella lista degli animali del recinto.
        
            self.animals.remove(animal)
            # Rimuove l'animale dalla lista degli animali nel recinto.
            
            animal_area: float = animal.area()
            # Calcola l'area dell'animale.
            
            self.area += animal_area
            # Aggiunge l'area occupata dall'animale all'area totale del recinto.
            
            animal.fence = None
            # Imposta il recinto dell'animale su None, indicando che l'animale non è più nel recinto.

    def feed(self, animal: Animal):
    # Definisce un metodo per nutrire un animale nel recinto.
        new_height, new_width = animal.become_bigger()
        # Calcola le nuove dimensioni dell'animale dopo essere stato nutrito.
        
        if self.enough_space((new_height * new_width) - animal.area()):
        # Verifica se c'è abbastanza spazio nel recinto per le nuove dimensioni dell'animale.
        
            self.area += animal.area()
            # Aggiunge l'area occupata dall'animale prima di essere nutrito all'area totale del recinto.
            
            animal.height = new_height
            animal.width = new_width
            # Imposta le nuove dimensioni dell'animale.
            
            self.area -= animal.area()
            # Sottrae dall'area totale del recinto l'area occupata dalle nuove dimensioni dell'animale.
            
            animal.become_healthier()
            # Incrementa la salute dell'animale.
            
    def __str__(self) -> str:
    # Definisce il metodo speciale __str__ per ottenere una rappresentazione in stringa dell'oggetto Fence.
        return f"Fence(area={round(self.area,3)}, temperature={self.temperature}, habitat={self.habitat})"
        # In
class ZooKeeper:
# Definisce la classe ZooKeeper.

    def __init__(self, name: str, surname: str, id: str) -> None:
    # Definisce il metodo di inizializzazione (__init__) per la classe ZooKeeper.
        self.name: str = name
        # Assegna il nome dello ZooKeeper.
        
        self.surname: str = surname
        # Assegna il cognome dello ZooKeeper.
        
        self.id: str = id
        # Assegna l'ID dello ZooKeeper.

    def add_animal(self, animal: Animal, fence: Fence):
    # Definisce un metodo per aggiungere un animale a un recinto.
        fence.add_animal(animal)
        # Chiama il metodo add_animal del recinto per aggiungere l'animale.

    def remove_animal(self, animal: Animal, fence: Fence):
    # Definisce un metodo per rimuovere un animale da un recinto.
        fence.remove_animal(animal)
        # Chiama il metodo remove_animal del recinto per rimuovere l'animale.

    def feed(self, animal: Animal):
    # Definisce un metodo per nutrire un animale.
        fence: Fence = animal.fence
        # Ottiene il recinto in cui si trova l'animale.
        
        if fence:
        # Verifica se l'animale è in un recinto (non è fuori).
            fence.feed(animal)
            # Chiama il metodo feed del recinto per nutrire l'animale.

    def clean(self, fence: Fence) -> float:
    # Definisce un metodo per pulire un recinto.
        occupied_area: float = 0
        # Inizializza la variabile per tracciare l'area occupata nel recinto.
        
        for animal in fence.animals:
        # Itera su tutti gli animali presenti nel recinto.
            occupied_area += animal.area()
            # Aggiunge l'area occupata dall'animale alla variabile occupied_area.
            
        if fence.area == 0:
        # Se l'area del recinto è 0, restituisce l'area occupata.
            return occupied_area
        else:
        # Altrimenti, calcola e restituisce la frazione dell'area occupata rispetto all'area totale del recinto.
            return occupied_area / fence.area

    def clean_all(self, zoo) -> float:
    # Definisce un metodo per pulire tutti i recinti in uno zoo e restituire il tempo totale impiegato per la pulizia.
        cleaning_time = 0
        # Inizializza la variabile per tracciare il tempo totale di pulizia.
        
        for fence in zoo.fences:
        # Itera su tutti i recinti nello zoo.
            cleaning_time += self.clean(fence)
            # Chiama il metodo clean per pulire il recinto e aggiunge il tempo impiegato alla variabile cleaning_time.
            
        return cleaning_time
        # Restituisce il tempo totale di pulizia.

    def __str__(self) -> str:
    # Definisce il metodo speciale __str__ per ottenere una rappresentazione in stringa dell'oggetto ZooKeeper.
        return f'ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})'
        # Restituisce una stringa formattata che rappresenta le informazioni dello ZooKeeper.
@decor
class Zoo:
# Definisce la classe Zoo.

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]):
    # Definisce il metodo di inizializzazione (__init__) per la classe Zoo.
        self.fences: list[Fence] = fences
        # Assegna la lista dei recinti allo zoo.
        
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers
        # Assegna la lista degli zookeeper allo zoo.

    def describe_zoo(self):
    # Definisce un metodo per descrivere lo zoo.
        print("Guardians:")
        # Stampa una intestazione per gli zookeeper.
        for zoo_keeper in self.zoo_keepers:
        # Itera su tutti gli zookeeper nello zoo.
            print(zoo_keeper)
            # Stampa le informazioni di ogni zookeeper.
        print("Fences:")
        # Stampa una intestazione per i recinti.
        for fence in self.fences:
        # Itera su tutti i recinti nello zoo.
            print(fence)
            # Stampa le informazioni di ogni recinto.
            print("#" * 30)
            # Stampa una linea di separazione per distinguere i recinti.

"""PRINT"""
simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")
simba1 = Animal(name="Simba", species="Leone", age=5, height=2, width=2, preferred_habitat="Giungla")

savana = Fence(area=100, temperature=27, habitat="Savana")
zoo_keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")

print(f"L'area del fence Savana è {savana.area}")
zoo = Zoo(fences=[savana], zoo_keepers=[zoo_keeper])
zoo_keeper.add_animal(simba, savana)
zoo_keeper.add_animal(simba1, savana)
print(f"L'area del fence Savana è {savana.area}")
old_area = 0
for i in range(1000):
    zoo_keeper.feed(simba)
    if old_area == round(simba.area(), 3):
        break
    print(f"It={i+1} --> L'area residua del recinto è {round(simba.fence.area, 3)}")
    print(f"It={i+1} --> Simba è diventato grande = {round(simba.area(), 3)}")
    old_area = round(simba.area(), 3)
    
pumba = Animal(name="Pumba", species="Porco", age=25, height=2, width=5, preferred_habitat="Savana")
zoo_keeper.add_animal(pumba, savana)
zoo.describe_zoo()
"""Fine print"""
""""""