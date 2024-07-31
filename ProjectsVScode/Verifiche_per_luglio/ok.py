class ContactManager:
    def __init__(self) -> None:
        #Dizionario che ha per chiave il nome del contatto
        # e per valore una lista di numeri di telefono.
        # I numeri di telefono sono espressi sottoforma di stringa
        self.contacts:dict[str,list[str]] = {}
    
    def create_contact(self, name: str, phone_numbers: list[str])->dict[str,list[str]]:
        """Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato
            e una lista di numeri di telefono. Restituisce un nuovo dizionario 
            con il solo contatto appa   ena creato o il messaggio di errore "Errore: il contatto esiste
            già." se il contatto esiste già.
        """
        
        if name in self.contacts:
            return "Errore: il contatto esiste già. e il contatto esiste già."
        else:
            self.contacts[name] = phone_numbers
        
        return {name: self.contacts[name]}
    
    def add_phone_number(self, contact_name: str, phone_number: str)->dict[str,list[str]]:
        """Aggiunge un numero di telefono al contatto specificato. 
            Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di
            errore "Errore: il contatto non esiste." se il contatto non esiste
            oppure "Errore: il numero di telefono esiste già." se il numero di telefono
            è già presente per il contatto specificato.
        """
        
        if contact_name in self.contacts:
            lista:list[str] = self.contacts[contact_name]
            if phone_number in lista:
                    return"Errore: il numero di telefono esste già"
            else:
                 self.contacts[contact_name].append(phone_number)
        else:
            return "Errore: il contatto non esiste."
        
        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str)->dict[str,list[str]] :
        """
            Rimuove un numero di telefono dal contatto specificato.
            Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." 
            se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
        """

        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
        
        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str)->dict[str,list[str]]:
        """
            Sostituisce un numero di telefono con un altro nel contatto specificato.
            Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." 
            se il contatto non esiste oppure "Errore: il numero di telefono non è presente."
            se il numero di telefono non esiste per il contatto specificato.
        """
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                index = self.contacts[contact_name].index(old_phone_number)
                self.contacts[contact_name][index] = new_phone_number
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
        
        return {contact_name: self.contacts[contact_name]}
    
    def list_contacts(self)->list:
        """
            Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
        """
        lista:list[str] = []
        for k,v in self.contacts.items():
        
            lista.append(k)
        return lista
    
    def list_phone_numbers(self, contact_name: str)->list:
        """ 
            Mostra i numeri di telefono di un contatto specifico.
            Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste."
            se il contatto non esiste.
        """
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."
        
    def search_contact_by_phone_number(self, phone_number: str)->list: 
        """
            Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. 
            Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato
            tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono."
            se nessun contatto contiene il numero di telefono.
        """

        listak=[]
        for k,v in self.contacts.items():
            if phone_number in v:
                listak.append(k)
            
        if listak==[]:
            return("Nessun contatto trovato con questo numero di telefono.")
        else:
            return(listak)
            
        
        
# Creazione di un nuovo gestore di contatti
manager = ContactManager()
# Creazione di nuovi contatti
print(manager.create_contact("Alice", ["123456789"]))
print(manager.create_contact("Bob", ["987654321"]))
print(manager.create_contact("Charlie", ["999999999"]))

print(manager.update_phone_number("Bob", "987654321", "999999999"))

# Ricerca di contatti per numero di telefono
print(manager.search_contact_by_phone_number("999999999"))