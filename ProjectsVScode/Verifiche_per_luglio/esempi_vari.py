from collections import Counter

def find_unique_number(list1, list2):
    # Combina le due liste
    combined_list = list1 + list2
    
    # Conta le occorrenze di ogni elemento
    count = Counter(combined_list)
    
    # Trova l'elemento che appare una sola volta
    for num in count:
        if count[num] == 1:
            return num

# Esempio di liste
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 6]

unique_number = find_unique_number(list1, list2)
print(f"Il numero unico è: {unique_number}")

from collections import Counter

def find_unique_character(str1, str2):
    # Combina le due stringhe
    combined_str = str1 + str2
    
    # Conta le occorrenze di ogni carattere
    count = Counter(combined_str)
    
    # Trova il carattere che appare una sola volta
    for char in count:
        if count[char] == 1:
            return char

# Esempio di stringhe
str1 = "abcd"
str2 = "abcf"

unique_character = find_unique_character(str1, str2)
print(f"Il carattere unico è: {unique_character}")

def find_missing_number_and_position(lst):
    # Assumiamo che la lista sia ordinata e contenga numeri consecutivi
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1] + 1:
            # Il numero mancante è lst[i-1] + 1
            # La posizione è i
            return (lst[i-1] + 1, i)
            # numero = lst[i-1] + 1
            # posizione = i
            # return numero, posizione
    
    # Se non c'è nessun numero mancante, restituire None
    return None

# Esempio di lista
lst = [1, 2, 3, 5, 6]

missing_number, position = find_missing_number_and_position(lst)
print(f"Il numero mancante è: {missing_number}, alla posizione: {position}")


from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        lista:list = Counter(nums)
        for i in lista:
            if lista[i] == 1:
                return i
nums = [2,2,1]
ok=Solution()
print(ok.singleNumber(nums))