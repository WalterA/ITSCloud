
#------LEZIONE 7----------


#Scrivi una funzione che riceve una lista di numeri, 
# filtra i numeri pari,
# e restituisce una nuova lista con i numeri pari moltiplicati per un fattore
#dato.
def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    nuova_lista:list=[]
    for i in range(len(lista_numeri)):
        if lista_numeri[i] %2 == 0:
            nuova_lista.append(lista_numeri[i] * fattore)

    return nuova_lista
# print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))# [6, 12, 18] [6, 12, 18] 
# print(filtra_moltiplica([2, 4, 6, 8], 2))# [4, 8, 12, 16] [4, 8, 12, 16] 
# print(filtra_moltiplica([1, 3, 5], 10))# [] [] 
# print(filtra_moltiplica([10, 20, 30, 40], 5))# [50, 100, 150, 200] [50, 100, 150, 200] 
# print(filtra_moltiplica([], 3))# []

#Scrivi una funzione che determina se un numero è 'magico'.
# Un numero è considerato magico se è divisibile per 4 ma non per 6.
def numero_magico(num: int) -> bool:
    return num % 4 ==0 and num % 6 != 0


# print(numero_magico(8)) #True True 
# print(numero_magico(12)) #False False 
# print(numero_magico(16)) #True True 
# print(numero_magico(24)) #False False 
# print(numero_magico(28)) #True True


#Scrivi una funzione che elimini dalla lista dati certi elementi 
# specificati in un contactionario. Il contactionario contiene elementi da rimuovere come
#chiavi e il numero di volte che devono essere rimossi come valori.
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
        lista_risultato = lista.copy()
        for k,v in da_rimuovere.items():
            conta= 0
            while v > conta:
                if k in lista:
                    lista_risultato.remove(k)
                    conta+=1
                else:
                        break
        return lista_risultato

# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1})) #[1, 3, 2, 4] [1, 3, 2, 4] 
# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) #[1, 3, 4] [1, 3, 4] 
# print(rimuovi_elementi([1, 1, 1, 1], {1: 2})) #[1, 1] [1, 1] 
# print(rimuovi_elementi([4, 5, 6], {1: 3})) #[4, 5, 6] [4, 5, 6] 
# print(rimuovi_elementi([], {2: 1})) #[]

#Scrivi una funzione che prenda in input una lista di contactionari che 
# rappresentano voti di studenti e aggrega i voti per studente in un nuovo
#contactionario
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_aggregati={}
    for entry in voti:
        nome=entry['nome']
        voto=entry['voto']
        if nome in voti_aggregati:
            voti_aggregati[nome].append(voto)
        else:
            voti_aggregati[nome]=[voto]
    return voti_aggregati
# print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob',
# 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
# # {'Alice': [90, 85],
# # 'Bob': [75]}
# # {'Alice': [90, 85],
# # 'Bob': [75]}
# # 
# print(aggrega_voti([{'nome': 'Alice', 'voto': 100}]))# {'Alice': [100]} {'Alice': [100]} 
# print(aggrega_voti([{'nome': 'Bob', 'voto': 75}, {'nome': 'Bob',
# 'voto': 85}]))
# #{'Bob': [75, 85]} {'Bob': [75, 85]} 
# print(aggrega_voti([]))# {} {} 
# print(aggrega_voti([{'nome': 'Carl', 'voto': 60}, {'nome': 'Carl',
# 'voto': 70}, {'nome': 'Carl', 'voto': 80}]))

#Scrivi una funzione che accetti un contactionario di prodotti con i prezzi 
# e restituisca un nuovo contactionario con solo i prodotti che hanno un prezzo
#superiore a 20, scontati del 10%.

def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:
    contact:dict={}
    for nome,prezzo in prodotti.items():
        if prezzo > 20:
            sconto = (prezzo*10) / 100
            scontato = prezzo - sconto  
            contact[nome]=round(scontato,2)
     
    return contact

# print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0,
# 'Quaderno': 22.0}))
# # {'Zaino': 45.0,
# # 'Quaderno': 19.8}
# # {'Zaino': 45.0,
# # 'Quaderno': 19.8}
# print(filtra_e_mappa({'Tavolo': 120.0, 'Sedia': 85.0})) #{'Tavolo': 108.0, 'Sedia':76.5}
# # {'Tavolo': 108.0, 'Sedia':
# # 76.5}
# print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))# {} {} 
# print(filtra_e_mappa({'Lampada': 35.0, 'Libro': 19.0}))# {'Lampada': 31.5} {'Lampada': 31.5} 
# print(filtra_e_mappa({}))# {} {} 

