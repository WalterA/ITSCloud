"""Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e 
viceversa a seconda del parametro to_fahrenheit.
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit."""
def convert_temperature(temp, to_fahrenheit=True):
# Definisce una funzione chiamata 'convert_temperature' che accetta due argomenti: 
# 'temp' (temperatura) e 'to_fahrenheit' (un booleano che indica se convertire in Fahrenheit,con valore predefinito True).

    if to_fahrenheit:
    # Controlla se l'argomento 'to_fahrenheit' è True. Se lo è, esegue il blocco di codice sottostante.

        return temp * 9/5 + 32
        # Converte la temperatura da Celsius a Fahrenheit usando la formula (temp * 9/5 + 32) e restituisce il risultato.

    else:
    # Se l'argomento 'to_fahrenheit' non è True (cioè, è False), esegue il blocco di codice sottostante.

        return (temp - 32) * 5/9
        # Converte la temperatura da Fahrenheit a Celsius usando la formula ((temp - 32) * 5/9) e restituisce il risultato.

"""Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino."""

def rounded_average(numbers: list[int]) -> int:
# Definisce una funzione chiamata 'rounded_average' che accetta una lista di numeri interi come
# argomento e restituisce un intero come risultato.

    media=(sum(numbers))/len(numbers)
    # Calcola la media dei numeri nella lista sommando tutti i numeri e dividendo 
    # per il numero totale di elementi nella lista.

    media=round(media)
    # Arrotonda il valore della media al numero intero più vicino.

    return media
    # Restituisce il valore arrotondato della media.
    
"""La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati."""

def find_element(lst: list[int], element: int) -> bool:
#Definisce una funzione chiamata 'find_element' che accetta una lista di interi (lst)
#e un intero (element) come argomenti e restituisce un booleano come risultato.
    
    for item in lst:
    # Itera su ciascun elemento della lista.

        if item == element:
        # Controlla se l'elemento corrente della lista è uguale all'elemento cercato.

            return True
            # Se trova l'elemento, restituisce True e interrompe l'iterazione.

    return False
    # Se l'elemento non viene trovato dopo aver iterato su tutta la lista, restituisce False.
    
"""Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere 
con un'operazione. L'operazione può procedere solo se la condizione A è vera o 
se entrambe le condizioni B e C sono vere. 
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a
seconda delle condizioni che sono soddisfatte."""

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
#Definisce una funzione chiamata 'check_combination' che accetta tre condizioni booleane 
# (conditionA, conditionB e conditionC) come argomenti e restituisce una stringa come risultato.

    if conditionA == True or (conditionB==True and conditionC==True): 
    # Verifica se conditionA è True oppure se sia conditionB che conditionC sono True. 
    # Se almeno una di queste condizioni è soddisfatta, esegue il blocco di codice successivo.

        return "Operazione permessa"
        # Se una delle condizioni è soddisfatta, restituisce la stringa "Operazione permessa".

    else:
    # Se nessuna delle condizioni è soddisfatta, esegue il blocco di codice successivo.

        return "Operazione negata"
        # Se nessuna delle condizioni è soddisfatta, restituisce la stringa "Operazione negata".

"""Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')'
sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude."""

def check_parentheses(expression: str) -> bool:
#Definisce una funzione chiamata 'check_parentheses' che accetta una stringa 
#(expression) come argomento e restituisce un booleano come risultato."""

    stack = []
    # Crea una lista vuota chiamata 'stack' che verrà utilizzata come pila per tenere traccia delle parentesi aperte.

    for char in expression:
    # Itera su ciascun carattere della stringa.

        if char == '(':
        # Se il carattere è una parentesi aperta, lo aggiunge alla pila.

            stack.append(char)

        elif char == ')':
        # Se il carattere è una parentesi chiusa:

            if not stack or stack.pop() != '(':
            # Verifica se la pila è vuota (che indica che non ci sono parentesi aperte corrispondenti) o
            # se l'ultimo elemento della pila non è una parentesi aperta.

                return False
                # Se una parentesi chiusa non ha una corrispondente parentesi aperta, restituisce False.

    return len(stack) == 0
    # Dopo aver attraversato tutta la stringa, verifica se la pila è vuota. Se è vuota, 
    # significa che tutte le parentesi aperte hanno una corrispondente parentesi chiusa e restituisce True,
    # altrimenti restituisce False.

