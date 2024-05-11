
# * Nicola Walter Albano
# * 30/04/2024
"""
School Grading System:
1. Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.
2. Guess the Number Game:
Create a function that generates a random number within a range specified by the user.
Prompt the user to guess the number within a specified maximum number of attempts.
Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
3. E-commerce Shopping Cart:
Create a function that defines a product with a name, price, and quantity.
 Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
The function should calculate the cart total and apply any discounts or taxes.
 Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
4. Text Analysis:
 Create a function that reads a text file and counts the number of occurrences of each word.
The function should print a report showing the most frequent words and their number of occurrences.
You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
Implement error handling to handle missing files or other input issues.
5. Inventory Management System:
 Create a function that defines an item with a code, name, quantity, and price.
 Create a database or dictionary to store the items in inventory.
Implement functions to add, remove, search, and update items in the inventory.
Use for loops and conditional statements to manage the various inventory operations.
6. Password Generator:
Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
Allow the user to specify the password length and desired character types.
Generate and return a random password that meets the user's criteria.
7. Roman Numeral Conversion:
Create a function that converts a given integer to its Roman numeral representation.
Handle numbers from 1 to 3999.
Use a combination of string manipulation and conditional statements to build the Roman numeral.
8. ATM Machine Simulator:
Create a function that simulates an ATM machine.
Initialize an account with a starting balance.
Allow the user to perform transactions such as deposit, withdraw, and check balance.
 Validate transactions against the account balance and available funds.
Provide appropriate feedback to the user for each transaction.
9. Caesar Cipher Encryption/Decryption
Create functions for encrypting and decrypting a message using the Caesar cipher.
Allow the user to specify the shift value (number of positions to shift each letter).
 Handle both encryption and decryption using the same function with appropriate adjustments.
Encrypt and decrypt the given message using the specified shift value.
10. Anagram Checker:
Create a function that checks whether two given strings are anagrams of each other.
Convert both strings to lowercase and remove any non-alphabetic characters.
Sort the characters of each string and compare the sorted strings for equality.
Indicate whether the strings are anagrams or not.
11. Word Search Puzzle Solver:
Create a function that solves a word search puzzle.
Provide a 2D grid representing the puzzle and a list of words to find.
Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
Output the locations of the found words within the grid.
12. Sieve of Eratosthenes Prime Number Generator:
Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
Initialize an array of all numbers up to the limit, marking each number as prime initially.
Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
The remaining unmarked numbers are the prime numbers within the limit.
Return the list of prime numbers.
13. Fractal Tree Generator:
Create a function that generates a fractal tree using recursion.
Specify the starting trunk length and branching angle.
Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
Repeat the branching process until a desired level of detail is reached.
14. Sudoku Solver:
Create a function that solves a Sudoku puzzle using backtracking.
Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates.
Solve the puzzle by filling in the remaining empty cells with valid numbers.
15. Text Editor with Basic Functionality:
Create a simple text editor that allows the user to open, edit, and save text files.
Implement basic functionality such as inserting, deleting, and copying text.
Provide undo/redo functionality to allow users to reverse actions.
Save the edited text to a file when the user chooses to save.
"""
# * 1
studenti:list=[("Mario", [3, 4, 5]), ("Luigi", [4, 5, 6]), ("Piero", [7, 8, 9])]
def calcola_media_studenti(nome_studente: str, voto_studente: int) -> str:
    """Calcola voto del singolo studente"""
    media: float = sum(voto_studente) / len(voto_studente)
    risultato:str = "Superato" if media >= 6 else "Non superato"
    print(f"Studente: {nome_studente} \n -Media: {media}\n -Risultato: {risultato}")
def calcola_media_lista (elenco:list)->str:
    """Calcola voto di una lista di studenti"""
    for studente , voto in elenco:
        calcola_media_studenti(studente,voto)
print(calcola_media_lista(studenti))
# * 2
import random
def gioco_indovina_numero()->str:
    """GIOCA"""
    limite_inferiore = int(input("Inserisci il limite inferiore: "))
    limite_superiore = int(input("Inserisci il limite superiore: "))
    tentativi_massimi = int(input("Inserisci il numero di tentativi massimi: "))
    numero_segreto = random.randint(limite_inferiore, limite_superiore)
    tentativi = 0
    while tentativi < tentativi_massimi:
        tentativi += 1
        ipotesi_utente = int(input(f"Tentativo {tentativi}/{tentativi_massimi} - Indovina il numero: ")) 
        if ipotesi_utente == numero_segreto:
            print(f"Hai indovinato il numero! Il numero era {numero_segreto}")
            break
        elif ipotesi_utente < numero_segreto:
            print("Troppo basso!")
        else:
            print("Troppo alto!")
        if tentativi == tentativi_massimi:
            print(f"Hai perso! Il numero era {numero_segreto}")
# gioco_indovina_numero()
# * 3
