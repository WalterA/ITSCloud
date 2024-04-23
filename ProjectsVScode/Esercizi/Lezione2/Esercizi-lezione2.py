"""
2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message. 
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.

3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.

3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.

3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 

6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
"""
# #Nicola Walter Albano
# #18/04/2024

#Variabili
estensione="okok.txt"
nome:str="Alberto"
frase:str="è bello"
nomi:list=["pippo","baudo","gianfilippo","gianfranco","pippo","baudo"]
macchine:list=["fiat","ferrari","alfa","audi"]
persone = [
    {"nome": "Mario", "cognome": "Rossi", "età": 30, "città": "Roma"},
    {"nome": "Luigi", "cognome": "Verdi", "età": 25, "città": "Milano"},
    {"nome": "Anna", "cognome": "Bianchi", "età": 35, "città": "Napoli"}
]
animali = [
    {"razza": "pitbull", "taglia": "medio", "età": 10, "proprietario": "Massimo"},
    {"razza": "pit", "taglia": "piccolo", "età": 16, "proprietario": "Anna"},
    {"razza": "pitbl", "taglia": "grande", "età": 12, "proprietario": "Gigi"}
]
definizioni="Nome proprio di persona"
numeri_favoriti = {
    'maria': [42, 17],
    'michele': [42, 39, 56],
    'gustavo': [7, 12],
    }

#Funzioni
#2.4
def maiuscola (l:str) -> str:
        """Fornisce una stringa con tutti i caratteri maiuscoli."""
        x=l.upper()
        return x

def prima_lettera (l:str) -> str:
        """Converte solo la prima lettera della stringa in maiuscolo. """
        x=l.capitalize()
        return x
#2.8
def elimina_estensione (l:str)->str:
    """Rimuove l'estensione"""
    rimosso=l.removesuffix(".txt")
    return rimosso
#3.6-3.7-3.8
def aggiungi (l:list)->list:
        """Aggiunge nuove stringe nella lista"""
        l.append(input("Inserisci testo da aggiungere:"))
        return l

def elimina (index:int, l:list)->str:
    """elimina un elemento dalla lista e ritorna l'elemento cancellato"""
    eliminati=l.pop(index)
    return eliminati

def inserisci (index:int, l:list) ->str:
    """inserisce in un determinato indice una nuova stringa"""
    l.insert(index,input("Inserisci testo da aggiungere:"))
    return l

def ordina (l:list) -> list:
    """mosta la lista dissordinata e ritorna ordinata"""
    print(l)
    lista=sorted(l)
    return lista
#print(f"lista ordinata con sorted{ordina(nomi)}")
def ordinas (l:list) -> list:
    """mosta la lista dissordinata e ritorna ordinata"""
    print(l)
    l.sort()
    return l
#print(f"lista ordinata con sort{ordinas(nomi)}")
def reverse (l:list) ->list:
    """inverte la lista"""
    print(l)
    l.reverse()
    return (l)

def numero_di_persone(l:list)->int:
        """ritorna il numero degli elementi della lista"""
        elementi=len(l)
        return elementi
#print(numero_di_persone(nomi))
#3-10
def nuova_lista ()->list:
    """crea una nuova lista"""
    lista=[]
    lista=input("inserisci nomi della lista, lasciando uno spazio: ")
    lista=lista.split(" ")
    lista_numeri=[]
    for item in lista:

        if type(item) == str:
            try:
                lista_numeri.append(float(item))
            except Exception:
                lista_numeri.append(item)
    return lista_numeri


#6-1
def elenco_diz(lista_dict: list) -> dict:
    """legge i valori delle chiavi"""
    result = {}
    key:str=input("inserisci key")
    for dizionario in lista_dict:
            print(dizionario[key])
#elenco_diz(persone)
#6-2
def nuova_chiave(l:list)->dict:
    """inserisce nuove chiavi"""
    for i in l:
        lista={}
        l.append(lista)
        for k,v in lista:
            k[lista]= [input("Inserisci nome chiave")]
            v[lista]= [input("inserisci numero")]
    return lista
print(nuova_chiave(persone))
#6-3
def definizione(l:list)->list: #chiedere di inserire un range
    for k in l:
        print(k["nome"],':'"\n" ,definizioni)
#6.7
# def lista_di_nomi (l:list) -> list:
#     lista:list=[]
#     for k in l:
#         lista.append(k["nome"])
#     return lista

# def lista_di_cognomi (l:list) -> list:
#     lista:list=[]
#     for k in l:
#         lista.append(k["cognome"])
#     return lista

# #variabili per lista_persona
# n:list=lista_di_nomi(persone)
# c:list=lista_di_cognomi(persone)

def lista_persone (n:list,c:list) -> list:
    lista_uni:list = []
    if len(n) == len(c):
        for i in range(len(n)):
            lista_uni.append(n[i] + " " + c[i])
        return lista_uni
    else:
        print("Le liste devono avere la stessa lunghezza per unirle.")

#6-8
razza:list=[]
proprietario:list=[]
# #for k in animali:
#     razza.append(k["razza"])
#     proprietario.append(k["proprietario"])
# for i in range(len(razza)):
#     print(f"Il proprietario {proprietario[i]} ha scelto la razza {razza[i]}")

#6.10
# for nome, numeri in numeri_favoriti.items():
#     print("\n" + nome.title() + "I numeri fortunati sono:")
#     for num in numeri:
#         print("  " + str(num))

#2.5
#print(f"{maiuscola(nome)}, {prima_lettera(frase)}\"ma chissà\"")

#Stampa
#print(f"File senza esternzione:",elimina_estensione(estensione)) #->str
#print(aggiungi(nomi))
#print(elimina(nomi))
#print(inserisci(nomi))
#print(maiuscola(estensione))
#print(prima_lettera(estensione))
#print(ordina(nomi))
#print(reverse(nomi))
#print(ordinas(nomi))
#print(numero_di_persone(nomi))
#print(nuova_lista())
#print(nuova_lista())
#print(elenco_diz(persone))
#nuova_chiave(persone)
#print(definizione(persone))
#print(lista_persone(n,c))