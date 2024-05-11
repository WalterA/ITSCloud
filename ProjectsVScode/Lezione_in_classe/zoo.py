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
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / self.age), 3)

    def __str__(self):
        return f"Animal(name={self.name}, species={self.species}, age={self.age})"

class Fence:
    def __init__(self, area:float, temperature:float, habitat:str):
        assert isinstance(area, (float, int)), "area deve essere un float o intero"
        assert isinstance(temperature, (float, int)), "temperature deve essere un float o intero"
        assert isinstance(habitat, str), "habitat deve essere una stringa"
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:float):
        assert isinstance(name, str), "name deve essere una stringa"
        assert isinstance(surname, str), "surname deve essere una stringa"
        assert isinstance(id, (float, int)), "id deve essere un float o intero"
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
            fence.area -= animal.height * animal.width
        else:
            print("Non è possibile aggiungere l'animale al recinto. Non c'è abbastanza spazio.")

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.height * animal.width

    def feed(self, animal: Animal, fence: Fence):
        if animal in fence.animals and animal.height * animal.width * 1.02 <= fence.area:
            animal.health = min(animal.health * 1.01, 100)
            animal.height *= 1.02
            animal.width *= 1.02
            fence.area -= animal.height * animal.width * 0.02
        else:
            print("Non è possibile nutrire l'animale.")

    def clean(self, fence: Fence):
        occupied_area = sum([animal.height * animal.width for animal in fence.animals])
        return occupied_area / (fence.area + occupied_area) if fence.area > 0 else occupied_area
    

        

#da cancellare
animale1 =Animal(name="ok" , species="tigre", age=10, height=2.5, width=3, preferred_habitat="foresta")
#animale2 =Animal(name="Filippo" , species="tigre", age=10, height=2.5, width=3.3, preferred_habitat="foresta")
#animale3 =Animal(name="Filippo" , species="serpente", age=4, height=3.4, width=6.4, preferred_habitat="foresta")
#animale4 =Animal(name="Pippo" , species="cane", age=5, height=1.5, width=2.6, preferred_habitat="bosco")
print(animale1.name)
# guardiano1 =ZooKeeper(name="gianfranco", surname="rossi", id=125)
# guardiano2 =ZooKeeper(name="fabio", surname="bianco", id=155)
# guardiano3 =ZooKeeper(name="gianni", surname="alb", id=455)
fence1=Fence(area=10, temperature=30, habitat="foresta")
print(fence1.area)
# fence2=Fence(area=50, temperature=30, habitat="deserto")
# fence3=Fence(area=10, temperature=30, habitat="bosco")
# guardiano = ZooKeeper(name="gianfranco", surname="rossi", id=125)  # Crea un'istanza di ZooKeeper
# guardiano.add_animal(animale1, fence1)  # Usa il metodo add_animal su quell'istanza
# guardiano.add_animal(animale2,fence1)  #
# guardiano.add_animal(animale3,fence1)
# print(animale1.health)