#PARTE 1
#Scrivi una funzione chiamata create_contact() che accetta il nome e cognome,
# e-mail (facoltativo) e numero di telefono (facoltativo). La
#funzione dovrebbe restituire un contactionario con i dettagli del contatto.
#PARTE 2
#Scrivi una funzione chiamata update_contact() che accetta il contactionario creato, 
# il nome e cognome del contatto da aggiornare, e il dettaglio
#facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il contactionario del contatto.



def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contact = {'profile': name}
    if email:
        contact["email"]=email
    else:
        contact["email"]= None

    if telefono:
        contact["telefono"]=telefono
    else:
        contact["telefono"]= None
    return contact


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if dictionary['profile'] == name:
        if email:
            dictionary['email'] = email
        if telefono:
            dictionary['telefono'] = telefono
    return dictionary
# contact = create_contact("Mario Rossi",
# email="mario.rossi@gmail.com",
# telefono=788787)
# print(create_contact("Mario Rossi",
# email="mario.rossi@gmail.com",
# telefono=788787))
# print(update_contact(contact, "Mario Rossi", telefono=123456789))
# # {'profile': 'Mario Rossi', 'email':
# # 'mario.rossi@gmail.com',
# # 'telefono': 788787}
# # {'profile': 'Mario Rossi', 'email':
# # 'mario.rossi@gmail.com',
# # 'telefono': 123456789}
# # {'profile': 'Mario Rossi', 'email':
# # 'mario.rossi@gmail.com',
# # 'telefono': 788787}
# # {'profile': 'Mario Rossi', 'email':
# # 'mario.rossi@gmail.com',
# # 'telefono': 123456789}
# contact = create_contact("Laura Neri",
# email="laura.neri@domain.com")
# print(create_contact("Laura Neri",
# email="laura.neri@domain.com"))
# print(update_contact(contact, "Laura Neri", email="laura.new@domain.com",
# telefono=84736736))
# # {'profile': 'Laura Neri', 'email':
# # 'laura.neri@domain.com',
# # 'telefono': None}
# # {'profile': 'Laura Neri', 'email':
# # 'laura.new@domain.com', 'telefono':
# # 84736736}
#---Lezione9-----------------------------------------------------------------------------------------------------
#Data una stringa s e una lista di stringhe wordDict,
# restituisce True se s può essere segmentato in una sequenza separata da spazi
# di una o più parole del dizionario; False altrimenti.
def word_break(s: str, wordDict: list[str]) -> bool:
    for i in wordDict:
        if i in wordDict:
            s = s.replace(i, "")
    if s == "":
        return True
    else:
        return False
# print(word_break("leetcode",["leet","code"]))
# print(word_break("applepenapple", ["apple","pen"]))
# print(word_break("catsandog",["cats","dog","sand","and","cat"]))


















#----LEZIONE10------------------------------------------------------------------------------------------------
# Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
def transform(x: int) -> int:
    if x % 2== 0:
        return int( x/2)
    else:
        return int((x * 3)-1)
# print(transform(4)) #2 2 
# print(transform(3)) #8 8 
# print(transform(0)) #0 0 
# print(transform(-10))# -5 -5 
# print(transform(-5)) #-16 -16 

#Sviluppare una funzione in Python per calcolare lo stipendio
# lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le
#prime 40 ore di lavoro e paga "una volta e mezza" la paga 
# oraria per tutte le ore di lavoro oltre le 40 ore.
#Per ogni operaio, viene fornito il numero di ore che tale
# impiegato ha lavorato durante la settimana.
#La vostra funzione deve ricevere questa informazione per 
# ogni impiegato e determinare e stampare lo stipendio lordo.

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        return float(ore_lavorate*10)
    else:
        straordinari:int= ore_lavorate - 40
        ore_normali=40*10
        return float((straordinari*15) + ore_normali)
# print(calcola_stipendio(40)) #400.0 400 
# print(calcola_stipendio(30)) #300.0 300 
# print(calcola_stipendio(45)) #475.0 475 
# print(calcola_stipendio(60))# 700.0 700 
# print(calcola_stipendio(0)) #0.0
#Scrivere in Python dei
#cicli
#che stampino le seguenti sequenze di valori:
#a) 1, 2, 3, 4, 5, 6, 7
#b) 3, 8, 13, 18, 23
#c) 20, 14, 8, 2, -4, -10
#d) 19, 27, 35, 43, 51

