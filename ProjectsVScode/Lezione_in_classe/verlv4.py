# """
# Scrivi una funzione che accetta una stringa come input, rimuove le 
# parole non significative comuni stop_words e restituisce un dizionario in 
# cui le chiavi sono parole univoche nel testo rimanente 
# (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura)
# e i valori sono le frequenze di quelle parole."""


# def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
#     punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     cleaned_text = ''.join([char.lower() if char not in punctuation else ' ' for char in text])
    

#     words = cleaned_text.split()
    

#     def recursive_count(words, stopwords, word_counts):
#         if not words:
#             return word_counts
#         word = words[0]
#         if word in stopwords:
#             return recursive_count(words[1:], stopwords, word_counts)
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#         return recursive_count(words[1:], stopwords, word_counts)
    
    
#     word_counts = {}
#     return recursive_count(words, stopwords, word_counts)

# stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
# text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
# print(word_frequency(text, stopwords))

# """Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!

# Qual è il problema?

# Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).

# Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!
# """

# def is_subsequence(s: str, t: str) -> bool:
#     it = iter(t)
    

#     return all(char in it for char in s)
	
# print(is_subsequence("abc", "cab"))

# """Data una lista di numeri interi, riordina i 
# numeri in modo che tutti i numeri pari appaiano prima 
# di tutti i numeri dispari. Restituisce l'elenco riorganizzato."""
# def even_odd_pattern(nums: list[int]) -> list[int]:
#     ordinatip=[]
#     ordinatid=[]
#     for i in range(len(nums)):
#         if nums[i] % 2 == 0:
#             ordinatip.append(nums[i])
#         else:
#             ordinatid.append(nums[i])
#     ordinatip.extend(ordinatid)
#     return ordinatip
            
            

# print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

# """Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

# 1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
# 2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
# 3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

# Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

# Esempio:

# construct_rectangle(4)

# L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
# Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

# """
# def construct_rectangle(area: float) -> list[float]:

#     # Inizializziamo L e W con valori di default
#     L, W = 1, area
    
#     # Iteriamo per trovare la combinazione ottimale
#     for i in range(2, int(area**0.5) + 1):
#         if area % i == 0:
#             # Troviamo una coppia (i, area // i)
#             j = area // i
#             # Verifichiamo le condizioni L >= W e minimizziamo L - W
#             if i >= j and i - j < L - W:
#                 L, W = i, j
    
#     return [L, W]


# print(construct_rectangle(4))

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    risultato = []
   
    for i in range(len(x)):
        if i < len(y): 
            conta = x[i] + y[i]
            risultato.append(conta)
    return risultato

print(somma_elementi([1, 1, 1], [1, 1, 1]))  # Risultato: [2, 2, 2]
print(somma_elementi([1], [1, 2]))  # Risultato: [2]
print(somma_elementi([1, 2, -1], [0, -1, 0]))  # Risultato: [1, 1, -1]



