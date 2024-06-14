from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization : str, parcel: float ) -> None:
        super().__init__(first_name, last_name)
        
        self.__specialization = specialization
        self.__parcel = parcel
        
        if not isinstance(self.__specialization, str):
            self.__specialization = None        
            print("La specializzazione inserito non è una stringa!")
        
        if not isinstance(self.__parcel, float):
            self.__specialization = None        
            print("La parcella inserita non è un float!")
            
    def setSpecialization(self, specialization):
        if not isinstance(specialization, str):
            self.__specialization = None    
            print("La specializzazione inserita non è una stringa!")
        else:
            self.__specialization = specialization
        
    def setParcel(self, parcel):
        if not isinstance(parcel, float):
            self.__parcel = None    
            print("La specializzazione inserita non è una stringa!")
        else:
            self.__parcel = parcel
            
    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} e {self.getLastname()} is valid!")
            return True
        else:
            print(f"Doctor {self.getName()} e {self.getLastname()} is not valid!")
            return False
    def doctorGreet(self):
        self.greet()
        print (f"Sono un medico {self.getSpecialization()}")
    
#----------------------PRINT-------------------------------
ok = Dottore("gigi","sef","joe",14.0)
ok.setAge(31)
ok.setParcel(12.5)
ok.setSpecialization("gesfsfsage")
print(ok.getParcel())
print(ok.getSpecialization())
ok.isAValidDoctor()
ok.setSpecialization("dottore")
ok.doctorGreet()