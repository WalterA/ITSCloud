class Pagamento:
    def __init__(self) -> None:
        self.__impoto_pagamento : float = None
    
    def importset(self,importo):
        self.__impoto_pagamento = importo
    
    def get(self):
        return self.__impoto_pagamento
        
    def dettagliPagamento(self):
        """che visualizza una frase che descrive l'importo del pagamento,
        ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, 
        l'importo è sempre con 2 cifre decimali.
        """
        imp=round(self.get(),2)
        return f"Importo del pagamento: {imp}"
         
class PagamentoContanti(Pagamento):
    """Successivamente, si definisca una
    classe PagamentoContanti che sia derivata da Pagamento e
    definisca l'importo. Questa classe dovrebbe ridefinire il metodo 
    dettagliPagamento() per indicare che il pagamento è in contanti. 
    Si definisca inoltre il metodo inPezziDa() che stampa a schermo 
    quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 
    10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro,
    0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie per pagare l'importo in contanti."""
    def __init__(self, importo:float) -> None:
        super().__init__()
        self.importset(importo)
    
    def dettagliPagamento(self):
        imp=round(self.get(),2)
        return f"Importo del pagamento è in contanti: {imp}"
    
    def inPezziDa(self):
        map: list[float]= [500, 200 , 100 , 50, 20, 10, 5,2, 1, 0.50,0.20, 0.10, 0.05, 0.01]
        pezzi = 0
        importo:float = self.get()
        for i in map:
            pezzi = int(importo // i)
            importo = round(importo - pezzi*i, 2)
            
            if pezzi != 0 and i >= 5:
                print(f'{pezzi} di banconote da {i}')
            elif pezzi != 0 and i < 5:
                print(f'{pezzi} di monete da {i}')
                
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome:str,cognome:str,scadenza:str,cartadicredito:int,importo:float) -> None:
        super().__init__()
        self.importo:float = importo
        """Questa classe deve contenere gli attributi per il nome del titolare della carta,
        la data di scadenza, e il numero della carta di credito. Infine, si ridefinisca il metodo 
        dettagliPagamento() per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

        Per il test, si creino almeno due oggetti di tipo PagamentoContanti 
        e due di tipo PagamentoCartaDiCredito con valori differenti e si invochi 
        dettagliPagamento() per ognuno di essi."""
        
        self.nome:str = nome
        self.cognome:str = cognome
        self.scadenza:str = scadenza
        self.cartadicredito:int = cartadicredito
    def dettagliPagamento(self):
        return f"Pagamento di: {self.importo} effettuato con la carta di credito\nNome sulla carta:{self.nome} {self.cognome}\nData di scadenza: {self.scadenza}\nNumero della carta: {self.cartadicredito}"
        
        
        

        
#------------------print----------------------

contanti=PagamentoCartaDiCredito("TIZIO","bobo","23/25",432524646426245432132,23.11)
print(contanti.dettagliPagamento())