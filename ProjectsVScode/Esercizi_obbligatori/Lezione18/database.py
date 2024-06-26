class DateDatabase:
    def __init__(self):
        self.dates = {}  # Dizionario per memorizzare le date nel formato 'gg.mm.aaaa'

    def aggiungi_data(self, data_str):
        """Aggiunge una nuova data al database."""
        try:
            self._valida_formato_data(data_str)
            self.dates[data_str] = True
            print(f"Data '{data_str}' aggiunta al database.")
        except ValueError as e:
            print(str(e))

    def elimina_data(self, data_str):
        """Elimina una data specificata dal database."""
        try:
            self._valida_formato_data(data_str)
            if data_str in self.dates:
                del self.dates[data_str]
                print(f"Data '{data_str}' eliminata dal database.")
            else:
                print(f"Data '{data_str}' non trovata nel database.")
        except ValueError as e:
            print(str(e))

    def modifica_data(self, vecchia_data_str, nuova_data_str):
        """Modifica una data nel database."""
        try:
            self._valida_formato_data(vecchia_data_str)
            self._valida_formato_data(nuova_data_str)
            if vecchia_data_str in self.dates:
                del self.dates[vecchia_data_str]
                self.dates[nuova_data_str] = True
                print(f"Data '{vecchia_data_str}' modificata in '{nuova_data_str}'.")
            else:
                print(f"Data '{vecchia_data_str}' non trovata nel database.")
        except ValueError as e:
            print(str(e))

    def query_data(self, data_str):
        """Interroga una data specificata nel database."""
        try:
            self._valida_formato_data(data_str)
            if data_str in self.dates:
                print(f"Data '{data_str}' trovata nel database.")
            else:
                print(f"Data '{data_str}' non trovata nel database.")
        except ValueError as e:
            print(str(e))

    def _valida_formato_data(self, data_str):
        """Valida il formato della data (gg.mm.aaaa)"""
        if not isinstance(data_str, str) or len(data_str) != 10:
            raise ValueError("Formato data non valido. Il formato atteso è 'gg.mm.aaaa'.")
        parti = data_str.split('.')
        if len(parti) != 3 or not all(parte.isdigit() for parte in parti):
            raise ValueError("Formato data non valido. Il formato atteso è 'gg.mm.aaaa'.")
        giorno, mese, anno = int(parti[0]), int(parti[1]), int(parti[2])
        if giorno < 1 or giorno > 31 or mese < 1 or mese > 12 or anno < 1000 or anno > 9999:
            raise ValueError("Valori della data non validi. Verificare i valori di giorno, mese e anno.")

# Esempio di utilizzo:
if __name__ == "__main__":
    db = DateDatabase()

    db.aggiungi_data("15.06.202")
    db.aggiungi_data("25.12.2023")
    db.aggiungi_data("01.01.2023")

    db.query_data("15.06.2024")
    db.query_data("31.12.2024")

    db.modifica_data("01.01.2023", "01.01.2025")
    db.modifica_data("01.01.2024", "01.01.2025")

    db.elimina_data("25.12.2023")
    db.elimina_data("31.12.2024")

    db.query_data("25.12.2023")
    db.query_data("01.01.2025")
