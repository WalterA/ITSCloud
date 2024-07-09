
def mergeSort(list_input: list[int]) -> list[int]:
    """
    
    """
    if len(list_input) == 1:
        
        return list_input
    
    mid_point: int = len(list_input) // 2
    
    left_list: list[int] = mergeSort(list_input[:mid_point])
    right_list: list[int] = mergeSort(list_input[mid_point:])
    result: list[int] = merge(left_list, right_list)
    
    return result

def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    
    i, j = 0, 0

    result: list[int] = [None for _ in range(len(list_1 + list_2))]
    
    for k in range(len(result)):
        if list_1[i] > list_2[j]:
            result[k] = list_2[j]
            j += 1
            
            if j == len(list_2):
                return result[:k+1] + list_1[i:]
            
        else:
            result[k] = list_1[i]
            i += 1
            
            if i == len(list_1):
                
                return result[:k+1] + list_2[j:]