from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str,id :str) -> None:
        super().__init__(first_name, last_name)
        self.__id = id
        
    def setIdCode(self,idCode):
        self.__id = idCode
        
    def getidCode(self):
        return self.__id
    
    def patientInfo(self):
        """Paziente: {nome} {cognome}
         ID: {codice identificativo}"""
         
        print(f"Paziente: {self.getName()} {self.getLastname()} \nID:{self.getidCode()}")
        
#------------------print----------------------
ok = Paziente("dede","rerere","ete3443")
ok.setIdCode("sde3e455432")
print(ok.getidCode())
ok.patientInfo()
    
        