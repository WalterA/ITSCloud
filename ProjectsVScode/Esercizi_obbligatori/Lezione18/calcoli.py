class FormulaError(Exception):
    """Eccezione personalizzata per input di formula non validi."""
    pass

class Calculator:
    def calculate(self, formula):
        try:
            # Dividi la formula nei componenti
            parts = formula.split()
            
            # Verifica se la formula è composta da 3 parti
            if len(parts) != 3:
                raise FormulaError("Formato della formula non valido. Atteso: 'numero operatore numero'.")
            
            # Estrai i componenti
            num1_str, operator, num2_str = parts
            
            # Converti num1 e num2 in float
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
            except ValueError:
                raise FormulaError("Formato numero non valido. I numeri devono essere float validi.")
            
            # Verifica se l'operatore è valido
            if operator not in ('+', '-'):
                raise FormulaError("Operatore non valido. Gli operatori supportati sono '+' e '-'.")
            
            # Esegui il calcolo in base all'operatore
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            
            # Stampare il risultato del calcolo
            print(f"Risultato: {result}")
        
        except FormulaError as e:
            print(f"Errore: {e}")
        except Exception as e:
            print(f"Errore imprevisto: {e}")

# Esempio di utilizzo del calcolatore interattivo
if __name__ == "__main__":
    calc = Calculator()
    
    while True:
        formula = input("Inserisci una formula (oppure 'quit' per uscire): ")
        
        if formula.lower() == 'quit':
            print("Arrivederci!")
            break
        
        calc.calculate(formula)
