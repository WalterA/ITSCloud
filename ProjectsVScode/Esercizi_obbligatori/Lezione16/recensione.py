class Media:
    def __init__(self) -> None:
        self.rewiews:list[int] = []
        self.title = ""

    def set_title(self, title:str):
        """Imposta il titolo del media."""
        self.title = title
        
    def get_title(self):
        """Restituisce il titolo del media."""
        return f"{self.title}"
    
    def aggiungiValutazione(self, voto):
        """Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5)."""
        
        if voto <= 5 and voto >= 1:
            self.rewiews.append(voto)
            
    def getMedia(self):
        """Calcola e restituisce la media delle valutazioni."""
        tot = sum(self.rewiews)
        return tot / len(self.rewiews)
    
    def getRate(self): 
        """Restituisce una stringa che descrive il giudizio medio basato sulla media delle valutazioni, 
        ovvero mostra "Terribile" se il voto medio si avvicina a 1, "Brutto" se il voto medio si avvicina a 2, 
        "Normale" se il voto medio si avvicina a 3, "Bello" se il voto medio si avvicina a 4, 
        "Grandioso" se il voto medio si avvicina a 5."""
        media= self.getMedia()
        if media <= 1:
            return "Terribile"
        elif media <=2 and media >= 1:
            return "Brutto"
        elif media <= 3 and media >= 2:
            return "Normale"
        elif media <=4 and media >=3:
            return "Bello"
        else:
            media == 5 and media >=4
            return "Grandioso"
    def ratePercentage(self, voto): 
        """Calcola e restituisce la percentuale di un voto specifico nelle recensioni."""
        conta = 0
        for i in self.rewiews:
            if voto == i:
                conta += 1
        return round((conta / len(self.rewiews)) * 100)
    
    def recensione(self): 
        """Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, 
        il voto medio, il giudizio e le percentuali di ciascun voto."""
        """Titolo del Film: The Shawshank Redemption
        Voto Medio: 3.80
        Giudizio: Bello
        Terribile: 10.00%
        Brutto: 10.00%
        Normale: 10.00%
        Bello: 30.00%
        Grandioso: 40.00%"""
        
        return print(f"Titolo del Film:{self.title}\nVoto Medio:{self.getMedia()}\nGiudizio:{self.getRate()}\nTerribile:{self.ratePercentage(1):.2f}%\nBrutto:{self.ratePercentage(2):.2f}%\nNormale:{self.ratePercentage(3):.2f}%\nBello:{self.ratePercentage(4):.2f}%\nGrandioso:{self.ratePercentage(5):.2f}%")
                
class Film(Media):
    def __init__(self,title:str) -> None:
        super().__init__()
        self.set_title(title)
        
titolo = Film("The Shawshank Redemption")
titolo.aggiungiValutazione(5)
titolo.aggiungiValutazione(2)
titolo.aggiungiValutazione(3)
titolo.aggiungiValutazione(4)
titolo.aggiungiValutazione(4)
titolo.aggiungiValutazione(4)
titolo.aggiungiValutazione(5)
titolo.aggiungiValutazione(5)
titolo.aggiungiValutazione(5)
titolo.aggiungiValutazione(5)

titolo.getMedia()
titolo.getRate()
titolo.ratePercentage(4)
titolo.recensione()


    
    