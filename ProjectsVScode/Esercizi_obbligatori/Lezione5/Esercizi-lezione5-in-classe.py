def convert_temperature(temp, to_fahrenheit=True):
    if to_fahrenheit:
        return temp * 9/5 + 32
    else:
        return (temp - 32) * 5/9

def calculate_average(numbers: list[int]) -> float:
    if len(numbers):
        return sum(numbers) / len(numbers)
    else:
        return 0
lista=[1, 1, 2, 2]
def rounded_average(numbers: list[int]) -> int:
    numbers:float=sorted(numbers)
    if len(numbers) % 2 == 1:
        mid= len(numbers) // 2
        mediana=numbers[mid]
        return mediana
    else:
        mid= len(numbers) / 2
        mid=int(mid)
        mid1= mid
        mediana= (numbers[mid]+ numbers[mid1])//2
        return mediana

def rounded_average(numbers: list[int]) -> int:
    media=(sum(numbers))/len(numbers)
    round(media)
    media=int(media)
    return media

# print(rounded_average(lista))

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False
#print(find_element(lista,1))
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True or (conditionB==True and conditionC==True): 
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
# print(check_combination(True, False, True))

numbers: list[int] = [1, 2, 3, 4, 5]

for i in numbers:
    print('Number:', i)

def check_parentheses(expression: str) -> bool:
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return len(stack) == 0
lista=[]
def count_isolated(lista:list) -> int:
    conta = 0
    if lista == []:
        conta==0
    else:
        for i in range(1, len(lista)-1):
            if lista[i-1] != lista[i] and lista[i] != lista[i+1]:
                conta += 1
        if lista[0] != lista[1]:
            conta +=1
        if lista[-1] != lista[-2]:
            conta+=1
        if lista == []:
            conta==0
    return conta
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    mylist=list(original_set)
    nuova_lista=[]
    for i in mylist:
        if i not in elements_to_remove:
            nuova_lista.append(i)    
    nuova_lista=set(nuova_lista)     
    return nuova_lista
#print(remove_elements({5, 6, 7}, [7, 8, 9]))
# dict{'x': 5}, {'x': -5}{'x': 0}

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dizionario=dict1
    for k,v in dict2.items():
            if k in dizionario:
                dizionario[k]+=v
            else:
                dizionario[k]=v
    return dizionario
#print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))

