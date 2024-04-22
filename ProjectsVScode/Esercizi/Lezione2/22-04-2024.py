# # def subtract_all(x:list[float], y :float) -> float:
# #     res:list[float] =[] 
# #     for elem in x:
# #         diff: float = elem - y
# #         res.append(diff)
# #     return res

# # x=[2,3,4,5,7]
# # y=4
# # print(subtract_all(x,y))

# mylist: list[float] = [1,2,3,4,5]
# y:list[float] = [2,3,4,5,6,7,9]
# def add_diff_to_rest(x,y, length:int):
#     res:list[float] =[]
#     for i in range(length):
#         diff=x[i]-y[i]
#         res.append(diff)
#     return res
# def subtract_posizione(x:list[float], y :list[float]) -> list[float]:
#         length=min(len(x),len(y))
#         res:list[float]=add_diff_to_rest(x,y,length)
#         return res
#         if len(x) >= len(y):
#            res= add_diff_to_rest(x,y,len(y))   
#         else:
#             res=add_diff_to_rest(x,y,len(x))
#         return res
# print(subtract_posizione(mylist,y))


#set e dizionari


s: str = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi matematici equivalenti della teoria, come la meccanica ondulatoria e la meccanica delle matrici; al contrario, ne esistono numerose e discordanti interpretazioni riguardo all'essenza ultima del cosmo e della natura, che hanno dato vita a un dibattito tuttora aperto nell'ambito della filosofia della scienza. La meccanica quantistica rappresenta, assieme alla teoria della relatività, uno spartiacque rispetto alla fisica classica, portando alla nascita della fisica moderna. Attraverso la teoria quantistica dei campi, generalizzazione della formulazione originale che include il principio di relatività ristretta, essa è a fondamento di molte altre branche della fisica, come la fisica atomica, la fisica della materia condensata, la fisica nucleare, la fisica delle particelle, la chimica quantistica."
#def counter(s:str) -> list[int, int, int, int]:
    # """
    #     questa funzione prende una stringa in input e restituisce una lista costriita nel modo seguente:
    #     -il primo elemento della lista contiene il numero di caratteri nella stringa
    #     -il secondo elemento della lista contiene il numero di parole nella stringa
    #     -il terzo elemento della lista contiene il numero di parole distinte nella stringa
    #     -il quarto elemento della lista contene il numero di frasi nella stringa
    # """
    # lista=s.split(" ")
    # print("i parole sono",len(lista))
    # print("le caratteri sono",len(s))
    # paroledistinte=set(s.split())
    # print("le parole distinte sono",len(paroledistinte))
    # lista=s.split(".")
    # print("le frasi sono",len(lista))
#fatta dal prof

def counter(s:str) -> list[int]:
    res=[]
    #quanti caratteri ha la stringa
    res.append=len(s)
    #quante parole ha la stringa
    res.append=len(s.split())
    #quante parole distinte ha la stringa
    parole=s.splint()
    parole_distinte=set(parole)
    res.append=len(parole_distinte)
    #quanti frasi ha la stringa
    res.append=len(s.splint(".")) -1  #oppure res[-1]=s.count(".")
    return res
counter(s)