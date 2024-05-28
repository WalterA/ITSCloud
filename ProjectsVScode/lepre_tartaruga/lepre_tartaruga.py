

import random
percorso = ["_"*70]

def dado ():
    dado = random.randint(1,10)
    return dado


def mossa_tartaruga(energia):
    """una funzione per calcolare la mossa della tartaruga"""

    mossa = dado()
    if energia <= 0:
        
        if 1 <= mossa <= 5:
            energia -= 5
            
            return 3, energia  # Passo veloce avanti
        elif 6 <= mossa <= 7:
            energia -= 10
            
            return -6, energia  # Scivolata indietro
        else:
            energia -= 3
            
            return 1, energia  # Passo lento avanti
    else:
        energia += 10
        
        return 0, energia

  

def mossa_lepre(energia):
  
    mossa = dado()
    if energia <= 0:
        
        if 1 <= mossa <= 2:
            energia += 10
            return 0, energia  # La lepre dorme
        elif 3 <= mossa <= 4:
            energia -= 15
            
            return 9 , energia # Salto grande avanti
        elif mossa == 5:
            energia -= 20
            
            return -12, energia  # Scivolata grande indietro
        elif 6 <= mossa <= 8:
            energia -= 5
            
            return 1, energia  # Salto piccolo avanti
        else:
            energia -= 8
            
            return -2 , energia # Scivolata piccola indietro
    else: 
        energia += 10
        return 0, energia

def visualizzare_posizioni(conta_lepre,conta_tartaruga):
    """Mostra la posizione sulla corsia di gara."""
    corsia = ['_'] * 71
    if conta_lepre < 0:
        conta_lepre = 0
    if conta_tartaruga < 0:
        conta_tartaruga = 0
    if conta_lepre > 70:
        conta_lepre = 70
    if conta_tartaruga > 70:
        conta_tartaruga = 70
    if conta_lepre == conta_tartaruga:
        corsia[conta_lepre] = 'OUCH!!!'  # Collisione
    else:
        corsia[conta_lepre] = 'H'
        corsia[conta_tartaruga] = 'T'
    for pos in corsia:
        print(pos, end="")
    print()  # Nuova linea alla fine

def loop ():
    """Implementare un loop per simulare tartaruga tick dell'orologio. 
    Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, 
    e determinare l'eventuale fine della gara."""
    print("'BANG !!!!! AND THEY'RE OFF !!!!!'")
    conta_lepre = 0
    conta_tartaruga = 0
    tick = 0
    energia_lepre = 100
    energia_tartaruga = 100
    
    while True:

        meteo = random.choice(['sole', 'pioggia'])
        visualizzare_posizioni(conta_lepre, conta_tartaruga)
      
        movimento_lepre, energia_lepre = mossa_lepre(energia_lepre)
        movimento_tartaruga, energia_tartaruga = mossa_tartaruga(energia_tartaruga)
            
        print(energia_lepre)
        print(energia_tartaruga)
        conta_lepre += movimento_lepre
        conta_tartaruga += movimento_tartaruga
        
        tick += 1
        if tick % 10 == 0:
            if meteo == "sole":
                pass
            else:
                conta_lepre = -2
                conta_tartaruga = -1
                print("piove si torna indieto")
                
        visualizzare_posizioni(conta_lepre, conta_tartaruga)
        if conta_lepre >= len(percorso) or conta_tartaruga >= len(percorso):
            break
       
    if conta_lepre >= len(percorso):
        print("HARE WINS || YUCH!!!")
    elif conta_tartaruga >= len(percorso):
        print("TORTOISE WINS! || VAY!!!")
    else:
        print("IT'S A TIE.")
loop()