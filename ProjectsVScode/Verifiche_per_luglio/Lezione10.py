"""Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1"""

def transform(x: int) -> int:
    if x %2 == 0:  # Controlla se x è pari
        pari = x / 2  # Calcola il valore pari
        return int(pari)  # Restituisce il valore pari come intero
    else:
        dispari = (x*3 )-1  # Calcola il valore dispari
        return int(dispari) 
    
"""Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati.
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per
tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo."""

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate >= 40:  # Se le ore lavorate superano o sono uguali a 40
        tolte_40 = ore_lavorate - 40  # Calcola le ore eccedenti le prime 40
        prime_40 = 40 * 10  # Calcola lo stipendio per le prime 40 ore
        return (tolte_40 * 15) + prime_40  # Calcola lo stipendio totale con un tasso di 15 per le ore eccedenti
    else:
        prime_40 = ore_lavorate * 10  # Calcola lo stipendio per le prime 40 ore
        return prime_40  # Restituisce lo stipendio per le ore lavorate
"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 1, 2, 3, 4, 5, 6, 7
b) 3, 8, 13, 18, 23
c) 20, 14, 8, 2, -4, -10
d) 19, 27, 35, 43, 51"""

def print_seq(): 
    # Stampa della sequenza a)
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)
    print() 

    # Stampa della sequenza b)
    print("Sequenza b):")
    for i in range(3, 25, 5):
        print(i)
    print()

    # Stampa della sequenza c)
    print("Sequenza c):")
    for i in range(20, -11, -6):
        print(i)
    print()

    # Stampa della sequenza d)
    print("Sequenza d):")
    for i in range(19, 52, 8):
        print(i)
    print()
    
    return

"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente,
restituisca il risultato della potenza base^exponent. Supporre che base sia un numero intero
e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!"""

def integerPower(base, exponent):
    # Inizializza il risultato a 1
    risultato = 1
    # Itera attraverso il range dell'esponente
    for _ in range(exponent):
        # Moltiplica il risultato per la base
        risultato *= base
    # Restituisce il risultato
    return risultato

"""Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa 
di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float
(corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora."""

def hypotenuse(l1: float, l2: float):
    # Eleva il lato 1 al quadrato
    l1 **= 2
    # Eleva il lato 2 al quadrato
    l2 **= 2
    # Calcola la lunghezza dell'ipotenusa come radice quadrata della somma dei quadrati dei due lati
    return (l1 + l2) ** (1/2)
"""Scrivi una funzione che rimuove tutti i duplicati da una lista,
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi."""

def remove_duplicates(lista):
    # Crea una lista vuota per memorizzare gli elementi unici
    unique_items = []
    # Itera attraverso ogni elemento nella lista data
    for item in lista:
        # Verifica se l'elemento non è già presente nella lista degli elementi unici
        if item not in unique_items:
            # Se l'elemento non è presente, lo aggiunge alla lista degli elementi unici
            unique_items.append(item)
    # Restituisce la lista degli elementi unici
    return unique_items 
"""Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso come tre argomenti interi
(ore, minuti e secondi) e restituisca il numero dei secondi da quando l'orologio "ha battuto le 12" 
l'ultima volta (le ore 12, dunque, vengono considerate come orario di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi, ovvero sono passati
11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari,
entrambi espressi mediante ore, minuti e secondi. La funzione time_difference deve usare la
funzione seconds_since_noon per calcolare la quantità di tempo in secondi tra due orari,
entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi."""

def seconds_since_noon(ore, minuti, secondi):
    # Calcola i secondi trascorsi dalle ore del mattino fino al momento dato
    ore_second = ore * 3600
    minuti_second = minuti * 60
    return ore_second + minuti_second + secondi

def time_difference(ao, am, aS, bo, bm, bs):
    # Calcola i secondi trascorsi dalle ore del mattino fino al momento specificato per ogni ora
    time1 = seconds_since_noon(ao, am, aS)
    time2 = seconds_since_noon(bo, bm, bs)
    # Restituisce la differenza assoluta di tempo in secondi tra i due momenti specificati
    return abs(time1 - time2)
"""IN ALTERNATIVA"""
def seconds_since_noon(ore, minuti, secondi):
    ore_second = ore * 3600
    minuti_second = minuti * 60
    return ore_second + minuti_second + secondi

def time_difference(ao, am, aS, bo, bm, bs):
    # Calcola i secondi trascorsi dalle ore del mattino fino al momento specificato per ogni ora
    time1 = seconds_since_noon(ao, am, aS)
    time2 = seconds_since_noon(bo, bm, bs)
    
    # Calcola la differenza tra i due tempi
    difference = time1 - time2
    
    # Se la differenza è negativa, inverti i valori per ottenere il valore assoluto
    if difference < 0:
        difference = -difference
    
    return difference
"""PRINT"""
# # Test
# print(time_difference(1, 0, 0, 3, 15, 30))  # Expected output: 8130
# print(time_difference(0, 0, 0, 12, 0, 0))   # Expected output: 43200

"""Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza 
da terra in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza 
il valore della velocità corrente; poi, il valore della velocità viene modificato, sottraendo 96 
al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza
e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova 
la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"""

def rimbalzo() -> None:
    # Inizializzazione delle variabili
    tempo: int = 0  # Tempo trascorso
    altezza: float = 0.0  # Altezza della pallina
    velocita: float = 100.0  # Velocità della pallina
    rimbalzi: int = 0  # Numero di rimbalzi avvenuti
    
    # Ciclo finché non avvengono 5 rimbalzi
    while rimbalzi < 5:
        # Stampa tempo e altezza attuali
        print(f"Tempo: {tempo} Altezza: {altezza:}")
        
        # Aggiornamento dell'altezza e della velocità della pallina
        altezza += velocita
        velocita -= 96
        
        # Se la pallina raggiunge il suolo (altezza negativa), simula il rimbalzo
        if altezza < 0:
            # Inverte la direzione della pallina e riduce l'ampiezza del rimbalzo
            altezza *= -0.5
            velocita *= -0.5
            # Incrementa il contatore dei rimbalzi
            rimbalzi += 1
            # Incrementa il tempo trascorso e stampa il rimbalzo
            tempo += 1
            print(f"Tempo: {tempo} Rimbalzo!")
        
        # Incrementa il tempo trascorso ad ogni iterazione del ciclo
        tempo += 1

# # Chiamata alla funzione
# rimbalzo()

"""Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione.
Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi,
dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa,
deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l'
80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino)
da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello
spazio rimanente nel supporto di memorizzazione o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione 
originale del file, la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i 
blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte,
la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero 
di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso, la funzione deve
avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte,
la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio 
dei file è un numero intero pari a 1000 blocchi. """
def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
    for file in files:
        dimensione_compressa = file * 0.8  # Calcola la dimensione compressa del file
        blocchi_utilizzati = round(dimensione_compressa / 512)  # Arrotonda il numero di blocchi utilizzati
        blocchi_rimanenti = spazio_totale_blocchi - blocchi_utilizzati  # Calcola i blocchi rimanenti
        
        if blocchi_rimanenti >= 0:
            print(f"File di {file} byte compresso in {dimensione_compressa} byte e memorizzato. Blocchi usati: {blocchi_utilizzati}. Blocchi rimanenti: {blocchi_rimanenti}.")
            spazio_totale_blocchi -= blocchi_utilizzati  # Sottrae i blocchi utilizzati dallo spazio totale
        else:
            print(f"Non è possibile memorizzare il file di {file} byte. Spazio insufficiente.")



# Test
memorizza_file([1100, 20000, 1048576, 512, 5000])



