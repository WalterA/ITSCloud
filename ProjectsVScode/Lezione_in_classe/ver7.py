"""Scrivi una funzione che riceve una lista di numeri, 
filtra i numeri pari, e restituisce una nuova lista con i numeri 
pari moltiplicati per un fattore dato.
For example:

Test	Result
print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3)) 
[6, 12, 18]
print(filtra_moltiplica([], 3))
[]
"""
def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    listap=[]
    for i in range(len(lista_numeri)):
        if lista_numeri[i] % 2 == 0 and lista_numeri[i] != 1:
            pari = lista_numeri[i] * fattore
            listap.append(pari)
    
    return listap

    
    
    
    


# print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))
# print(filtra_moltiplica([], 3))

"""Scrivi una 
funzione che determina se un numero è 'magico'. Un numero è 
magico se è divisibile per 4 ma non per 6."""
def numero_magico(num: int) -> bool:
    return num % 4 == 0 and num % 6 != 0
# print(numero_magico(8))

# print(numero_magico(12))

"""Scrivi una funzione che elimini dalla lista dati certi elementi
specificati in un dizionario. Il dizionario contiene elementi da rimuovere 
come chiavi e il numero di volte che devono essere rimossi come valori."""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int, int]) -> list[int]:
    lista_risultato = lista.copy()
    
    for elemento, volte in da_rimuovere.items():
        conteggio = 0
        while conteggio < volte:
            if elemento in lista_risultato:
                lista_risultato.remove(elemento)
                conteggio += 1
            else:
                break
    
    return lista_risultato

# # Esempio di utilizzo
# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))  # Output: [1, 3, 4]
# print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 1}))  # Output: [1, 3, 2, 4]
# print(rimuovi_elementi([1, 2, 2, 2, 4], {2: 2}))  # Output: [1, 2, 4]
# print(rimuovi_elementi([1, 2, 3, 4], {5: 1}))    # Output: [1, 2, 3, 4] (elemento non presente)

"""Scrivi una funzione che prenda in input una lista di
dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario."""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    voti_aggregati = {}
    
    for entry in voti:
        nome = entry['nome']
        voto = entry['voto']
        
        if nome in voti_aggregati:
            voti_aggregati[nome].append(voto)
        else:
            voti_aggregati[nome] = [voto]
    
    return voti_aggregati
#print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))

"""Scrivi una funzione che accetti un dizionario di prodotti con i prezzi
e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%."""
def filtra_e_mappa(prodotti: dict[str, float]) -> dict[str, float]:
    prezzi_scontati = {}
    
    for prodotto, prezzo in prodotti.items():
        if prezzo > 20:
            prezzo_scontato = prezzo * 0.90  # Applica uno sconto del 10%
            prezzi_scontati[prodotto] = round(prezzo_scontato, 2)  # Arrotonda a 2 cifre decimali
    
    return prezzi_scontati

# Esempi di utilizzo
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))  # Output: {'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0}))  # Output: {}

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))
{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 


