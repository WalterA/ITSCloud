class Member:
    def __init__(self,name:str,id:str,registrazione,email:str,password:str) -> None:
        self.name = name
        self.id = id
        self.registrazione = registrazione
        self.email=email
        self.password = password
        
    
class Database:
    def __init__(self) -> None:
        self.db:dict = {}
    def database (self,membri:Member):
        
        if self.controllo(membri) ==True:
            self.db[membri.id] = [membri]
        else:
            return('controllo non conforme')
        
    def controllo (self, membri:Member):
        dominio:list[str] = ["gmail.com",
                             "yahoo.com",
                             "ymail.com",
                             "rocketmail.com",
                             "outlook.com",
                             "hotmail.com",
                             "live.com"]
        if membri.id not in self.db:
            nomeutente,dominio_email = membri.email.split("@")
            if dominio_email in dominio:
                if len(membri.password) >= 10:
                    if membri.password.endswith("!") and membri.password[0].isupper():
                        contiene_numero = False
                        for char in membri.password:
                            if '0' <= char <= '9':
                                contiene_numero = True
                                return True
                        
                        if not contiene_numero:
                            return 'inserisci almeno un numero'
                    else:
                        return 'La prima lettera deve essere maiuscola, deve terminare con \"!\"'
                else:
                    return 'La password deve avere almeno 10 caratteri'
            else:
                return 'Il dominio non è conforme'
    def get (self,membri:Member):
        return print(self.db.get(membri.id))
            
membri = Member("gigi","001","12.05.2024","gigi@ymail.com","Erjnjna7ss!")
google = Database()
print(google.database(membri))
print(google.get(membri))
