import random
def gioco_indovina_numero()->str:
    """GIOCA"""
    limite_inferiore = int(input("Inserisci il limite inferiore: "))
    limite_superiore = int(input("Inserisci il limite superiore: "))
    tentativi_massimi = int(input("Inserisci il numero di tentativi massimi: "))
    numero_segreto = random.randint(limite_inferiore, limite_superiore)
    tentativi = 0
    while tentativi < tentativi_massimi:
        tentativi += 1
        ipotesi_utente = int(input(f"Tentativo {tentativi}/{tentativi_massimi} - Indovina il numero: ")) 
        if ipotesi_utente == numero_segreto:
            print(f"Hai indovinato il numero! Il numero era {numero_segreto}")
            break
        elif ipotesi_utente < numero_segreto:
            print("Troppo basso!")
        else:
            print("Troppo alto!")
        if tentativi == tentativi_massimi:
            print(f"Hai perso! Il numero era {numero_segreto}")
#gioco_indovina_numero()
def gioco_alieno ()->str:
    """Gioco alieno"""
    punti:int=0
    while punti < 30:
        alien_color:str=input("Inserisci un colore alieno: ")
        if alien_color == "verde":
            punti+=5
            print("Hai guadagnato 5 punti")
        elif alien_color == "giallo":
            punti+=10
            print("Hai guadagnato 10 punti")
        elif alien_color == "rosso":
            punti+=15
            print("Hai guadagnato 15 punti")
        else:
            punti -= 5
            print("hai perso 5 punti")
        if punti >= 30:
            print( "Hai vinto")
    return "Hai perso"
#gioco_alieno()

def tombola() -> str:
    """Gioco tombola"""
    lista_nomi = []
    while True:
        nome = input("Inserisci un nome (o 'fine' per terminare): ").capitalize()
        if nome.lower() == "fine":
            break
        else:
            lista_nomi.append(nome)

    print("La lista dei nomi è:", lista_nomi)


tombola()
