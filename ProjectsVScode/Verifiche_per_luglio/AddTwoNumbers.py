class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Crea un nodo testa fittizio per la lista dei risultati
        dummy_head = ListNode(0)
        # Puntatore corrente per costruire la nuova lista
        current = dummy_head
        # Variabile per tenere traccia del riporto (carry)
        carry = 0

        # Traversare entrambe le liste
        while l1 is not None or l2 is not None:
            # Ottieni i valori dai nodi correnti (o 0 se una lista è più corta)
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            # Calcola la somma e il nuovo riporto
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next

            # Passa ai nodi successivi nelle liste
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        # Se c'è un riporto rimasto dopo l'ultima somma, aggiungi un nuovo nodo
        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next

# Esempio di utilizzo:
# Creiamo due liste concatenate: 342 (rappresentato come 2 -> 4 -> 3) e 465 (rappresentato come 5 -> 6 -> 4)

# Lista concatenata 1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Lista concatenata 2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Aggiungere i due numeri
result = addTwoNumbers(l1, l2)

# Stampa il risultato: dovrebbe essere 7 -> 0 -> 8 (807)
while result is not None:
    print(result.val, end=" ")
    result = result.next
