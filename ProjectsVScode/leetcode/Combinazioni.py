"""Data una stringa contenente cifre da incluso, 
restituisce tutte le possibili combinazioni di lettere che il numero potrebbe rappresentare.
Restituisci la risposta in qualsiasi ordine.2-9"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mappatura: dict[str, list[str]] = {
            "1": [""], "2": ["a", "b", "c"],
            "3": ["d", "e", "f"], "4": ["g", "h", "i"],
            "5": ["j", "k", "l"], "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"], "0": [" "]
        }
        
        if not digits:
            return []
        
        risultato = [""]
        
        for digit in digits:
            if digit in mappatura:
                temp = []
                for comb in risultato:
                    for letter in mappatura[digit]:
                        temp.append(comb + letter)
                risultato = temp
        
        return risultato

sol = Solution()
print(sol.letterCombinations("23"))
