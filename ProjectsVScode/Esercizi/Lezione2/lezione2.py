# #Nicola Walter Albano
# #18/04/2024
# print("Hello word")



# #3-1. Names: Store the names of a few of your friends in a list called names.
# #Print each person’s name by accessing each element in the list, one at a time.
# alphabet:list=["a","b","c","d","e"]
# firt_letter= alphabet[0]
# print(firt_letter)
# last_letter=alphabet[-1]
# print(last_letter)
# firt_three=alphabet[0:3]
# print(firt_three)
# last_three=alphabet[-3:]
# print(last_three)
# alphabet.append("f")
# alphabet.append("m")
# alphabet.append("g")
# print(alphabet)
# last_three=alphabet[-3:]
# print(last_three)
# eliminet=alphabet.pop(-1)
# print(alphabet)
# print(eliminet)

# #2-3. Personal Messege: Use a variable to represent a person's name.
# #and print a message to that person.
# #Your message should be simple, such as,
# #"Hello Eric, would you like to learn some Python today?"
# #3-2. Greetings: Start with the list you used in Exercise 3-1, 
# #but instead of just printing each person’s name, print a message to them. 
# #The text of each message should be the same, 
# #but each message should be personalized with the person’s name.
# nome:str="Eric"
# print(f"Hello {nome}, would you like to learn some Python today?")
# #2-4. Name Cases: Use a variable to represent a person’s name, 
# #and then print that person’s name in lowercase, uppercase, and title case.
# tipo:str="Fracy"
# x=tipo.upper()
# print(x)
# x=tipo.capitalize()
# print(x)
# famous_person="Albert Einstein"
# citazione="Una persona che non ha mai commesso un errore non ha mai provato nulla di nuovo"
# print(f"{famous_person},\"{citazione}\"")

# filename="python_notes.txt"
# file=filename.removesuffix(".txt")
# print(file)

#3-3. Your Own List: Think of your favorite mode of transportation, 
#such as a motorcycle or a car, and make a list that stores several examples.
#Use your list to print a series of statements about these items, 
#such as “I would like to own a Honda motorcycle.”

#list transportation
transportation: str =["Car","Buss"]
motorcycle: str = ["Ferrari","Fiat"]
speak: str = ["buy","cool"]
print(f"{speak[1]} {transportation[0]}, {motorcycle[1]}")


#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.