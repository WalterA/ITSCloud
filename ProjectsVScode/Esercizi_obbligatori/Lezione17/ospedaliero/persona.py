class Persona:
    def __init__(self, first_name : str, last_name : str) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = 0
        
        if not isinstance(self.__first_name, str):
            self.__first_name = None        
            print("Il nome inserito non è una stringa!")
            
        if not isinstance(self.__last_name, str):
            self.__last_name = None
            print("Il nome inserito non è una stringa!")
            
        if not isinstance(self.__last_name,str) and isinstance(self.__last_name, str):
            self.__age = None

    def setName(self,first_name : str):
        if not isinstance(first_name, str):
            self.__first_name = None    
            print("Il nome inserito non è una stringa!")
        else:
            self.__first_name = first_name
    
    def setLastName(self,last_name : str):
        if not isinstance(last_name, str):
            self.__last_name = None        
            print("Il cognome inserito non è una stringa!")
        else:
            self.__last_name = last_name
            
    def setAge(self, age : int):
        if not isinstance(age, int):
            self.__age = None        
            print("Il cognome inserito non è una stringa!")
        else:
            self.__age = age
        
    def getName(self):
        return self.__first_name
    
    def getLastname(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        print(f"Ciao, sono {self.getName()}{self.getLastname()}! Ho {self.getAge()} anni!")
        
        
#----------------------PRINT-------------------------------
ok = Persona("nooooo", "siiiiiiiiii")
ok.setAge(5)
ok.setName("fefeadea")
ok.setLastName("gege")
print(ok.getName())
print(ok.getLastname())
print(ok.getAge())
ok.greet()