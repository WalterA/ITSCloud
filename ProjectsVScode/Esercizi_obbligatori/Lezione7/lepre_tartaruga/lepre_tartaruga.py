import random
import unittest  # Importa il modulo random per generare numeri casuali

def dado():
    return random.randint(1, 10)  # Restituisce un numero casuale compreso tra 1 e 10

def ostacoli() -> dict[int, int]:
    percorso = list(range(1, 70))  # Crea una lista di numeri da 1 a 69 rappresentando il percorso della gara
    posizioni_bonus = percorso[1:70:15]  # Seleziona ogni 15esimo elemento a partire dall'indice 9

    # Effetti dei bonus (numero di quadrati in cui far avanzare l'animale)
    effetti_bonus = [-random.randint(1, 10) for _ in range(len(posizioni_bonus))]  # Crea una lista di effetti negativi casuali

    # Inizializziamo un dizionario vuoto per i bonus
    negativ_dict:dict[int,int] = {}

    # Riempiamo il dizionario con le posizioni dei bonus e gli effetti negativi
    for i in range(len(posizioni_bonus)):
        posizione_bonus = posizioni_bonus[i]
        effetto_bonus = effetti_bonus[i]
        negativ_dict[posizione_bonus] = effetto_bonus

    # Ritorniamo il dizionario
    return negativ_dict


def bonus() -> dict[int,int] :
    # Creiamo una lista da 1 a 70
    percorso = list(range(1, 71))
    posizioni_bonus = percorso[10:70:5]  # Seleziona ogni 5° elemento a partire dal decimo
    effetti_bonus = [random.randint(1, 10) for _ in range(len(posizioni_bonus))]  # Crea una lista di effetti casuali
    bonus_dict:dict[int,int] = {}

    # Riempiamo il dizionario con le posizioni dei bonus e i relativi effetti
    for i in range(len(posizioni_bonus)):
        posizione_bonus = posizioni_bonus[i]
        effetto_bonus = effetti_bonus[i]
        bonus_dict[posizione_bonus] = effetto_bonus

    # Ritorniamo il dizionario
    return bonus_dict

def mossa_tartaruga(energia:int, meteo:str):
    mossa = dado()  # Genera un numero casuale per determinare la mossa della tartaruga
    movimento:int = 0  # Inizializza la variabile di movimento della tartaruga
    if energia > 0:  # Se la tartaruga ha energia
        if 1 <= mossa <= 5:  # Se il numero casuale è tra 1 e 5 (Passo veloce)
            if energia >= 5:  # Se ha abbastanza energia per il passo veloce
                energia -= 5  # Decrementa l'energia per il passo veloce
                movimento = 3  # La tartaruga avanza di 3 quadrati
            else:
                energia += 10  # Altrimenti recupera 10 di energia
        elif 6 <= mossa <= 7:  # Se il numero casuale è tra 6 e 7 (Scivolata)
            if energia >= 10:  # Se ha abbastanza energia per la scivolata
                energia -= 10  # Decrementa l'energia per la scivolata
                movimento = -6  # La tartaruga scivola indietro di 6 quadrati
            else:
                energia += 10  # Altrimenti recupera 10 di energia
        else:  # Se il numero casuale è tra 8 e 10 (Passo lento)
            if energia >= 3:  # Se ha abbastanza energia per il passo lento
                energia -= 3  # Decrementa l'energia per il passo lento
                movimento = 1  # La tartaruga avanza di 1 quadrato
            else:
                energia += 10  # Altrimenti recupera 10 di energia
    else:  # Se la tartaruga è a corto di energia
        energia += 10  # Recupera 10 di energia
    if meteo == 'pioggia':  # Se il meteo è pioggia
        movimento -= 1  # Riduce il movimento della tartaruga di 1 quadrato

    return movimento, max(energia, 0)  # Ritorna il movimento della tartaruga e l'energia massima non negativa


def mossa_lepre(energia: int, meteo: str):
    mossa = dado()  # Genera un numero casuale per determinare la mossa della lepre
    movimento = 0  # Inizializza la variabile di movimento della lepre
    if energia > 0:  # Se la lepre ha energia
        if 1 <= mossa <= 2:  # Se il numero casuale è tra 1 e 2 (Riposo)
            energia += 10  # La lepre recupera 10 di energia
        elif 3 <= mossa <= 4:  # Se il numero casuale è tra 3 e 4 (Grande balzo)
            if energia >= 15:  # Se ha abbastanza energia per il grande balzo
                energia -= 15  # Decrementa l'energia per il grande balzo
                movimento = 9  # La lepre avanza di 9 quadrati
            else:
                energia += 10  # Altrimenti recupera 10 di energia
        elif mossa == 5:  # Se il numero casuale è 5 (Grande scivolata)
            if energia >= 20:  # Se ha abbastanza energia per la grande scivolata
                energia -= 20  # Decrementa l'energia per la grande scivolata
                movimento = -12  # La lepre scivola indietro di 12 quadrati
            else:
                energia += 10  # Altrimenti recupera 10 di energia
        elif 6 <= mossa <= 8:  # Se il numero casuale è tra 6 e 8 (Piccolo balzo)
            if energia >= 5:  # Se ha abbastanza energia per il piccolo balzo
                energia -= 5  # Decrementa l'energia per il piccolo balzo
                movimento = 1  # La lepre avanza di 1 quadrato
            else:
                energia += 10  # Altrimenti recupera 10 di energia
        else:  # Se il numero casuale è 9 o 10 (Piccola scivolata)
            if energia >= 8:  # Se ha abbastanza energia per la piccola scivolata
                energia -= 8  # Decrementa l'energia per la piccola scivolata
                movimento = -2  # La lepre scivola indietro di 2 quadrati
            else:
                energia += 10  # Altrimenti recupera 10 di energia
    else:  # Se la lepre è a corto di energia
        energia += 10  # Recupera 10 di energia

    if meteo == 'pioggia':  # Se il meteo è pioggia
        movimento -= 2  # Riduce il movimento della lepre di 2 quadrati

    return movimento, max(energia, 0)  # Ritorna il movimento della lepre e l'energia massima non negativa

