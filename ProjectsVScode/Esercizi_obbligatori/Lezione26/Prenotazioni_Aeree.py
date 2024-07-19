from abc import ABC,abstractmethod
import sys

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
                    return (f'I posti non sono disponibili nella classe{classe_servizio=}{self.cod_volo=}')
                
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
                return (f'classe non trovata {classe_servizio}')
        else:
            return (f"Il volo {self.cod_volo=} è al completo.")
                
                
            
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
        self.costo_volo:float = costo_volo
        
    def prenota_posto(self):
        if self.posti_disponibili() == self.cap_max:
            self.prenotazioni = self.cap_max
            return (f'{self.cod_volo=} è stato prenotato, dal costo {self.costo_volo}')
        else:
            return (f'Il volo charter {self.cod_volo} è già prenotato.')
    
    def posti_disponibili(self):
        return self.cap_max- self.prenotazioni
    
class CompagniaAerea:
    def __init__(self,compagnia:str,prezzo_standard:float) -> None:
        self.compagnia = compagnia
        self.prezzo_standard = prezzo_standard
        self.flotta = []
    
    def aggiungi_volo(self,volo_commerciale:Volo):
        self.flotta.append(volo_commerciale)
    
    def rimuovi_volo(self,volo_commerciale:Volo):
        self.flotta.remove(volo_commerciale)
        
    def mostra_flotta(self):
        for volo in self.flotta:
            return (volo.cod_volo)
        
    def guadagno(self):
        guadagno_totale:float = 0.0
        for volo in self.flotta:
            if isinstance(volo,VoloCommerciale):
                guadagno_totale += (volo.prenotazioni_economica * self.prezzo_standard + volo.prenotazioni_business * self.prezzo_standard * 2 + volo.prenotazioni_prima * self.prezzo_standard * 3)
            elif isinstance(volo,VoloCommerciale):
                guadagno_totale += volo.costo_volo
        return round(guadagno_totale, 2)
def main():
    output = []
 # Creazione di un volo commerciale
    volo_commerciale = VoloCommerciale("VC123", 100)
    output.append(f"Posti disponibili iniziali sul volo commerciale: {volo_commerciale.posti_disponibili()}")

    # Tentativo di prenotazione in classe economica
    output.append(volo_commerciale.prenota_posto(70, "economica"))
    output.append(f"Posti disponibili dopo prenotazione economica: {volo_commerciale.posti_disponibili()}")

    # Tentativo di prenotazione in classe business
    output.append(volo_commerciale.prenota_posto(20, "business"))
    output.append(f"Posti disponibili dopo prenotazione business: {volo_commerciale.posti_disponibili()}")

    # Tentativo di prenotazione in prima classe con posti maggiori della capacità disponibile
    output.append(volo_commerciale.prenota_posto(15, "prima"))
    output.append(f"Posti disponibili dopo tentativo di prenotazione prima classe con troppi posti: {volo_commerciale.posti_disponibili()}")

    # Tentativo di prenotazione in prima classe con posti esatti
    output.append(volo_commerciale.prenota_posto(10, "prima"))
    output.append(f"Posti disponibili dopo prenotazione prima classe: {volo_commerciale.posti_disponibili()}")

    # Ulteriore tentativo di prenotazione che dovrebbe fallire
    output.append(volo_commerciale.prenota_posto(1, "economica"))
    output.append(f"Posti disponibili dopo ulteriore tentativo di prenotazione: {volo_commerciale.posti_disponibili()}")

    # Creazione di un volo charter
    volo_charter = VoloCharter("VC124", 50, 5000.0)
    output.append(f"Posti disponibili iniziali sul volo charter: {volo_charter.posti_disponibili()}")

    # Tentativo di prenotazione del volo charter
    output.append(volo_charter.prenota_posto())
    output.append(f"Posti disponibili dopo prenotazione charter: {volo_charter.posti_disponibili()}")

    # Ulteriore tentativo di prenotazione del volo charter
    output.append(volo_charter.prenota_posto())
    output.append(f"Posti disponibili dopo ulteriore tentativo di prenotazione charter: {volo_charter.posti_disponibili()}")

    # Creazione di un secondo volo commerciale
    volo_commerciale2 = VoloCommerciale("VC125", 200)

    # Tentativo di prenotazione in classe economica
    output.append(volo_commerciale2.prenota_posto(140, "economica"))
    output.append(f"Posti disponibili sul secondo volo commerciale: {volo_commerciale2.posti_disponibili()}")

    # Creazione di una compagnia aerea
    compagnia = CompagniaAerea("CompagniaXYZ", 100.0)

    # Aggiungere i voli commerciali alla compagnia aerea
    compagnia.aggiungi_volo(volo_commerciale)
    compagnia.aggiungi_volo(volo_commerciale2)

    # Stampare la flotta della compagnia aerea
    output.append("Flotta della compagnia aerea:")
    output.extend(compagnia.mostra_flotta())

    # Calcolare e stampare il guadagno della compagnia aerea
    guadagno = compagnia.guadagno()
    output.append(f"Guadagno totale della compagnia aerea: {guadagno} euro")

    # Scrivere l'output su terminale e su un file
    with open("report.txt", "w") as f:
        for line in output:
            f.write(line)

if __name__ == "__main__":
    main()






        
        
        
        