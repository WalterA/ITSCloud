"""Implementing Static Methods"""

class MathOperations:

    @staticmethod
    def add(n1: float, n2: float) -> float:
        return n1 + n2

    @staticmethod
    def multiply(n1: float, n2: float) -> float:
        return n1 * n2

# Esempio di utilizzo
num1 = 5
num2 = 6

# Utilizzo dei metodi statici
sum_result = MathOperations.add(num1, num2)
product_result = MathOperations.multiply(num1, num2)

print(f"La somma di {num1} e {num2} è: {sum_result}")
print(f"Il prodotto di {num1} e {num2} è: {product_result}")