def visualizzare_posizioni(conta_lepre:int, conta_tartaruga:int):
    corsia = ['_'] * 71  # Creiamo una lista di 71 elementi, inizialmente vuoti (quadrati sulla pista)
    if conta_lepre < 1:  # Se la posizione della lepre è inferiore a 1, la impostiamo a 1
        conta_lepre = 1
    if conta_tartaruga < 1:  # Se la posizione della tartaruga è inferiore a 1, la impostiamo a 1
        conta_tartaruga = 1
    if conta_lepre > 70:  # Se la posizione della lepre è superiore a 70, la impostiamo a 70
        conta_lepre = 70
    if conta_tartaruga > 70:  # Se la posizione della tartaruga è superiore a 70, la impostiamo a 70
        conta_tartaruga = 70
    if conta_lepre == conta_tartaruga:  # Se le posizioni di lepre e tartaruga coincidono
        corsia[conta_lepre] = 'OUCH!!!'  # Segnala l'incidente sulla pista
    else:  # Altrimenti
        corsia[conta_lepre] = 'H'  # Segnala la posizione della lepre sulla pista
        corsia[conta_tartaruga] = 'T'  # Segnala la posizione della tartaruga sulla pista
    print(''.join(corsia))  # Stampa la pista


def loop() -> None:
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")  # Messaggio di inizio gara
    conta_lepre = 0  # Inizializza la posizione della lepre a 0 (partenza)
    conta_tartaruga = 0  # Inizializza la posizione della tartaruga a 0 (partenza)
    tick = 0  # Contatore per tenere traccia del numero di turni
    energia_lepre = 100  # Inizializza l'energia della lepre a 100
    energia_tartaruga = 100  # Inizializza l'energia della tartaruga a 100
    meteo: str = ""
    while conta_lepre < 70 and conta_tartaruga < 70:  # Finchè nessuno dei due arriva al quadrato 70
        if tick % 10 == 0:  # Ogni 10 turni
            meteo = random.choice(['sole', 'pioggia'])  # Scegli casualmente il meteo (sole o pioggia)
        visualizzare_posizioni(conta_lepre, conta_tartaruga)  # Visualizza la posizione di lepre e tartaruga sulla pista

        movimento_lepre, energia_lepre = mossa_lepre(energia_lepre, meteo)  # Ottiene il movimento e aggiorna l'energia della lepre
        movimento_tartaruga, energia_tartaruga = mossa_tartaruga(energia_tartaruga, meteo)  # Ottiene il movimento e aggiorna l'energia della tartaruga

        conta_lepre += movimento_lepre  # Aggiorna la posizione della lepre
        conta_tartaruga += movimento_tartaruga  # Aggiorna la posizione della tartaruga

        conta_lepre = max(0, conta_lepre)  # Assicura che la posizione della lepre sia sempre >= 0
        conta_tartaruga = max(0, conta_tartaruga)  # Assicura che la posizione della tartaruga sia sempre >= 0

        ostacoli_dict = ostacoli()  # Ottiene un dizionario degli ostacoli
        for k, v in ostacoli_dict.items():  # Per ogni ostacolo nel dizionario
            if k == conta_lepre:  # Se l'ostacolo è nella posizione della lepre
                conta_lepre += v  # Aggiorna la posizione della lepre
            if k == conta_tartaruga:  # Se l'ostacolo è nella posizione della tartaruga
                conta_tartaruga += v  # Aggiorna la posizione della tartaruga

        bonus_dict = bonus()  # Ottiene un dizionario dei bonus
        for k, v in bonus_dict.items():  # Per ogni bonus nel dizionario
            if k == conta_lepre:  # Se il bonus è nella posizione della lepre
                conta_lepre += v  # Aggiorna la posizione della lepre
            if k == conta_tartaruga:  # Se il bonus è nella posizione della tartaruga
                conta_tartaruga += v  # Aggiorna la posizione della tartaruga

        tick += 1  # Incrementa il contatore dei turni

    visualizzare_posizioni(conta_lepre, conta_tartaruga)  # Visualizza la posizione finale di lepre e tartaruga

    if conta_lepre >= 70 and conta_tartaruga >= 70:  # Se entrambi hanno completato la gara
        print("IT'S A TIE.")  # Stampa che è un pareggio
    elif conta_lepre >= 70:  # Se la lepre ha completato la gara
        print("HARE WINS || YUCH!!!")  # Stampa che la lepre ha vinto
    elif conta_tartaruga >= 70:  # Se la tartaruga ha completato la gara
        print("TORTOISE WINS! || VAY!!!")  # Stampa che la tartaruga ha vinto

# if __name__ == "__main__":
#     unittest.main()

# loop()  # Esegui la funzione di loop per avviare la gara
