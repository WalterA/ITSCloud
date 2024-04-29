
#* Nicola Walter Albano
#* 23/04/2024

"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.


4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/. You won’t use much of it now, but it might be interesting to skim through it.

4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.

5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list

5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.

5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.


5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.

5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!

5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.

5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)


5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""

# * 4.1
#variabili
pizza:list[str]=["marg","diav","capri"]
frasi_list:list[str]=["mi piace"]
def frasi(p:list, f:list)->str:
    """unisce due liste di lunghezze diverse"""
    for o in p:
        for i in f:
            lista=i + " " + o
            print(lista)
# * 4.2 vedi 4.1
# * 4.3
def genera_numeri (index:int)->list:
    """Genera dei numeri"""
    my_list:list =[index for index in range(index)]
    return my_list
def scansione_lista(index:int,inizio:int,fine:int)->str:
    """stampa un range di numeri"""
    genera_numeri(index)
    for i in range(inizio,fine):
        print(i)
# * 4.4
def genera_milione ()->int:
    """Genera da 1 a un milione"""
    for index in range(1, 100001):
        print(index)
# * 4.5
def min_max_sum ()->list[int]:
    """Crea una lista di un milione di numeri e trova il num, max e la somma"""
    lista_numeri:list = list(range(1,100001))
    minimo:int=min(lista_numeri) #-> list
    massimo:int=max(lista_numeri) #-> lista
    somma:int=sum(lista_numeri) #-> list
    print(f"La lista dei numeri è:{lista_numeri} \nIl numero più piccolo è:{minimo}\nIl numero più grande è:{massimo}\nLa somma è:{somma}") #-> print int
# * 4.6
def dispari ()->int:
    """Stampa i numeri dispari da 1 a 20"""
    lista_numeri:list = list(range(1,20))
    for i in lista_numeri:
        if i %2 !=0:
            print(i)
# * 4.7
def multipli3 ()->int:
    """Stampa i numeri multipli di 3 da 3 a 30"""
    lista_numeri:list = list(range(3,30))
    for i in lista_numeri:
        if i %3 ==0:
            print(i)
# * 4.8
def cubi ()->int:
    """Stampa i numeri cubi da 1 a 11"""
    cubi:list=[numero**3 for numero in range(1,11)]
    for cubo in cubi:
        print(cubo)
# * 4.9
# my_list:list =[index for index in range(100)]
# my_list1:list =[index for index in range(100) if index %2 ==0]
# my_list2:list =[index if index %2 == 0 else -1 for index in range(100)]
# my_list3:list =[parola.lower() for parola in my_list]
# my_dict:dict={"key_1":0, "key_2":1}
# my_dict2:dict={v:k for k,v in my_dict.items()}
# * 4.10
elenco_numeri:list=genera_numeri(10)
def primi3 (lista:list)->int:
    """Stampa i primi 3 elementi di una lista"""
    for i in range(3):
        print(lista[i])
def centro_elenco (lista:list)->int:
    """Stampa centro elenco"""
    centro=len(lista)//2
    for i in lista[centro-1:centro+2]:
        print(i)
def ultimi3 (lista:list)->int:
    """Stampa le ultime tre elementi di una lista"""
    for i in lista[-3:]:
        print(i)
# * 4.11
def aggiungi_elemento (lista:list,index:str)->list:
    """Aggiunge un elemento alla fine di una lista"""
    lista.append(index)
    return lista
def nuova_lista ()->list:
    """crea una nuova lista"""
    lista:list=[]
    lista=input("inserisci nomi della lista, lasciando uno spazio: ")
    lista=lista.split(" ")
    lista_mista:list=[]
    for item in lista:
        if type(item) == str:
            try:
                lista_mista.append(float(item))
            except Exception:
                lista_mista.append(item)
    return lista_mista
