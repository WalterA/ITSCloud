check_number = False
check_special = False
check_upper = False
registration = True
 
while registration:
    with open("gestione.txt", "a") as reader:
        email = str(input("Insersci l'email "))
        password = str(input("Insersci la password con almeno un carattere speciale e un numero "))
        for char in password:
            if char.isnumeric():
                check_number = True
            if not char.isalnum():
                check_special = True
            if char.isupper():
                check_upper = True
        if check_upper and check_special and check_number:
            registration = False
            reader.write("\n")
            reader.write(email)
            reader.write("\n")
            reader.write(password)
            print("registrazione confermata")
        else:
            print("registrazione fallita")

login = True

while login:
    with open("gestione.txt", "r") as reader:
        file = reader.readlines()
        for i in range(len(file)):
            file[i] = file[i].strip("\n")
        check_email = str(input("Insersci l'email "))
        check_password = str(input("Insersci la password "))
        try:
            for i in range(len(file)):
                if file[i] == check_email and file[i+1] == check_password:
                    print("login effettuato con sucesso")
                    login = False
                    break
        except:
            print("utente o password errati")