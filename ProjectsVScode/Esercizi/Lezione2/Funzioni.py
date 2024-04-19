# def subtract (x:float,y:float) -> float:
#     differenza:float=x-y
#     return differenza
# x,y =float(input("inserisci il primo numero")),float(input("inserisci il secondo numero"))
# diff=(subtract(x,y))
# print(f"numero è:{x} meno {y} e uguale {diff}")

l=[2,9,0,-1,25,2,4,3,9]
# def median (l:list[float])-> float:
#     l:float=sorted(l)
#     print(l)
#     if len(l) % 2 == 1:
#             mid= len(l) // 2
#             mediana=l[mid]
#             return mediana
#     else:
#         mid= len(l) // 2
#         mid1= mid -1 
#         mediana= (l[mid]+ l[mid1])/2
#         return mediana
# print(median(l))



# #fatta dal prof
# def median (l:list[float])-> float:
#     l=sorted(l)
#     mid=len(l) //2
#     # se len(l) =8, mid =4
#     if len(l) % 2 != 0: #dispari
#         mediana=l[mid]
#     else:#pari
#         mediana=(l[mid] + l[mid - 1]) /2
#     return mediana
# print(median(l))

l=[1,2,3,4,5,6]
def diff_cum(l:list[float]) -> float:
    sottrazione=l[0]
    for i in range(len(l)-1):
       sottrazione -= l[i+1]

       print(sottrazione)

    
# #fatto dal prof
# l=[1,2,3,4,5,6]
# def diff_cum(l:list[float]) -> float:
#     sottrazione=l[0]
#     for i in l[1:]:
#        sottrazione -= i
#        print(sottrazione)
    
# diff_cum(l)

l=[1,2,3,4,5,6]
# def diff_cum(l:list[float]) -> float:
#     for i in l:
#        numero=l.pop(2)
#        numero -= i
#        print(numero)
    
# diff_cum(l)

def diff_cum(l:list[float],index:int) -> float:
    if -len(l) <= index <len(l): #index <len(l) and index >= -len(l)
        fulcro=l[index]
        for i in range(len(l)):
         if i != index:
            fulcro-=l[i]
        return fulcro
    
print(diff_cum(l, 3))