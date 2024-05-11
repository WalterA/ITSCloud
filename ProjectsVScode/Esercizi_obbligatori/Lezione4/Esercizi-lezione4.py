
# * Nicola Walter Albano
# * 26/04/2024

"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call.

8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.

8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.

8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. 

8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
"""
# * 8.1 \ 8.8
def album (artist:str, title:str, tracce:int=None)-> dict:
    "Crea nuovi dizionari"
    album={"Artista":artist, "Titolo":title}
    if tracce:
        album["Tracce"]=tracce
    return album
album1:dict=album("Nirvana", "Nevermind", 10)
album2:dict=album("Michael Jackson", "Thriller", 12)
album3:dict=album("Pink Floyd", "The Wall", 17)

def descrivi_album() -> dict:
    """Crea nuovi dizionari"""
    album_info={}
    while True:
        artista=input("Artista: \nquit per uscire \n")
        if artista == "quit":
            break
        titolo = input("Titolo: \nquit per uscire \n")
        if titolo == "quit":
            break
        tracce = input("Tracce: \nquit per uscire \n")
        if tracce == "quit":
            break
        elif tracce:
            tracce=int(tracce)
        else:
            tracce=None
        album_info:dict = {"artista": artista, "titolo": titolo, "tracce": tracce}
        print(f"Album creato: {album_info}")
    return album_info
# * 8.9 \ 8.11
sms=["ciao","come","stai"]
inviati_messaggi=[]
def Messaggi (sms:list, inviati_messaggi:list)->str:
    """Stampa e invia messaggi"""
    for mess in sms:
        print(mess)
    while sms:
        inviati=sms.pop(0)
        print(f"Invio messaggio: {inviati}")
        inviati_messaggi.append(inviati)
# * 8.12
def ordina_panino():
    """Stampa un riepilogo ingredienti"""
    ingredienti:list=[]
    ingredienti=input("inserisci ingredienti, lasciando uno spazio: ")
    ingredienti=ingredienti.split(" ")
    print("\n Hai ordinato un panino con i seguenti ingredienti: ")
    for ingrediente in ingredienti:
        print(f"- {ingrediente}")
# * 8.13
def build_profile(first:str, last:str, **user_info:dict)->dict:
    """Costuisce un profilo utente in un dizionario"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return f"{profile['first_name']} {profile['last_name']}, " + ", ".join([f"{k}: {v}" for k, v in user_info.items()])
# * 8.14
def make_car (produttore:str, modello:str, **car_info:dict)->dict:
    """Costuisce un dizionario contenente informazioni sul veicolo"""
    auto:dict={produttore:produttore, modello:modello}
    for key, value in car_info.items():
        auto[key] = value
    return auto
car=make_car("subaru", "outback", color="blue", tow_package=True)
# * 8.15
from printing_models import funzione1, funzione2
funzione1("che figooo a saperlo prima non avrei riscritto la metà delle funzioni qui sopra e non solo")
# * 8.16
from Esercizi_lezione3 import *
scansione_lista(5, 0, 10)
# * 8.17
"fatto"













