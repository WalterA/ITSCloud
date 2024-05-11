from user import User

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
