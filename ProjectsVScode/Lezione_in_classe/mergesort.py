import time


def mergesort(lista_input: list[int])-> list[int]:
    """
    """
    if len(lista_input) == 1:
        return lista_input
    mid_point: int = len(lista_input) // 2
    leftlist:list[int] = mergesort(lista_input=lista_input[:mid_point])
    rightlist:list[int] = mergesort(lista_input=lista_input[mid_point:])
    print(f"L:{leftlist}R:{rightlist}")
    result = merge(leftlist,rightlist)
    return result

def merge (list1:list[int], lista2:list[int])-> list[int]:
    i, j = 0,0
    result:list[int] = [None for _ in range(len(list1 + lista2))]
    for k in range(len(result)):
        if list1[i] > lista2[j]:
            result[k] = lista2[j]
            j+=1
            if j == len(lista2):
                return result[k:+1] + list1[i:]
        else:
            result[k] = list1[i]
            i += 1
            if i == len(list1):
                return result[:k+1] + lista2[j:]
            
        
def bubble_sort_v2(x: list[int]):
    # Ω(n) -> caso migliore quando la lista è già ordinata
    # O(n^2) -> caso peggiore
    ho_fatto_swap: bool = True
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j+1]:
                # swap(x[j], x[j+1])
                ho_fatto_swap = False
                temp: int = x[j]
                x[j] = x[j+1]
                x[j+1] = temp
        if ho_fatto_swap:
            break  
    
if __name__== "__main__":
    merge_sort_times=[]
    bubble_srt_times=[]
    
    lista_input:list[int] =[0, 1, 2, 3,4 , 5, 6,7]
    time.time
    result = mergesort(lista_input=lista_input)
    print(result)
    
