"""Dato l'inizio di una lista collegata semplice, restituisci True se è un palindromo.
Modella i concetti di Nodo e Lista Collegata utilizzando classi.
"""
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
# Definizione della classe Node che rappresenta un nodo nella lista collegata. 
# Ogni nodo ha un attributo 'value' per memorizzare il valore del nodo e un attributo
# 'next' per memorizzare il riferimento al prossimo nodo nella lista.

class LinkedList:
    def __init__(self):
        self.head = None
# Definizione della classe LinkedList che rappresenta una lista collegata.
# Ogni lista ha un attributo 'head' che punta al primo nodo nella lista.

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
# Metodo 'append' per aggiungere un nuovo nodo con il valore specificato 
# alla fine della lista collegata. Se la lista è vuota, il nuovo nodo diventa 
# la testa della lista. Altrimenti, scorre la lista fino all'ultimo nodo e aggiunge il nuovo nodo alla fine.

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
# Metodo 'to_list' che converte la lista collegata in una lista Python standard.
# Scorre la lista collegata e aggiunge i valori di ogni nodo alla lista risultante.

def is_palindrome(head: Node) -> bool:
# Definizione della funzione is_palindrome che verifica se una lista collegata è un palindromo. 
# Prende come input il nodo iniziale della lista collegata e restituisce True se è un palindromo, altrimenti False.

    # Trova il centro della lista collegata
    slow = fast = head
    # Inizializza due puntatori slow e fast all'inizio della lista.

    stack = []
    # Inizializza uno stack vuoto per memorizzare la prima metà degli elementi della lista.

    # Usa uno stack per memorizzare la prima metà degli elementi
    while fast and fast.next:
    # Finché fast e il successivo di fast non sono entrambi None
    # (ovvero finché ci sono almeno due elementi successivi nella lista):
        stack.append(slow.value)
        # Aggiunge il valore del nodo puntato da slow allo stack.
        slow = slow.next
        # Muove il puntatore slow avanti di un nodo.
        fast = fast.next.next
        # Muove il puntatore fast avanti di due nodi.

    # Se la lista collegata ha un numero dispari di elementi, salta l'elemento centrale
    if fast:
    # Se fast non è None (ovvero se la lista ha un numero dispari di elementi):
        slow = slow.next
        # Salta il nodo centrale muovendo il puntatore slow avanti di un nodo.

    # Confronta la seconda metà con i valori nello stack
    while slow:
    # Finché slow non diventa None (ovvero finché ci sono nodi nella seconda metà della lista):
        if slow.value != stack.pop():
        # Se il valore del nodo puntato da slow non è uguale al valore estratto dall'ultimo elemento dello stack:
            return False
            # La lista non è un palindromo, quindi restituisce False.
        slow = slow.next
        # Muove il puntatore slow avanti di un nodo.

    return True
    # Se il ciclo è stato completato senza restituire False, 
    # significa che la lista è un palindromo, quindi restituisce True.
    
"""print"""
# ll1 = LinkedList()
# for value in [1, 2, 3, 2, 1]:
#     ll1.append(value)
# print(is_palindrome(ll1.head))

"""Ti vengono dati due array di interi nums1 e nums2, 
ordinati in ordine non decrescente, e due interi m e n,
che rappresentano il numero di elementi in nums1 e nums2 rispettivamente. 
Scrivi una funzione per unire nums1 e nums2 in un singolo array ordinato in ordine non decrescente.

L'array finale ordinato non deve essere restituito dalla funzione,
ma deve essere memorizzato all'interno dell'array nums1. 
Per farlo, nums1 ha una lunghezza di m + n, dove i primi m elementi denotano 
gli elementi che devono essere uniti, e gli ultimi n elementi sono impostati 
su 0 e devono essere ignorati. nums2 ha una lunghezza di n."""

def merge(nums1, m, nums2, n):
    # Inizializza gli indici:
    # i - indice dell'ultimo elemento valido di nums1
    # j - indice dell'ultimo elemento di nums2
    # k - indice dell'ultima posizione disponibile in nums1 (m + n - 1)
    i, j, k = m - 1, n - 1, m + n - 1

    # Loop finché ci sono elementi da confrontare sia in nums1 che in nums2
    while i >= 0 and j >= 0:
        # Confronta l'elemento corrente di nums1 con l'elemento corrente di nums2
        if nums1[i] >= nums2[j]:
            # Se l'elemento in nums1 è maggiore o uguale, mettilo nella posizione corrente di k in nums1
            nums1[k] = nums1[i]
            i -= 1  # Decrementa l'indice i
        else:
            # Se l'elemento in nums2 è maggiore, mettilo nella posizione corrente di k in nums1
            nums1[k] = nums2[j]
            j -= 1  # Decrementa l'indice j
        k -= 1  # Decrementa l'indice k per spostarsi alla posizione precedente

    # Copia eventuali elementi rimanenti di nums2 in nums1
    # (Se ci sono ancora elementi in nums2 che non sono stati copiati)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1  # Decrementa l'indice j
        k -= 1  # Decrementa l'indice k
