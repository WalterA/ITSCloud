import unittest
class Documento:
    def __init__(self,testo:str) -> None:
        self.testo = testo
    
    def getText(self):
        return self.testo
    
    def setText(self,testo:str):
        self.testo = testo
        
    def islnText (self,parola:str):
        if parola in self.testo:
            return True
        else: 
            return False
        
class Email(Documento):
    def __init__(self, testo: str,mittente:str,destinatario:str,titolo:str) -> None:
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo = titolo
        
    def setmittente(self, mittente):
        self.mittente = mittente
        
    def setdestinatario (self, destinatario):
        self.destinatario = destinatario
        
    def settitolo (self,titolo):
        self.titolo = titolo
    
        
    def getmittente (self):
        return self.mittente
    
    def getdestinatario(self):
        return self.destinatario
    
    def gettitolo(self):
        return self.titolo
    
       
    def getText(self)->str:
        return f'Da:{self.getmittente()},A:{self.getdestinatario()}\nTiTolo:{self.gettitolo()}\nMessaggio:{self.testo}'

    def writeToFile(self,nomefile:str):
        with open(nomefile,'w') as reader:
            reader.write(self.getText())

class File(Documento):
    def __init__(self, percorso:str) -> None:
        self.percorso = percorso
        super().__init__(testo=self.leggiTestoDaFile())
        
    def leggiTestoDaFile(self):
        with open(self.percorso,'r') as reader:
            return reader.read()
        
    def getText(self):
        return (f'Percorso:{self.percorso},Contenuto:{self.testo}')
    


class testdocumento(unittest.TestCase):
    def Text(self):
        var=Documento("testo")
        var.getText("testo2")
        self.assertEqual(var.getText(),"testo2")

if __name__ == '__main__':
    unittest.main()


# email = Email("Ciao Bob, possiamo incontrarci domani?", "alice@example.com", "bob@example.com","Incontro")
# file=File("ProjectsVScode/Esercizi_obbligatori/Lezione24/documento.txt")
# print(email.getText())
# print(file.getText())
# email.writeToFile("ProjectsVScode/Esercizi_obbligatori/Lezione24/enuovo.txt")
# print(email.islnText("incontrarci"))
# print(file.islnText("percorso"))






