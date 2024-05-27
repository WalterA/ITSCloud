


import random


def dado ():
    dado = random.randint(1,10)
    print("numero dado:", dado)
    return dado


def mossa_tartaruga():
    """una funzione per calcolare la mossa della tartaruga       ___
    passo veloce" quando 1 ≤ tartaruga ≤ 5,
    una "scivolata" quando 6 ≤ tartaruga ≤ 7, o
    un "passo lento" quando 8 ≤ tartaruga ≤ 10."""
    tartaruga = 0
    mossa = dado()
    if mossa <= 5:
        return tartaruga + 3
    elif mossa == 6 or mossa == 7:
        return tartaruga - 6
    elif mossa > 8:
        return tartaruga + 1


        

def mossa_lepre():
    """una funzione per calcolare la mossa della lepre"""
    lepre = 0
    mossa = dado()
    if mossa <= 1 or mossa <= 2:
        return lepre
    elif mossa <= 3 or mossa <=4:
        return lepre + 9
    elif mossa == 5:
        return lepre -12
    elif mossa <= 6 or mossa <= 7 or mossa <= 8:
        return lepre + 1
    else:
        return lepre -2
    


def visualizzare_posizioni():
    """una funzione per visualizzare le posizioni sulla corsia di gara"""
    tartaruga : int = 0
    lepre : int = 0
    tartaruga = mossa_tartaruga()
    print("posizione attuale tarta",tartaruga)
    lepre = mossa_lepre()
    print("posizione attuale lepre", lepre)
    return tartaruga,lepre
#visualizzare_posizioni()

"""Implementare un loop per simulare i tick dell'orologio. 
Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.
 """
def loop ():
    """Implementare un loop per simulare tartaruga tick dell'orologio. 
    Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, 
    e determinare l'eventuale fine della gara."""
    conta_lepre = 0
    conta_tartaruga = 0

    
    while conta_tartaruga <= 70 and conta_lepre <= 70:
        
        if conta_lepre <= 70 and conta_tartaruga < 70:
            conta_lepre += mossa_lepre()
            conta_tartaruga += mossa_tartaruga()
        break
        
    return conta_lepre == 70 or conta_tartaruga == 70
        

loop()