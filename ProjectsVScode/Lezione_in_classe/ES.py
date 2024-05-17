
# """
# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
# """




class Account:
    
     def __init__(self,account_id:str,balance= 0)-> None:
         self.account_id = account_id
         self.balance = balance
        
     def deposit(self, amount:float):
         self.balance += amount
    
     def get_balance(self):
         return self.balance

class Bank:
    def __init__(self) -> None:
         self.accounts: dict[str, Account] = {}
        
    def create_account(self, account_id):
        if account_id in self.accounts:
            raise ValueError( "Account with this ID already exists")
        else:
            account= Account(account_id)
            self.accounts[account_id] = account
            return account
    
    def deposit(self,account_id,amount):
        if account_id in self.accounts:
             self.accounts[account_id].deposit(amount)
        else:
             return "Id error"

    def get_balance(self,account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
             raise ValueError("Account not found")
    
# utente = Account("pippi")  
bank = Bank()
account = Bank.create_account("1234")
# account = bank.create_account("1234")
# bank.deposit("1234", 100)
# balance = bank.get_balance("1234")
# print(balance)

# """Data una stringa s e una lista di stringhe wordDict, 
# restituisce True se s può essere segmentato in una sequenza separata da
# spazi di una o più parole del dizionario; False altrimenti.

# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione."""  
    
# def word_break(s: str, wordDict: list[str]) -> bool:
#     x= True
#     for _ in wordDict:
#         if s == wordDict:
#             return x
#         else:
#             x

# print(word_break("leetcode" , ["leet","code"]))


# """
# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

# La lista di interi è formata così:

#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.
# """
# # def binary_search (arrey:list[int],x:int)->int:
# #     low=0
# #     high =len(arrey)
# #     while low<= high:
# #         mid=(low + high) //2
# #         if arrey[mid] ==x:
# #             return mid
# #         else:
# #             if x>arrey[mid]:
# #                 low =mid +1
# #             else:
# #                 high =mid -1
# #     return None
# # def visit_tree(tree, node):
# #     print(node)
# #     left_child, right_child=tree.get(node, [None,None])
# #     if left_child:
# #         visit_tree(tree, left_child)
# #     if right_child:
# #         visit_tree(tree, right_child)
        
# class TreeNode:
    
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def visit_tree(tree, node):
#         left_child, right_child=tree.get(node, [None,None])
#         if left_child:
#             visit_tree(tree, left_child)
#         if right_child:
#             visit_tree(tree, right_child)
        
# def symmetric(tree: list[int]) -> bool:
#     # scrivere qui la vostra funzione
#     pass
# """
# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola
# o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.
# """
# def anagram(s: str, t: str) -> bool:
#     t=t.lower().replace(" ","")
#     s=s.lower().replace(" ","")
    
#     if sorted(t)== sorted(s):
#           return True
#     else:
#           return False

# print(anagram("anagram","nagaram"))



    
        