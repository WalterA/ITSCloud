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


#3-4. Guest List: If you could invite anyone, 
#living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person,
# inviting them to dinner.
#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
# #list invit
invit: str=["pippo","bob","vieri","gianpippo2"]
for i in invit:
    print("Invite", i)

eliminate=invit.pop(1)
print(eliminate)
print(invit)
invit.insert(0, "gianfranco")
invit.insert(3, "milimassimo")
invit.append("gianfrippone")
print(invit)
del invit[0]
print(invit)