"""Dato head, l'inizio di una lista collegata, determina se la lista 
collegata ha un ciclo. C'è un ciclo in una lista collegata se c'è un 
nodo nella lista che può essere raggiunto di nuovo seguendo continuamente 
il puntatore next. Internamente, pos viene utilizzato per indicare l'indice 
del nodo a cui è collegato il puntatore next della coda. Nota che pos non 
viene passato come parametro. Restituisci True se c'è un ciclo nella lista collegata. 
Altrimenti, restituisci False.

Modella i concetti di Nodo e Lista Collegata utilizzando classi."""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    # Definisce un nodo della lista collegata con un valore (value) e un puntatore al nodo successivo (next).

class LinkedList:
    def __init__(self):
        self.head = None
    # Definisce una lista collegata con un puntatore all'inizio della lista (head).

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    # Aggiunge un nuovo nodo con il valore specificato alla fine della lista collegata.
    # Se la lista è vuota (self.head è None), crea il nodo iniziale.
    # Altrimenti, attraversa la lista fino all'ultimo nodo e aggiunge il nuovo nodo alla fine.

    def get_node(self, index):
        current = self.head
        count = 0
        while current and count < index:
            current = current.next
            count += 1
        return current
    # Ritorna il nodo alla posizione specificata (index) nella lista collegata.
    # Se l'indice è fuori dai limiti della lista, ritorna None.

    def create_cycle(self, pos):
        if pos == -1:
            return
        cycle_node = self.get_node(pos)
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = cycle_node
    # Crea un ciclo nella lista collegata collegando l'ultimo nodo al nodo alla posizione specificata (pos).
    # Se pos è -1, non fa nulla.
    # Ottiene il nodo alla posizione pos e lo collega all'ultimo nodo della lista.

def has_cycle(head: Node) -> bool:
    if not head or not head.next:
        return False
    # Se la lista è vuota o contiene solo un nodo, non c'è ciclo.

    slow = head
    fast = head
    # Inizializza due puntatori, slow e fast, entrambi puntati al nodo iniziale.

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    # Utilizza l'algoritmo dei due puntatori (tartaruga e lepre) per rilevare un ciclo.
    # I due puntatori si muovono a velocità diverse: slow si muove di un passo e fast di due passi.
    # Se i due puntatori si incontrano, c'è un ciclo e la funzione ritorna True.

    return False
    # Se il ciclo termina senza che i puntatori si incontrino, non c'è ciclo e la funzione ritorna False.
    
"""PRINT"""
# ll1 = LinkedList()
# for i in range(5):
#     ll1.append(i)
# node1 = ll1.get_node(1)  # Node with value 1
# node4 = ll1.get_node(4)  # Node with value 4
# node4.next = node1  # Creating a cycle

