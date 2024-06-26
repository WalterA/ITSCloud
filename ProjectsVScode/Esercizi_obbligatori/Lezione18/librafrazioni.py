class FractionError(Exception):
    """Eccezione personalizzata per errori relativi alle frazioni."""
    pass

class Fraction:
    def __init__(self, numerator, denominator):
        try:
            if denominator == 0:
                raise FractionError("Il denominatore non può essere zero.")
            
            self.numerator = numerator
            self.denominator = denominator
            self._simplify()
        
        except FractionError as e:
            print(f"Errore nella frazione: {e}")
    
    def _simplify(self):
        """Semplifica la frazione dividendo numeratore e denominatore per il loro MCD."""
        gcd_value = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value
    
    def _gcd(self, a, b):
        """Funzione ausiliaria per trovare il massimo comune divisore usando l'algoritmo di Euclide."""
        while b:
            a, b = b, a % b
        return a
    
    def get_numerator(self):
        return self.numerator
    
    def get_denominator(self):
        return self.denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __eq__(self, other):
        """Verifica se due frazioni sono equivalenti."""
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def add(self, other):
        """Esegue l'addizione tra due frazioni."""
        try:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except FractionError as e:
            print(f"Errore nell'addizione delle frazioni: {e}")
    
    def subtract(self, other):
        """Esegue la sottrazione tra due frazioni."""
        try:
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except FractionError as e:
            print(f"Errore nella sottrazione delle frazioni: {e}")
    
    def multiply(self, other):
        """Esegue la moltiplicazione tra due frazioni."""
        try:
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        except FractionError as e:
            print(f"Errore nella moltiplicazione delle frazioni: {e}")
    
    def divide(self, other):
        """Esegue la divisione tra due frazioni."""
        try:
            if other.numerator == 0:
                raise FractionError("Impossibile dividere per zero.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        except FractionError as e:
            print(f"Errore nella divisione delle frazioni: {e}")
    
# Esempio di utilizzo della libreria di frazioni
if __name__ == "__main__":
    try:
        frac1 = Fraction(1, 2)
        frac2 = Fraction(3, 4)
        
        print(f"frac1: {frac1}")
        print(f"frac2: {frac2}")
        
        sum_result = frac1.add(frac2)
        print(f"Sum: {sum_result}")
        
        diff_result = frac1.subtract(frac2)
        print(f"Difference: {diff_result}")
        
        prod_result = frac1.multiply(frac2)
        print(f"Product: {prod_result}")
        
        div_result = frac1.divide(frac2)
        print(f"Division: {div_result}")
        
        if frac1 == Fraction(2, 4):
            print("frac1 is equivalent to 2/4")
        else:
            print("frac1 is not equivalent to 2/4")
            
    except FractionError as e:
        print(f"Errore nelle operazioni con le frazioni: {e}")
