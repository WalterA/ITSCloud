from typing import Any


class ContoBancario:
    
    total_accounts: int = 0 
    definizione: str = "Classe<ContoBancario>"

    def __init__(self, iban: int, saldo: int, nome: str):
        self.iban: int = iban
        self.nome: str = nome
        self.saldo: int = saldo
        
        ContoBancario.total_accounts += 1

    def deposito(self, importo: int):

        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è {self.saldo}')

    def prelievo(self, importo: int):
        self.saldo -= importo
        print(f'{importo} prelevato. Il nuovo saldo è {self.saldo}')
        
    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_accounts}')

    @classmethod
    def get_type(cls):
        print(f'Type: {cls.definizione}')

    @staticmethod
    def valida_account(iban: Any):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print('iban valido')
            return True
        else:
            print('iban non valido')
            return False
        
        
d: dict[str, Any] = {
    "a": ["ciao", "ciao"],
    "a": 1
}

class ContoBancarioFiglio(ContoBancario):
    
    total_conto_bancario_figlio = 0
    
    def __init__(self, iban, saldo, nome):
        super().__init__(iban, saldo, nome)
        
        ContoBancarioFiglio.total_conto_bancario_figlio += 1
        
    @classmethod
    def get_total_conto_bancario_figlio(cls):
        print(f"Numero account figlio: {cls.total_conto_bancario_figlio}")

cbf_1 = ContoBancarioFiglio(iban=124122, saldo=0, nome="Chiara")

ContoBancarioFiglio.get_total_accounts()

account1 = ContoBancario(1234567890, 0, 'Alice')
account2 = ContoBancario(9876543210, 1000, 'Bob')

account1.deposito(500)
account1.prelievo(200)

account2.deposito(200)
account2.prelievo(150)

ContoBancario.get_total_accounts()
ContoBancario.get_type()
account3 = ContoBancario(1234567890, 0, 'Bob')

ContoBancario.get_total_accounts()


ContoBancario.valida_account(1234567890)
ContoBancario.valida_account('12345ABCD')

# def valida_account(iban):
#         if isinstance(iban, int) and len(str(iban)) == 10:
#             print('iban valido')
#             return True
#         else:
#             print('iban non valido')
#             return False
        
        
# valida_account(iban=123821413)



class Utility:
    
    
    @staticmethod
    def utility_1():
        
        pass
    
    @staticmethod
    def utility_2():
        
        pass
    
    @staticmethod
    def utility_3():
        
        pass
    
    @staticmethod
    def utility_4():
        
        pass
    

Utility.utility_1()
Utility.utility_2()
Utility.utility_3()