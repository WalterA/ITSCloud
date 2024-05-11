class Zoo:
    def __init__(self, fences:list, zoo_keepers:list):
        assert isinstance(fences, list), "fences deve essere una lista"
        assert isinstance(zoo_keepers, list), "zoo_keepers deve essere una lista"
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    def describe_zoo(self):
        print("Guardians:")
        for keeper in self.zoo_keepers:
            print(keeper)
        print("\nFences:")
        for fence in self.fences:
            print(fence)
            print("\nwith animals:")
            for animal in fence.animals:
                print(animal)
            print("\n" + "#" * 30)

class Animal:
    def __init__(self, name:str , species:str, age:float, height:float, width:float, preferred_habitat:str):
        assert isinstance(name, str), "name deve essere una stringa"
        assert isinstance(species, str), "species deve essere una stringa"
        assert isinstance(age, (float, int)), "age deve essere un float o intero"
        assert isinstance(height, (float, int)), "height deve essere un float o intero"
        assert isinstance(width, (float, int)), "width deve essere un float o intero"
        assert isinstance(preferred_habitat, str), "preferred_habitat deve essere una stringa"
        self.name = name.capitalize()
        self.species = species
        self.age = round(age, 2)
        self.height = round(height, 2)
        self.width = round(width, 2)
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 2)

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"

class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        assert isinstance(area, (float, int)), "area deve essere un float o intero"
        assert isinstance(temperature, (float, int)), "temperature deve essere un float o intero"
        assert isinstance(habitat, str), "habitat deve essere una stringa"
        self.area = round(area, 2)
        self.temperature = round(temperature, 2)
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:float):
        assert isinstance(name, str), "name deve essere una stringa"
        assert isinstance(surname, str), "surname deve essere una stringa"
        assert isinstance(id, int), "id deve essere un intero"
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.id = id

    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"

    def add_animal(self, animal: Animal, fence: Fence):
        for existing_animal in fence.animals:
            if animal.__dict__ == existing_animal.__dict__:
                print("L'animale è già presente nel recinto.")
                return
        if animal.preferred_habitat == fence.habitat and animal.height * animal.width <= fence.area:
            fence.animals.append(animal)
            fence.area = round(fence.area - animal.height * animal.width, 2)
        else:
            print("Non è possibile aggiungere l'animale al recinto. Non c'è abbastanza spazio.")

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width
        else:
            print(f"L'animale {animal.name} non si trova nel recinto specificato.")


    def feed(self, fence: Fence):
        for animal in fence.animals:
            if round(animal.height * animal.width * 1.02, 2) <= fence.area:
                animal.health = min(round(animal.health * 1.01, 2), 100)
                animal.height = round(animal.height * 1.02, 2)
                animal.width = round(animal.width * 1.02, 2)
                fence.area = round(fence.area - animal.height * animal.width * 0.02, 2)
            else:
                print(f"Non è possibile nutrire uno degli animali. Non c'è abbastanza spazio nel recinto.")


    def clean(self, fence: Fence):
        occupied_area = sum([animal.height * animal.width for animal in fence.animals])
        return round((1 - occupied_area / (fence.area + occupied_area)) * 100, 2) if fence.area > 0 else 0

# Creazione di alcuni animali
animale1 = Animal(name="Leo", species="Leone", age=5, height=1.2, width=2.0, preferred_habitat="Savana")
animale2 = Animal(name="Tigro", species="Tigre", age=4, height=7.9, width=8.8, preferred_habitat="Giungla")
animale3 = Animal(name="fa", species="Tigre", age=4, height=5.9, width=9.8, preferred_habitat="Giungla")
animale4 = Animal(name="ge", species="Tigre", age=4, height=10.9, width=1.8, preferred_habitat="Giungla")
animale5 = Animal(name="re", species="Serpente", age=10, height=0.9, width=1.8, preferred_habitat="Deserto")

# Creazione di un recinto
recinto1 = Fence(area=20.0, temperature=24.0, habitat="Savana")
recinto2 = Fence(area=10.0, temperature=24.0, habitat="Foresta")
recinto3 = Fence(area=50.0, temperature=24.0, habitat="Deserto")
recinto4 = Fence(area=100.0, temperature=24.0, habitat="Giungla")

# Creazione di un guardiano dello zoo
guardiano1 = ZooKeeper(name="Mario", surname="Rossi", id=1)
guardiano2 = ZooKeeper(name="Sergio", surname="Rossi", id=12)
guardiano3 = ZooKeeper(name="Franco", surname="Rossi", id=13)

# Il guardiano aggiunge gli animali al recinto
guardiano1.add_animal(animale1, recinto1)
guardiano2.add_animal(animale2, recinto4)
guardiano3.add_animal(animale3, recinto4)
guardiano1.add_animal(animale4, recinto4)
guardiano2.add_animal(animale5, recinto3)
# Creazione dello zoo
zoo = Zoo(fences=[recinto1, recinto2, recinto3,recinto4], zoo_keepers=[guardiano1,guardiano2,guardiano3])

# Descrizione dello zoo
zoo.describe_zoo()

# Il guardiano nutre gli animali
guardiano1.feed(recinto1)
guardiano2.feed(recinto1)
guardiano3.feed(recinto1)
guardiano2.feed(recinto2)
guardiano3.feed(recinto2)
guardiano2.feed(recinto2)
guardiano3.feed(recinto3)
guardiano1.feed(recinto3)
guardiano1.feed(recinto3)
guardiano2.feed(recinto4)
guardiano3.feed(recinto4)
guardiano1.feed(recinto4)
guardiano1.feed(recinto4)

print(recinto1.area)
print(recinto2.area)
print(recinto3.area)
print(recinto4.area)

# Pulizia del recinto
pulizia = guardiano1.clean(recinto1)
print(f"Percentuale di area occupata nel recinto: {pulizia}")
pulizia2 = guardiano1.clean(recinto2)
print(f"Percentuale di area occupata nel recinto: {pulizia2}")
pulizia3 = guardiano1.clean(recinto3)
print(f"Percentuale di area occupata nel recinto: {pulizia3}")
pulizia4 = guardiano1.clean(recinto4)
print(f"Percentuale di area occupata nel recinto: {pulizia4}")
rimuovi=guardiano1.remove_animal(animale1, recinto1)
rimuovi=guardiano1.remove_animal(animale1, recinto1)
rimuovi=guardiano1.remove_animal(animale3, recinto4)
rimuovi=guardiano1.remove_animal(animale5, recinto4)
zoo.describe_zoo()
