from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self,doctor : Dottore, patient: list[Paziente]):
        self.patient:list = patient
        self.doctor = doctor
        
        if doctor.isAValidDoctor():
            self.fatture = int
            self.salary = 0
        else:
            self.fatture = None
            self.salary = None
            self.patient = None
            self.doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            
    def getSalary(self):
        """deve ritornare il salario guadagnato dal dottore. 
        Il salario gudaganto viene calcolato moltiplicando la parcella 
        del dottore per il numero di pazienti."""
        num = len(self.patient)
        guadagno = self.doctor.getParcel() * num
        return guadagno
    
    def getFatture(self):
        """deve assegnare all'attributo fatture il numero di pazienti
        (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore."""
        num = len(self.patient)
        self.fatture = num
        return self.fatture
    
    def addPatient(self,newPatient: Paziente):
        """consente di aggiungere un paziente alla lista 
        di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, 
        richiamando il metodo getFatture() e getSalary().  Stampare "Alla lista del Dottor 
        cognome è stato aggiunto il paziente {codice_identificativo}"""
        self.patient.append(newPatient)
        self.getSalary()
        self.getFatture()
        return f"Alla lista del Dottor {self.doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}"
        




ok: Dottore = Dottore("gigi","sef","joe",14.0)
ok.setAge(31)
ok.setParcel(12.5)
ok.setSpecialization("gesfsfsage")
p1 = Paziente("dede","rerere","ete3443")
p1.setIdCode("sde3e455432")
p2 = Paziente("dede","rerere","ete3443")
p2.setIdCode("sde3e455432")
p3 = Paziente("dede","rerere","ete3443")
p3.setIdCode("sde3e455432")
lista =[]
fa=Fattura(ok,lista)
print(fa.addPatient(p1))
