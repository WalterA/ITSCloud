class Zoo:
    def __init__(self, fences:list, zoo_keepers:list):
        """Costruttore della classe Zoo"""
        #Verifica che i recinti e i guardiani siano liste
        assert isinstance(fences, list), "fences deve essere una lista"
        assert isinstance(zoo_keepers, list), "zoo_keepers deve essere una lista"
        # Inizializza i recinti e i guardiani dello zoo
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        """Metodo per descrivere lo zoo"""
        print("Guardians:")
        # Stampa i dettagli di ogni guardiano
        for keeper in self.zoo_keepers:
            print(keeper)
        print("\nFences:")
        # Stampa i dettagli di ogni recinto e degli animali al suo interno
        for fence in self.fences:
            print(fence)
            print("\nwith animals:")
            for animal in fence.animals:
                print(animal)
            print("\n" + "#" * 30)

class Animal:
    def __init__(self, name:str , species:str, age:float, height:float, width:float, preferred_habitat:str):
        """Costruttore della classe Animal"""
        # Verifica che i parametri siano del tipo corretto
        assert isinstance(name, str), "name deve essere una stringa"
        assert isinstance(species, str), "species deve essere una stringa"
        assert isinstance(age, (float, int)), "age deve essere un float o intero"
        assert isinstance(height, (float, int)), "height deve essere un float o intero"
        assert isinstance(width, (float, int)), "width deve essere un float o intero"
        assert isinstance(preferred_habitat, str), "preferred_habitat deve essere una stringa"
        # Inizializza le proprietà dell'animale
        self.name = name.capitalize()
        self.species = species
        self.age = round(age, 2)
        self.height = round(height, 2)
        self.width = round(width, 2)
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 2)
    def __str__(self):
        """Metodo per rappresentare l'animale come stringa"""
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"

class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        """Costruttore della classe Fence"""
        # Verifica che i parametri siano del tipo corretto
        assert isinstance(area, (float, int)), "area deve essere un float o intero"
        assert isinstance(temperature, (float, int)), "temperature deve essere un float o intero"
        assert isinstance(habitat, str), "habitat deve essere una stringa"
        # Inizializza le proprietà del recinto
        self.area = round(area, 2)
        self.temperature = round(temperature, 2)
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        """Metodo per rappresentare il recinto come stringa"""
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:float):
        """Costruttore della classe ZooKeeper"""
        # Verifica che i parametri siano del tipo corretto
        assert isinstance(name, str), "name deve essere una stringa"
        assert isinstance(surname, str), "surname deve essere una stringa"
        assert isinstance(id, int), "id deve essere un intero"
        # Inizializza le proprietà del guardiano dello zoo
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.id = id

    def __str__(self):
        """Metodo per rappresentare il guardiano dello zoo come stringa"""
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"

    def add_animal(self, animal: Animal, fence: Fence):
        """Metodo per aggiungere un animale a un recinto"""
        # Verifica se l'animale è già nel recinto
        for existing_animal in fence.animals:
            if animal.__dict__ == existing_animal.__dict__:
                print("L'animale è già presente nel recinto.")
                return
        # Verifica se l'habitat preferito dell'animale corrisponde a quello del recinto e se c'è abbastanza spazio nel recinto
        if animal.preferred_habitat == fence.habitat and animal.height * animal.width <= fence.area:
            # Aggiunge l'animale al recinto e riduce l'area del recinto
            fence.animals.append(animal)
            fence.area = round(fence.area - animal.height * animal.width, 2)
        else:
            print("Non è possibile aggiungere l'animale al recinto. Non c'è abbastanza spazio.")

    def remove_animal(self, animal: Animal, fence: Fence):
        """Metodo per rimuovere un animale da un recinto"""
        # Verifica se l'animale si trova nel recinto
        if animal in fence.animals:
            # Rimuove l'animale dal recinto e aumenta l'area del recinto
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
        else:
            print(f"L'animale {animal.name} non si trova nel recinto specificato.")

    def feed(self, animal: Animal):
        """Metodo per nutrire un animale"""
        # Calcola le nuove dimensioni dell'animale dopo essere stato nutrito
        new_height = animal.height * 1.02
        new_width = animal.width * 1.02
        # Verifica se l'animale si trova in un recinto con abbastanza spazio
        for fence in self.fences:
            if animal in fence.animals and new_height * new_width <= fence.area:
                # Aumenta la salute dell'animale del 1%
                animal.health = min(animal.health * 1.01, 100)
                # Aumenta le dimensioni dell'animale del 2%
                animal.height = new_height
                animal.width = new_width
                # Riduce l'area del recinto
                fence.area -= new_height * new_width - animal.height * animal.width
                return
        print(f"Non è possibile nutrire l'animale {animal.name}. Non c'è abbastanza spazio nel recinto.")


    def clean(self, fence: Fence):
        """Metodo per pulire un recinto"""
        # Calcola l'area occupata dagli animali nel recinto
        occupied_area = sum([animal.height * animal.width for animal in fence.animals])
        # Restituisce la percentuale di area occupata nel recinto
        cleaning_time = occupied_area / (fence.area + occupied_area) if fence.area > 0 else occupied_area
        return round(cleaning_time, 2)

# Creazione di un animale
animal = Animal("Leo", "Lion", 5, 1.2, 0.5, "Savannah")
print(animal)  # Stampa: Animal(name=Leo, species=Lion, age=5)

# Creazione di un recinto
fence = Fence(100.0, 25.0, "Savannah")
print(fence)  # Stampa: Fence(area=100.0, temperature=25.0, habitat=Savannah)

# Creazione di un guardiano dello zoo
zoo_keeper = ZooKeeper("Mario", "Rossi", 1)
print(zoo_keeper)  # Stampa: ZooKeeper(name=Mario, surname=Rossi, id=1)

# Aggiunta dell'animale al recinto
zoo_keeper.add_animal(animal, fence)
# Non stampa nulla, ma l'animale viene aggiunto al recinto

# Rimozione dell'animale dal recinto
zoo_keeper.remove_animal(animal, fence)
# Non stampa nulla, ma l'animale viene rimosso dal recinto

# Nutrizione dell'animale
zoo_keeper.feed(animal)
# Non stampa nulla, ma la salute e le dimensioni dell'animale vengono aumentate

# Pulizia del recinto
cleaning_time = zoo_keeper.clean(fence)
print(cleaning_time)  # Stampa il tempo di pulizia del recinto

# Creazione dello zoo
zoo = Zoo([fence], [zoo_keeper])
zoo.describe_zoo()  # Stampa i dettagli dei guardiani e dei recinti dello zoo

