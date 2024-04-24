alphabet:list=["a","b","c","d","e"]
firt_letter= alphabet[0]
print(firt_letter)
last_letter=alphabet[-1]
print(last_letter)
firt_three=alphabet[0:3]
print(firt_three)
last_three=alphabet[-3:]
print(last_three)
alphabet.append("f")
alphabet.append("m")
alphabet.append("g")
print(alphabet)
last_three=alphabet[-3:]
print(last_three)
eliminet=alphabet.pop(-1)
print(alphabet)
print(eliminet)


menu={"pasta":10.50,"pizza":9.00,"salad":6.50,"wine":4.00,"water":2.30}
print(menu)
pasta:float=menu["pasta"]
wine:float=menu["wine"]
print(pasta)
print(wine)
menu["pizza"]=10.50
print(menu)



nome:str="Eric"
print(f"Hello {nome}, would you like to learn some Python today?")
tipo:str="Fracy"
x=tipo.upper()
print(x)
x=tipo.capitalize()
print(x)
famous_person="Albert Einstein"
citazione="Una persona che non ha mai commesso un errore non ha mai provato nulla di nuovo"
print(f"{famous_person},\"{citazione}\"")

filename="python_notes.txt"
file=filename.removesuffix(".txt")
print(file)

