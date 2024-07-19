from abc import ABC,abstractmethod

class Volo(ABC):
    def __init__(self,cod_volo:str,cap_max:int) -> None:
        self.cod_volo = cod_volo
        self.cap_max = cap_max
        self.prenotazioni = 0
        
    @abstractmethod
    def prenota_posto(self):
        pass
    @abstractmethod
    def posti_disponibili():
        pass
    
class VoloCommerciale(Volo):
    def __init__(self, cod_volo: str, cap_max: int) -> None:
        super().__init__(cod_volo, cap_max)
      
        self.posti_economici = ((cap_max*70)/100)
        self.posti_business = (((cap_max-self.posti_economici)*20)/100)
        self.posti_prima = (cap_max-self.posti_economici-self.posti_business)
        self.prenotazioni_economica:int = 0
        self.prenotazioni_business:int = 0
        self.prenotazioni_prima:int = 0
        
    def prenota_posto(self,posti:int,classe_servizio:str):
        if self.posti_disponibili()['posti disponibili'] > posti:
            if classe_servizio == "economica":
                if self.posti_disponibili()['classe economica'] > posti:
                    self.prenotazioni_economica += posti
                    self.prenotazioni += posti
                    return (f'posti riservati: {posti=},nella classe: {classe_servizio=}, abbinato al codice: {self.cod_volo=}')
                else:
                    return (f'I posti non sono disponibili nella classe{classe_servizio=}')
                
            elif classe_servizio == 'business':
                if self.posti_disponibili()['classe business'] > posti:
                    self.prenotazioni_business += posti
                    self.prenotazioni += posti
                    return (f'posti riservati: {posti=},nella classe: {classe_servizio=}, abbinato al codice: {self.cod_volo=}')
                else:
                    return (f'I posti non sono disponibili nella classe{classe_servizio=}')
                
            elif classe_servizio == 'prima classe':
                if self.posti_disponibili()['prima classe'] > posti:
                    self.prenotazioni_prima += posti
                    self.prenotazioni += posti
                    return (f'posti riservati: {posti=},nella classe: {classe_servizio=}, abbinato al codice: {self.cod_volo=}')
                else:
                    return (f'I posti non sono disponibili nella classe{classe_servizio=}')
            else:
                raise ValueError(f'classe non trovata {classe_servizio}')
        else:
            return ('Volo completo!!')
                
                
            
    def posti_disponibili(self):
        self.diz:dict={}
        
        if self.cap_max-self.prenotazioni > 0:
            self.diz['posti disponibili'] = self.cap_max-self.prenotazioni
        else:
            self.diz['posti disponibili'] = 0
            
        if self.posti_economici-self.prenotazioni_economica > 0:
            self.diz['classe economica'] = self.posti_economici-self.prenotazioni_economica
        else:
            self.diz['classe economica'] = 0
        
        if self.posti_business - self.prenotazioni_business > 0:
            self.diz['classe business'] = self.posti_business - self.prenotazioni_business
        else:
            self.diz['classe business'] = 0
            
        if self.posti_prima-self.prenotazioni_prima > 0:
            self.diz['prima classe'] = self.posti_prima-self.prenotazioni_prima
        else:
            self.diz['prima classe'] = 0
        return self.diz

class VoloCharter(Volo):
    def __init__(self, cod_volo: str, cap_max: int,costo_volo:float) -> None:
        super().__init__(cod_volo, cap_max)
        self.cap_max = cap_max
        self.cod_volo = cod_volo
        self.costo_volo:float = costo_volo
    def prenota_posto(self):
        if self.posti_disponibili() == self.cap_max:
            self.prenotazioni = self.cap_max
            return (f'{self.cod_volo=} è stato prenotato, dal costo {self.cod_volo}')
        else:
            return ('il volo è stato prenotato')
    
    def posti_disponibili(self):
        return self.cap_max- self.prenotazioni
    
class CompagniaArea:
    def __init__(self,compagnia:str,prezzo_standard:float,flotta:list) -> None:
        self.compagnia = compagnia
        self.prezzo_standard = prezzo_standard
        self.flotta = flotta
    
    def aggiungi_volo(self,volo_commerciale:VoloCommerciale):
        self.flotta.append(volo_commerciale)
    
    def rimuovi_volo(self,volo_commerciale):
        self.flotta.remove(volo_commerciale)
    def mostra_flotta(self):
        return self.flotta
    def guadagno(self):
                
        
        
        
        