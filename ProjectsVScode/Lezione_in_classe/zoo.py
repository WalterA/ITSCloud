class Zoo:
    def __init__(self, fences:list, zoo_keepers:list):
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
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def __str__(self):
        return f"Fence(area={self.area}, temperature={self.temperature}, habitat={self.habitat})"

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:float):
        self.name = name.capitalize()
        self.surname = surname.capitalize()
        self.id = id

    def __str__(self):
        return f"ZooKeeper(name={self.name}, surname={self.surname}, id={self.id})"

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat and animal.height * animal.width <= fence.area:
            fence.animals.append(animal)
            fence.area -= animal.height * animal.width
        else:
            print("Non è possibile aggiungere l'animale al recinto.")

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
animale1 =Animal(name="Filippo" , species="tigre", age=10, height=2.5, width=3.3, preferred_habitat="foresta")
animale2 =Animal(name="Gigi" , species="tigre", age=2, height=4.6, width=3.4, preferred_habitat="foresta")
animale3 =Animal(name="Franco" , species="serpente", age=4, height=3.4, width=6.4, preferred_habitat="deserto")
animale4 =Animal(name="Pippo" , species="cane", age=5, height=1.5, width=2.6, preferred_habitat="bosco")
guardiano1 =ZooKeeper(name="gianfranco", surname="rossi", id=125)
guardiano2 =ZooKeeper(name="fabio", surname="bianco", id=155)
guardiano3 =ZooKeeper(name="gianni", surname="alb", id=455)
fence1=Fence(area=89, temperature=30, habitat="foresta")
fence2=Fence(area=50, temperature=30, habitat="deserto")
fence3=Fence(area=10000, temperature=30, habitat="bosco")
guardiano = ZooKeeper(name="gianfranco", surname="rossi", id=125)  # Crea un'istanza di ZooKeeper
guardiano.add_animal(animale1, fence3)  # Usa il metodo add_animal su quell'istanza
guardiano.add_animal(animale2,fence3)  #! risolvere problema doppio animale
print(animale1.health)