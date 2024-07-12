from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod   
    def codifica(self, testoInChiaro:str):
        pass
    
class DecodificatoreMessaggio(ABC):
    def __init__(self,testoCodificato:str) -> None:
        self.testoCodificato = testoCodificato
        
    @abstractmethod   
    def decodifica(testoCodificato:str)->str:
        pass
    
class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self, chiave:int) -> None:
        self.chiave = chiave
         
    def codifica(self, testoInChiaro:str):
        lista:list =["A , B , C , D , E , F , G , H , I , J , K , L , M , N , O , P , Q , R , S , T , U , V , W , X , Y , Z"]
        ["defabc"]
        for i in testoInChiaro:
            if i in lista:
                carattere = lista[i]
            testoInChiaro[i] = carattere
    
              

            
            
        