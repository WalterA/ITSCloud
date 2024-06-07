class Media:
    def __init__(self,rewiews) -> None:
        self.rewiews:list[int] = []

    def set_title(self, title:str):
        """Imposta il titolo del media."""
        self.title:str = title
        
    def get_title(self):
        """Restituisce il titolo del media."""
        return print(f"Titolo del Film:  {self.title}")
    
    def aggiungiValutazione(self, voto):
        """Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5)."""
        
        if voto <= 5 and voto >= 1:
            rewiews.append(voto)
            
    def getMedia(self):
        """Calcola e restituisce la media delle valutazioni."""
        for i in self.rewiews:
            for valore in self.voto:
                
            
            
media = Media()       
media.set_title("pippo")
media.get_title()