# ! print(f"La lista aggiornata: {aggiungi_elemento(pizza,"funghi")},la nuova lista: {nuova_lista()}")
# * 4.12
# ma basta!!!!!!!!!!!!!!!
# * 5.1
car="subaru"
result=car=="subaru"
result1=car=="audi"
result2=car=="bmw"
result3=car=="toyota"
result4=car=="nissan"
result5=car=="honda"
result6=car=="s"
# !print(result)
# !print(result1)
# !print(result2)
# !print(result3)
# !print(result4)
# !print(result5)
# !print(result6)
# * 5.2
def pari_dispari ()->bool:
    """testa se un numero è pari o dispari"""
    num:float=float(input("inserisci un numero: "))
    if num %2 ==0:
        return True
    else:
        return False
def test_palindromo ()->bool:
    """testa se una stringa è un palindromo"""
    stringa:str=input("inserisci una stringa: ")
    stringa:str=stringa.lower()
    stringa:str=stringa.replace(" ", "")
    if stringa == stringa[::-1]:
        return True
    else:
        return False
def stringa_uguale ()->bool:
    """restituisce se lunghi uguali"""
    stringa1:str=input("inserisci prima stringa: ")
    stringa2:str=input("inserisci seconda stringa: ")
    if len(stringa1) == len(stringa2):
        return True
    else:
        return False
# * 5.3 - 5.4 - 5.5 completo rispetto alla traccia dell'esercizio
def gioco_alieno ()->str:
    """Gioco alieno"""
    punti:int=0
    while punti < 30:
        alien_color:str=input("Inserisci un colore alieno: ")
        if alien_color == "verde":
            punti+=5
            print("Hai guadagnato 5 punti")
        elif alien_color == "giallo":
            punti+=10
            print("Hai guadagnato 10 punti")
        elif alien_color == "rosso":
            punti+=15
            print("Hai guadagnato 15 punti")
        else:
            punti -= 5
            print("hai perso 5 punti")
        if punti >= 30:
            print("Hai vinto")
    return "Hai perso"
# * 5.6
def eta (eta:int)->str:
    """restituisce l'età di un utente"""
    if eta <= 2:
        print ("sei un bambino")
    elif eta <= 4:
        print ("sei un bambino piccolo")
    elif eta <= 13:
        print ("sei un bambino")
    elif eta <= 20:
        print ("sei un adolescente")
    elif eta <= 65:
        print ("sei un adulto")
    else:
        print ("sei un anziano")
# * 5.7
def preferiti (stringa:str,list:list[str])->str:
    """stampa i preferiti"""
    if stringa in frutti:
        return("ti piacciono le mele")
    if stringa in frutti:
        return("ti piacciono le pere")
    if stringa in frutti:
        return("Ti piacciono le banane")
    else:
        print("Elemento non trovato nella lista")
frutti=["mele", "pere", "banane"]
# * 5.8 - 5.9
nomi:list[str]=["admin","user1","user2","user3"]
nomi1:list[str]=[]
def saluta_utenti (lista:list[str])->str:
    """saluta gli utenti"""
    for utenti in lista:
        if utenti == "admin":
            print(f"Hello Adimin, would you like to see a status report?")
        else:
            print(f"Hello {utenti}, thank you for logging in again.")
    else:
        print("Non ci sono utenti")
# * 5.10
def controlla_utente (lista:list[str])->str:
    """controlla se l'utente è registrato"""
    lista_min = [item.lower() for item in lista]
    utente = input("inserisci nome utente: ")
    utente_min = utente.lower()
    if utente_min in lista_min:
        return("utente registrato")
    else:
        return("utente non registrato")
# * 5.11
def non_so (lista:list[int])->str:
    """stampa le posizioni dei numeri diversi da zero"""
    for numeri in lista:
        if numeri == 0:
            pass
        elif numeri == 1:
            print(f"{numeri}°")
        elif numeri == 2:
            print(f"{numeri}°")
        elif numeri == 3:
            print(f"{numeri}°")
        elif numeri == 4:
            print(f"{numeri}°")
        elif numeri == 5:
            print(f"{numeri}°")
        else:
            print(f"{numeri}°")
num=list(range(1,10))
#non_so(num)