"""Dato un stringa `s` che consiste di lettere maiuscole o minuscole, 
scrivi una funzione che restituisca la lunghezza del palindromo più lungo che può essere costruito con quelle lettere.
Le lettere sono case sensitive, ad esempio, "Aa" non è considerato un palindromo qui."""
def longest_palindrome(s: str) -> int:
    char_counts = {}  # Crea un dizionario per contare le occorrenze di ciascun carattere
    for char in s:
        if char in char_counts:
            char_counts[char] += 1  # Incrementa il conteggio del carattere se è già presente nel dizionario
        else:
            char_counts[char] = 1  # Aggiungi il carattere al dizionario con un conteggio iniziale di 1

    length = 0  # Inizializza la lunghezza del palindromo a 0
    odd_exists = False  # Flag per controllare se esiste almeno un carattere con conteggio dispari
    for count in char_counts.values():
        # Aggiungi alla lunghezza del palindromo il numero di coppie di ogni carattere
        length += (count // 2) * 2

        if count % 2 == 1:
            odd_exists = True  # Se esiste un carattere con conteggio dispari, imposta il flag a True

    # Se esiste almeno un carattere con conteggio dispari, aggiungi 1 alla lunghezza del palindromo
    if odd_exists:
        length += 1

    return length  # Ritorna la lunghezza del palindromo più lungo possibile

"""Implementa uno stack LIFO (last-in-first-out) utilizzando solo due code. 
Lo stack implementato dovrebbe supportare tutte le funzioni di uno stack normale (push, top, pop e empty).

Implementa la classe MyStack:

push(x: int) -> None: Aggiunge l'elemento x in cima allo stack.
pop() -> int: Rimuove l'elemento in cima allo stack e lo restituisce.
top() -> int: Restituisce l'elemento in cima allo stack senza rimuoverlo.
empty() -> bool: Restituisce true se lo stack è vuoto, altrimenti false."""

class Queue:
    def __init__(self):
        self.data = []  # Inizializza una lista vuota per memorizzare gli elementi della coda

    def push(self, x):
        self.data.append(x)  # Aggiunge l'elemento x alla fine della coda

    def pop(self):
        return self.data.pop(0)  # Rimuove e restituisce il primo elemento della coda

    def empty(self):
        return len(self.data) == 0  # Restituisce True se la coda è vuota, altrimenti False


class MyStack:
    def __init__(self):
        self.q1 = Queue()  # Inizializza la prima coda vuota
        self.q2 = Queue()  # Inizializza la seconda coda vuota

    def push(self, x: int) -> None:
        self.q1.push(x)  # Aggiunge l'elemento x alla prima coda

    def pop(self) -> int:
        while len(self.q1.data) > 1:  # Trasferisce tutti gli elementi tranne l'ultimo dalla prima coda alla seconda
            self.q2.push(self.q1.pop())
        popped = self.q1.pop()  # Rimuove l'ultimo elemento rimasto nella prima coda
        self.q1, self.q2 = self.q2, self.q1  # Scambia i riferimenti delle due code
        return popped  # Restituisce l'elemento rimosso

    def top(self) -> int:
        while len(self.q1.data) > 1:  # Trasferisce tutti gli elementi tranne l'ultimo dalla prima coda alla seconda
            self.q2.push(self.q1.pop())
        top = self.q1.pop()  # Rimuove l'ultimo elemento rimasto nella prima coda
        self.q2.push(top)  # Rimette l'elemento rimosso nella seconda coda
        self.q1, self.q2 = self.q2, self.q1  # Scambia i riferimenti delle due code
        return top  # Restituisce l'elemento rimosso

    def empty(self) -> bool:
        return self.q1.empty()  # Restituisce True se la prima coda è vuota, altrimenti False
"""Dato una stringa s contenente solo i caratteri '(', ')', '{', '}', '[' e ']',
scrivi una funzione per determinare se la stringa di input è valida.

Una stringa di input è valida se:

Le parentesi aperte devono essere chiuse dallo stesso tipo di parentesi.
Le parentesi aperte devono essere chiuse nell'ordine corretto.
Ogni parentesi di chiusura deve avere una corrispondente parentesi di apertura dello stesso tipo."""
def is_valid_parenthesis(s: str) -> bool:
     # Definisce una funzione chiamata is_valid_parenthesis che prende una stringa s come argomento e restituisce un valore booleano.

    stack = []
     # Inizializza uno stack vuoto. Lo stack verrà utilizzato per tenere traccia delle parentesi aperte.

    bracket_map = {"(": ")", "[": "]",  "{": "}"}
#     # Definisce un dizionario che mappa le parentesi di apertura alle corrispondenti parentesi di chiusura.

    for char in s:
#         # Inizia un ciclo for per ogni carattere nella stringa s.
        
        if char in bracket_map:
#             # Se il carattere corrente è una parentesi di apertura:
            stack.append(char)
#             # Aggiunge il carattere allo stack.
        
        elif bracket_map[stack.pop()] != char:
             # Se il carattere corrente è una parentesi di chiusura:
             # Rimuove e restituisce l'elemento in cima allo stack. Quindi, cerca il carattere di chiusura corrispondente nel dizionario.
             # Confronta il carattere di chiusura previsto con il carattere corrente.
             # Se non corrispondono, la funzione restituisce False.
            return False

    return len(stack) == 0
#     # Alla fine del ciclo, se lo stack è vuoto, significa che tutte le parentesi di apertura hanno avuto una corrispondente parentesi di chiusura nel giusto ordine.
#     # Restituisce True se lo stack è vuoto, altrimenti False.
"""ALTERNATIVA"""
def is_valid_parenthesis(s: str) -> bool:
    # Inizializza uno stack per memorizzare le parentesi aperte
    stack = []
    # Mappa delle parentesi aperte e chiuse
    bracket_map = {"(": ")", "[": "]",  "{": "}"}

    # Itera su ciascun carattere nella stringa di input
    for char in s:
        # Se il carattere è una parentesi aperta, aggiungilo allo stack
        if char in bracket_map:
            stack.append(char)
        # Se il carattere è una parentesi chiusa
        elif not stack or bracket_map[stack.pop()] != char:
            # Se lo stack è vuoto o se la parentesi chiusa non corrisponde alla parentesi aperta più recente nello stack, restituisci False
            return False

    # Alla fine, se lo stack è vuoto, tutte le parentesi aperte sono state chiuse correttamente
    # Altrimenti, se lo stack non è vuoto, ci sono parentesi aperte non chiuse
    return not stack


	
# print(is_valid_parenthesis("(]"))
	
# print(is_valid_parenthesis("([)]"))

