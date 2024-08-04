# #Aggiunta da Gpt per inserirlo in un html
# from flask import Flask, render_template, request
# import os

# app = Flask(__name__, template_folder='../html', static_folder='../css')

class Member:
    id = 0
    def __init__(self,name:str,email:str,password:str) -> None:
        self.name = name
        self.id:int = Member.id
        self.email=email
        self.password = password
        Member.id +=1 #per ogni nuovo oggetto aggiunge 1 per avere un id unico

    def get_id (self)->int:
        """Lettura ID"""
        print (f"Il tuo ID: {self.id}")

class Database():
    def __init__(self) -> None:
        self.registrazione:dict[int:list] = {}

    def controllo (self, membri:Member)->bool:
        """Controllo email e password"""
        dominio_email:list[str] = ["gmail.com",
                             "yahoo.com",
                             "ymail.com",
                             "rocketmail.com",
                             "outlook.com",
                             "hotmail.com",
                             "live.com"]

        map:list=["!",
                  "?",
                  "*",
                  "£",
                  "$",
                  "%",
                  "=",
                  "^",
                  "§"]

        num:int = ["1",
                   "2",
                   "3",
                   "4",
                   "5",
                   "6",
                   "7",
                   "8",
                   "9"]

        #Trovare il modo per ottimizzare le mappature delle liste

        nome , dominio =membri.email.split("@")

        if len(membri.password) >= 10:
            """Controllo carattere speciale"""
            for car in map:
                if car in membri.password:
                    break
            else:
                print('Deve contenere un carattere speciale')
                return False
        else:
            print( 'La password deve avere almeno 10 caratteri')
            return False

        for char in num:
            """Controllo presenza di numeri"""
            if char in membri.password:
                break
        else:
            print('inserisci almeno un numero')
            return False

        for dom in dominio_email:
            """Controllo dominio"""
            if dom in dominio:
                break
        else:
            print('Il dominio non è conforme')
            return False

        for mai in membri.password:
            """Controllo carattere maiuscolo"""
            if mai.isupper():
                break
        else:
            print("Deve avere almeno un carattere maiscolo")
            return False

        return True

#     def db_registra (self, membri:Member)->str:
#         """Registra nel Database"""
#         if self.controllo(membri):
#             if membri.id in self.registrazione:
#                 print("Sei già nel DataBase")
#             else:
#                 self.registrazione[membri.id]= [membri.name,membri.email,membri.password]
#                 print(f'Utente registrato con ID {membri.id}')
#         else:
#             print('Utente non registrato')

#     def tutti (self)->list:
#         """Stampa tutti i membri registrati"""
#         lista:list=[]
#         for k,v in self.registrazione.items():
#             lista.append([k,v])
#         return print(lista)
# #Aggiunta da Gpt per inserirlo in un html
# db = Database()

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         member = Member(name, email, password)
#         message = db.db_registra(member)
#         return render_template('pagReg.html', message=message, members=db.tutti())
#     return render_template('pagReg.html', members=db.tutti())

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='../html', static_folder='../html/css')

class Member:
    id = 0
    def __init__(self, name, email, password):
        self.name = name
        self.id = Member.id
        self.email = email
        self.password = password
        Member.id += 1

    def get_id(self):
        return self.id

class Database:
    def __init__(self):
        self.registrazione = {}

    def controllo(self, membri):
        dominio_email = ["gmail.com", "yahoo.com", "ymail.com", "rocketmail.com", "outlook.com", "hotmail.com", "live.com"]
        map = ["!", "?", "*", "£", "$", "%", "=", "^", "§"]
        num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        nome, dominio = membri.email.split("@")

        if len(membri.password) >= 10:
            for car in map:
                if car in membri.password:
                    break
            else:
                return False

        else:
            return False

        for char in num:
            if char in membri.password:
                break
        else:
            return False

        for dom in dominio_email:
            if dom in dominio:
                break
        else:
            return False

        for mai in membri.password:
            if mai.isupper():
                break
        else:
            return False

        return True

    def db_registra(self, membri):
        if self.controllo(membri):
            if membri.id in self.registrazione:
                return "Sei già nel DataBase"
            else:
                self.registrazione[membri.id] = [membri.name, membri.email, membri.password]
                return f'Utente registrato con ID {membri.id}'
        else:
            return 'Utente non registrato'

    def tutti(self):
        lista = []
        for k, v in self.registrazione.items():
            lista.append(v[0])  # Aggiungi solo il nome alla lista
        return lista

db = Database()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        member = Member(name, email, password)
        message = db.db_registra(member)
        return render_template('pagReg.html', message=message, members=db.tutti())
    return render_template('pagReg.html', members=db.tutti())

if __name__ == '__main__':
    app.run(debug=True)
