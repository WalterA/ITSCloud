class Member:
    def __init__(self,name:str,id:str,registrazione:dict[list],email:str,password:str) -> None:
        self.name = name
        self.id = id
        self.registrazione = registrazione
        self.email=email
        self.password = password
        
    
class Database(Member):
    def __init__(self, name: str, id: str, registrazione: dict[list], email: str, password: str) -> None:
        super().__init__(name, id, registrazione, email, password)
    
    def controllo (self, membri:Member):
        dominio_email:list[str] = ["gmail.com",
                             "yahoo.com",
                             "ymail.com",
                             "rocketmail.com",
                             "outlook.com",
                             "hotmail.com",
                             "live.com"]
        map:list=["!","?","*","£","$","%","=","^","§"]
        nome , dominio =self.email.split("@")
        if dominio in dominio_email:
                if len(membri.password) >= 10:
                    if self.password in map:
                        
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
            
membri = Member("gigi","001","12.05.2024","gigi@ymail.com","Erjnjnass?")
google = Database()
print(google.controllo(membri))
print(google.database(membri))
print(google.get(membri))
