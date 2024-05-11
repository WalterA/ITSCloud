# restaurant.py
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nome del ristorante: {self.restaurant_name}")
        print(f"Tipo di cucina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} è ora aperto!")
