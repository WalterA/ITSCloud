class Zoo:

    def __init__(self, fences:str, zoo_keepers:list):
        self.fences: list = fences
        self.zoo_keepers: list = zoo_keepers

    # def describe_zoo():

class Animal:

    def __init__(self, name:str , species:str, age:float, height:float, width:float, preferred_habitat:str, health:float):
        self.name: str = name.capitalize()
        self.species: str = species
        self.age: float = age
        self.height:float = height
        self.width:float = width
        self.preferred_habitat:str = preferred_habitat

    def health (self):
        self.health:float = 100 * (1 / self.age)


class Fence:

    def __init__(self,area:float, temperature:float, habitat:str):
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat

class ZooKeeper:

    def __init__(self, name:str, cognome:str, id:float):
        self.name: str = name.capitalize()
        self.cognome: str = cognome.capitalize()
        self.id: float = id

    def add_animal(animal: Animal, fence: Fence):
        lista=[]
        if animal not in fence:
            lista.append()






    # def remove_animal(animal: Animal, fence: Fence):

    # def feed(animal: Animal):

    # def clean(fence: Fence):

    
        

#da cancellare
animale1 =Animal(name="Filippo" , species="tigre", age=10, height=2.5, width=3.3, preferred_habitat="foresta")
animale2 =Animal(name="Gigi" , species="leopardo", age=2, height=4.6, width=3.4, preferred_habitat="foresta")
animale3 =Animal(name="Franco" , species="serpente", age=4, height=3.4, width=6.4, preferred_habitat="deserto")
guardiano1 =ZooKeeper(name="gianfranco", cognome="rossi", id=125)
guardiano2 =ZooKeeper(name="fabio", cognome="bianco", id=155)
guardiano3 =ZooKeeper(name="gianni", cognome="alb", id=455)
fence1=Fence(area=89, temperature=30, habitat="foresta")
fence2=Fence(area=50, temperature=30, habitat="deserto")
fence3=Fence(area=100, temperature=30, habitat="bosco")