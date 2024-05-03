#log(len(arrey)) liste ordinate per trovare un numero
def binary_search (arrey:list[int],x:int)->int:
    low=0
    high =len(arrey)
    while low<= high:
        mid=(low + high) //2
        if arrey[mid] ==x:
            return mid
        else:
            if x>arrey[mid]:
                low =mid +1
            else:
                high =mid -1
    return None
#arrey.index(x) ricerca l'elemento in lista