# for i in range(1,8):
#     print(i)
# for i in range(3,25,5):
#     print(i)
# for i in range(20,-11,-6):
#     print(i)
# for i in range(19,52,8):
#     print(i)

# Scrivere una funzione chiamata integerPower che, dati in input una 
# base e un esponente, restituisca il risultato della
# potenza base^exponent. Supporre che base sia un numero intero e che 
# l'esponente sia un valore intero positivo e diverso da 0.
# La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
# Non utilizzare nessuna funzione della libreria math!
def integerPower(base, exponent):
    risultato = 1
    for _ in range(exponent):
        risultato *= base
    return risultato
# print(integerPower(3, 4)) #81 81 
# print(integerPower(5, 3))# 125 125 
# print(integerPower(2, 5)) #32 32 
# print(integerPower(10, 2)) #100

# Definire una funzione chiamata hypotenuse che calcoli la lunghezza 
# dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due
# argomenti di tipo float (corrispondenti ai due lati del triangolo) e 
# restituire l'ipotenusa come un float.
# Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
def hypotenuse (l1: float,l2: float):
    l1 **= 2
    l2 **= 2
    return((l1+l2)**(1/2))
#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
def remove_duplicates(lista):
    lista_copia=[]
    for i in lista:
        if i not in lista_copia:
            lista_copia.append(i)
    return lista_copia
# print(remove_duplicates([1, 2, 3, 1, 2, 4])) #[1, 2, 3, 4] [1, 2, 3, 4] 
# print(remove_duplicates([4, 5, 'a', 4, 6])) #[4, 5, 'a', 6] [4, 5, 'a', 6] 
# print(remove_duplicates(['a', 'b', 'a'])) #['a', 'b'] ['a', 'b'] 
# print(remove_duplicates([1, 1, 1, 1])) #[1] [1] 
# print(remove_duplicates([]))

# Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi (ore, minuti e secondi) e restituisca
# il numero dei secondi da quando l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza,
# dunque, come uno zero).
# Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati 11750 secondi da quando l'orologio ha "battuto
# le 12" per l'ultima volta.
# Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, entrambi espressi mediante ore, minuti e secondi.
# La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari, entrambi
# contenuti entro un ciclo dell'orologio di 12 ore.
# Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
def seconds_since_noon (ore,minuti,secondi):
    ore_second=ore* 3600
    minuti_second= minuti * 60
    return ore_second+ minuti_second + secondi
def time_difference(ao,am,aS,bo,bm,bs):
    time1=seconds_since_noon(ao,am,aS)
    time2=seconds_since_noon(bo,bm,bs)
    return abs(time1-time2)
# Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo, a mano amano che il tempo passa su un orologio simulato.
# Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.
# Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, il valore dellavelocità viene modificato, sottraendo 96 al valore della velocità corrente.
# Dunque, dopo ogni secondo, si ha che
# altezza = altezza + velocità
# velocità = velocità - 96
# .
# Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque,per il rimbalzo, si avrà che
# altezza= altezza*-0,5
# velocità=velocità*-0,5
# .
# Ci si fermi al quinto rimbalzo.
# Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
# Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
# "Tempo: 0 Altezza: 0"
# Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
# Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
# "Tempo: 4 Rimbalzo!"
def rimbalzo() -> None:
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza:}")
        altezza += velocita
        velocita -= 96
        if altezza<0:
            altezza *= -0.5
            velocita *= -0.5
            rimbalzi += 1
            tempo+= 1
            print(f"Tempo: {tempo} Rimbalzo!")
        tempo+=1
# Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. 
# Prima che il file compresso vengamemorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
# Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi,
# dove ogni valore intero della listarappresenta la dimensione non compressa di un singolo file espressa in byte.
# Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve 
# calcolare la dimensione compressa di talefile espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa),
# calcolare il numero di blocchi (arrotondato al numerointero più vicino) da 512 byte necessari per la memorizzazione, al fine di 
# determinare se il file compresso può essere salvato nello spaziorimanente nel supporto di memorizzazione o meno.
# In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file,
# la dimensionecompressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione.
# Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
# "File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
# Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un
# numero di blocchi più grande di quellirimasti disponibili sul supporto di memorizzazione. In tal caso, la 
# funzione deve avvisare l'utente che lo spazio disponibile sul supporto dimemorizzazione non è sufficiente per salvare il file.
# Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
# "Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
# Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000blocchi.
# def memorizza_file(files:list[int])->None:
#     spazio_totale_blocchi=1000
#     for i in files:
#         if i == 
