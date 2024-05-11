
# * Nicola Walter Albano

"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.

9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. 

9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.

9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
# * 9.1 / 9.2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance
restaurant = Restaurant("The Culinary Spot", "Italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Cafe Delight", "Cafe")
restaurant2 = Restaurant("Spice Bazaar", "Indian")
restaurant3 = Restaurant("Sushi House", "Japanese")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# * 9.3
# 9-3. Users
class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
        
    @classmethod
    def lista(cls, users):
        lista = [user.describe_user() for user in users]
        return lista

# Creating instances
user1 = User("John", "Doe", "johndoe", "johndoe@example.com")
user2 = User("Jane", "Doe", "janedoe", "janedoe@example.com")
user3 = User("Jim", "Beam", "jimbeam", "jimbeam@example.com")
lista=[user1, user2, user3]
User.lista(lista)

# * 9.4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nome del ristorante: {self.restaurant_name}")
        print(f"Tipo di cucina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} è ora aperto!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Creazione di un'istanza
restaurant = Restaurant("La Trattoria", "Italiana")
print(f"Numero di clienti serviti: {restaurant.number_served}")

# Modifica del valore e stampa di nuovo
restaurant.number_served = 20
print(f"Numero di clienti serviti: {restaurant.number_served}")

# Uso del metodo set_number_served()
restaurant.set_number_served(30)
print(f"Numero di clienti serviti: {restaurant.number_served}")

# Uso del metodo increment_number_served()
restaurant.increment_number_served(5)
print(f"Numero di clienti serviti: {restaurant.number_served}")

# * 9.5

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Informazioni Utente:")
        print(f"Nome: {self.first_name}")
        print(f"Cognome: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Ciao, {self.first_name} {self.last_name}! Bentornato!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creazione di un'istanza
user = User("Giovanni", "Rossi", "gio_rossi", "gio.rossi@example.com")

# Incremento dei tentativi di accesso
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Stampa del numero di tentativi di accesso
print(f"Tentativi di accesso: {user.login_attempts}")

# Reimpostazione dei tentativi di accesso
user.reset_login_attempts()

# Stampa del numero di tentativi di accesso dopo la reimpostazione
print(f"Tentativi di accesso: {user.login_attempts}")

# * 9.6

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nome del ristorante: {self.restaurant_name}")
        print(f"Tipo di cucina: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, gusti):
        super().__init__(restaurant_name, cuisine_type)
        self.gusti = gusti

    def mostra_gusti(self):
        print("I gusti di gelato disponibili sono:")
        for gusto in self.gusti:
            print(f"- {gusto}")

# Creazione di un'istanza
gelateria = IceCreamStand("Gelato Paradiso", "Gelateria", ["Cioccolato", "Vaniglia", "Fragola"])
gelateria.mostra_gusti()

# * 9.7

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Informazioni Utente:")
        print(f"Nome: {self.first_name}")
        print(f"Cognome: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Ciao, {self.first_name} {self.last_name}! Bentornato!")

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = ["può aggiungere post", "può eliminare post", "può bannare l'utente"]

    def show_privileges(self):
        print("Privilegi dell'amministratore:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Creazione di un'istanza
admin = Admin("Mario", "Bianchi", "mario_bianchi", "mario.bianchi@example.com")
admin.show_privileges()

# * 9.8

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Informazioni Utente:")
        print(f"Nome: {self.first_name}")
        print(f"Cognome: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Ciao, {self.first_name} {self.last_name}! Bentornato!")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privilegi dell'amministratore:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(["può aggiungere post", "può eliminare post", "può bannare l'utente"])

# Creazione di un'istanza
admin = Admin("Mario", "Bianchi", "mario_bianchi", "mario.bianchi@example.com")
admin.privileges.show_privileges()

# * 9.9

class Battery:
    def __init__(self, battery_size=60):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Questa auto ha una batteria da {self.battery_size}-kWh.")

    def get_range(self):
        if self.battery_size == 60:
            range = 200
        elif self.battery_size == 65:
            range = 245

        message = f"Questa auto può andare circa {range}"
        message += " miglia con una carica completa."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

# Creazione di un'auto elettrica
my_tesla = ElectricCar('tesla', 'model s', 2019)

# Chiamata a get_range() una volta
my_tesla.battery.get_range()

# Aggiornamento della batteria
my_tesla.battery.upgrade_battery()

# Chiamata a get_range() una seconda volta
my_tesla.battery.get_range()

# * 9.10

# main.py
from restaurant import Restaurant

# Creazione di un'istanza di Restaurant
ristorante = Restaurant("La Trattoria", "Italiana")

# Chiamata di un metodo di Restaurant
ristorante.describe_restaurant()

# * 9.11

from user import Admin

# Creazione di un'istanza di Admin
admin = Admin("Mario", "Bianchi", "mario_bianchi", "mario.bianchi@example.com")
admin.privileges.show_privileges()

# * 9.12
from admin import Admin

# Creazione di un'istanza di Admin
admin = Admin("Mario", "Bianchi", "mario_bianchi", "mario.bianchi@example.com")
admin.privileges.show_privileges()

# * 9.13

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# Creazione di un dado a 6 facce e tiro 10 volte
die_6 = Die(6)
for i in range(10):
    print(die_6.roll_die())

# Creazione di un dado a 10 facce e tiro 10 volte
die_10 = Die(10)
for i in range(10):
    print(die_10.roll_die())

# Creazione di un dado a 20 facce e tiro 10 volte
die_20 = Die(20)
for i in range(10):
    print(die_20.roll_die())
# * 9.14

import random

# Creazione di una lista con 10 numeri e 5 lettere
lotteria = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Selezione casuale di 4 numeri o lettere
vincitori = random.sample(lotteria, 4)

print("Qualsiasi biglietto che corrisponde a questi 4 numeri o lettere vince un premio:")
for vincitore in vincitori:
    print(vincitore)

# * 9.15

import random

# Creazione di una lista con 10 numeri (come stringhe) e 5 lettere
lotteria = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E']

# Creazione del mio biglietto
my_ticket = ['1', '2', 'A', 'B']

# Contatore per il numero di tentativi
tentativi = 0

while True:
    tentativi += 1
    estratti = random.sample(lotteria, 4)
    estratti.sort()
    my_ticket.sort()
    if estratti == my_ticket:
        break

print(f"Il tuo biglietto ha vinto dopo {tentativi} tentativi!")