"""Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi.
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali."""

def count_isolated(lista:list) -> int:
#Definisce una funzione chiamata 'count_isolated' che accetta una lista (lista)
#come argomento e restituisce un intero come risultato."""

    conta = 0
    # Inizializza una variabile 'conta' che conterà il numero di elementi isolati nella lista.

    if lista == []:
    # Verifica se la lista è vuota.

        return conta
        # Se la lista è vuota, restituisce immediatamente 0.

    else:
    # Se la lista non è vuota, esegue il blocco di codice successivo.

        for i in range(1, len(lista)-1):
        # Itera su ogni elemento della lista eccetto il primo e l'ultimo.

            if lista[i-1] != lista[i] and lista[i] != lista[i+1]:
            # Verifica se l'elemento corrente è diverso dai suoi vicini.

                conta += 1
                # Se l'elemento è isolato, incrementa il contatore 'conta'.

        if lista[0] != lista[1]:
        # Verifica se il primo elemento è diverso dal secondo.

            conta +=1
            # Se il primo elemento è isolato, incrementa il contatore 'conta'.

        if lista[-1] != lista[-2]:
        # Verifica se l'ultimo elemento è diverso dal penultimo.

            conta+=1
            # Se l'ultimo elemento è isolato, incrementa il contatore 'conta'.

        return conta
        # Restituisce il conteggio finale degli elementi isolati nella lista.

"""Scrivi una funzione che, 
dato un insieme e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista."""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
# Definisce una funzione chiamata 'remove_elements' che accetta due argomenti: 
# un insieme di interi (original_set) e una lista di interi (elements_to_remove),
# e restituisce un insieme di interi come risultato.

    mylist = list(original_set)
    # Converte l'insieme originale in una lista per poter iterare sui suoi elementi.

    nuova_lista = []
    # Inizializza una nuova lista vuota che conterrà gli elementi 
    # dell'insieme originale esclusi gli elementi da rimuovere.

    for i in mylist:
    # Itera su ogni elemento della lista.

        if i not in elements_to_remove:
        # Verifica se l'elemento corrente non è presente nella lista degli elementi da rimuovere.

            nuova_lista.append(i)
            # Se l'elemento non deve essere rimosso, lo aggiunge alla nuova lista.

    nuova_lista = set(nuova_lista)
    # Converte la nuova lista in un insieme.

    return nuova_lista
    # Restituisce l'insieme contenente gli elementi dell'insieme originale esclusi gli elementi da rimuovere.

"""Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori."""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
# Definisce una funzione chiamata 'merge_dictionaries' che accetta due dizionari (dict1 e dict2) 
# come argomenti e restituisce un nuovo dizionario come risultato.

    dizionario = dict1
    # Crea una copia del primo dizionario per modificare e restituire il risultato.

    for k, v in dict2.items():
    # Itera su ogni coppia chiave-valore nel secondo dizionario.

        if k in dizionario:
        # Verifica se la chiave è già presente nel dizionario.

            dizionario[k] += v
            # Se la chiave è già presente, aggiorna il valore sommando il valore corrispondente del secondo dizionario.

        else:
        # Se la chiave non è presente nel dizionario, esegue il blocco di codice successivo.

            dizionario[k] = v
            # Aggiunge la nuova coppia chiave-valore al dizionario.

    return dizionario
    # Restituisce il dizionario risultante dopo la fusione dei due dizionari.




