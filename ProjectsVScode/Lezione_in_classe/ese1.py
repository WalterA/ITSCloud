x = 5
y= 0

ok = x < 5 and y > x
print(ok)

"""
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
"""


def transform(x: int) -> int:
    if x %2 == 0:
        pari = x // 2
        return int(pari)
    else:
        dispari = (x //3 )-1 
        return int(dispari)

x=2
x=8
x=0
x=-5
x=16
print(transform(x))

"""Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. 
L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo."""

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate >= 40:
        tolte_40 = ore_lavorate - 40
        prime_40 = 40 * 10
        return (tolte_40 * 15) + prime_40
    else:
        prime_40 = ore_lavorate * 10
        return prime_40

print(calcola_stipendio(30))
"""Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a=[1, 2, 3, 4, 5, 6, 7]
b=[3, 8, 13, 18, 23]
c=[20, 14, 8, 2, -4, -10]
d=[19, 27, 35, 43, 51]"""
a=[1, 2, 3, 4, 5, 6, 7]
b=[3, 8, 13, 18, 23]
c=[20, 14, 8, 2, -4, -10]
d=[19, 27, 35, 43, 51]
def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)
    print() 

    print("Sequenza b):")
    for i in range(3,25,5):
        print(i)
    print()

    print("Sequenza c):")
    for i in range(20,-11,-6):
        print(i)
    print()

    print("Sequenza d):")
    for i in range(19,52,8):
        print(i)
    print()
    
    return
"""Scrivere una funzione chiamata integerPower che, dati in input una base e un esponente, 
restituisca il risultato della potenza base^exponent. 
Supporre che base sia un numero intero e che l'esponente sia un valore intero positivo e diverso da 0.
 
La funzione deve usare un ciclo come struttura di controllo per il calcolo del risultato.
Non utilizzare nessuna funzione della libreria math!"""
def integerPower(base:int,esponente:int):
        for _ in range(base,esponente):
            if int(base) and esponente != 0 and esponente >0:
                return base ** esponente
        
print(integerPower(5,3))

"""Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. 
La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.


Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora."""

def hypotenuse (l1: float,l2: float):
    l1 **= 2   
    l2 **= 2
    print((l1+l2)**(1/2))
    
hypotenuse(3.0, 4.0)
"""Scrivi una funzione che rimuove tutti i duplicati da una lista,
contenente sia numeri che lettere,
mantenendo l'ordine originale degli elementi."""
"""Scrivi una funzione che rimuove tutti i duplicati da una lista,
contenente sia numeri che lettere,
mantenendo l'ordine originale degli elementi."""
"""Scrivi una funzione che rimuove tutti i duplicati da una lista,
contenente sia numeri che lettere,
mantenendo l'ordine originale degli elementi."""
def remove_duplicates(lista):
    unique_items = []
    for item in lista:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

a=[1, 2, 3, 1, 2, 4]
print(remove_duplicates(a)) 

"""
Scrivere la funzione chiamata seconds_since_noon che riceva il tempo espresso 
come tre argomenti interi (ore, minuti e secondi) e restituisca il numero dei secondi da quando 
l'orologio "ha battuto le 12" l'ultima volta (le ore 12, dunque, vengono considerate come orario 
di partenza, dunque, come uno zero).

Ad esempio, alle ore 3:15:50 sono passate 3 ore, 15 minuti e 50 secondi,
ovvero sono passati 11750 secondi da quando l'orologio ha "battuto le 12" per l'ultima volta.

Definire, poi, la funzione chiamata time_difference che prende come argomento due orari, 
entrambi espressi mediante ore, minuti e secondi. 
La funzione time_difference deve usare la funzione seconds_since_noon per calcolare la 
quantità di tempo in secondi tra due orari, entrambi contenuti entro un ciclo dell'orologio di 12 ore.

Ad esempio, tra le ore 1:00 e 3:15:30 sono passati 8130 secondi.
"""   
def seconds_since_noon (ore,minuti,secondi):
    ore_second=ore* 3600
    minuti_second= minuti * 60
    return ore_second+ minuti_second + secondi

def time_difference(ao,am,aS,bo,bm,bs):
    time1=seconds_since_noon(ao,am,aS)
    time2=seconds_since_noon(bo,bm,bs)
    return time1-time2
print(seconds_since_noon(3,15,30))
    
"""Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia,
aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi,
il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, 
si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque,
per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a
cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"""
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    
    while rimbalzi <5:
        altezza = altezza + velocita
        velocita = velocita - 96
            
        if altezza<0:
            altezza *= -0.5 
            velocita *= -0.5 
            rimbalzi+=1
            tempo+= 1
            print(f"tempo:{tempo}, {rimbalzi}Rimbalzo!")
        tempo+=1
    return 
            
        
rimbalzo()
        

  