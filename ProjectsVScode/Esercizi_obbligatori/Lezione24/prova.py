from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
    
    def codifica(self, testoInChiaro: str) -> str:
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1 = alfabeto.lower()
        s2 = testoInChiaro.lower()
        encrypted_message = ""

        for char in s2:
            if char in s1:
                index = s1.index(char)
                new_index = (index + self.chiave) % len(s1)
                encrypted_message += s1[new_index]
            else:
                encrypted_message += char

        return encrypted_message

    def _decodifica_carattere(self, char: str) -> str:
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s1 = alfabeto.lower()
        if char in s1:
            index = s1.index(char)
            new_index = (index - self.chiave) % len(s1)
            return s1[new_index]
        return char

    def decodifica(self, testoCodificato: str) -> str:
        decrypted_message = ""
        for char in testoCodificato:
            decrypted_message += self._decodifica_carattere(char)
        return decrypted_message

    def leggi_da_file(self, filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()

    def scrivi_su_file(self, filename: str, testo: str) -> None:
        with open(filename, 'w') as file:
            file.write(testo)

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int) -> None:
        self.n = n

    def _combinazione(self, testoInChiaro: str) -> str:
        index = len(testoInChiaro) // 2

        if len(testoInChiaro) % 2 == 0:
            sx = testoInChiaro[:index]
            dx = testoInChiaro[index:]
        else:
            sx = testoInChiaro[:index + 1]
            dx = testoInChiaro[index + 1:]

        combined = []
        for s, d in zip(sx, dx):
            combined.append(s)
            combined.append(d)

        # If sx is longer, add the last character from sx
        if len(sx) > len(dx):
            combined.append(sx[-1])

        return ''.join(combined)

    def codifica(self, testoInChiaro: str) -> str:
        for _ in range(self.n):
            testoInChiaro = self._combinazione(testoInChiaro)
        return testoInChiaro

    def _decodifica_combinazione(self, testoCodificato: str) -> str:
        if len(testoCodificato) % 2 == 0:
            first_half_length = len(testoCodificato) // 2
        else:
            first_half_length = (len(testoCodificato) // 2) + 1

        first_half = testoCodificato[:2*first_half_length:2]
        second_half = testoCodificato[1:2*first_half_length:2]
        
        return first_half + second_half

    def decodifica(self, testoCodificato: str) -> str:
        for _ in range(self.n):
            testoCodificato = self._decodifica_combinazione(testoCodificato)
        return testoCodificato

    def leggi_da_file(self, filename: str) -> str:
        with open(filename, 'r') as file:
            return file.read()

    def scrivi_su_file(self, filename: str, testo: str) -> None:
        with open(filename, 'w') as file:
            file.write(testo)

# Example usage for CifratoreAScorrimento
cifratore_scor = CifratoreAScorrimento(3)
testo_in_chiaro = "abcdefghi"
testo_cifrato = cifratore_scor.codifica(testo_in_chiaro)
print("Cifrato:", testo_cifrato)
print("Decifrato:", cifratore_scor.decodifica(testo_cifrato))

# Example usage for CifratoreACombinazione
cifratore_comb = CifratoreACombinazione(1)
testo_cifrato_comb = cifratore_comb.codifica(testo_in_chiaro)
print("Cifrato combinato:", testo_cifrato_comb)
print("Decifrato combinato:", cifratore_comb.decodifica(testo_cifrato_comb))
