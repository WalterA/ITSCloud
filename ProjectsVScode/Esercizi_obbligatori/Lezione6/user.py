
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
