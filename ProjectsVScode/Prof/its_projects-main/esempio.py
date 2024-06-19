def mergeSort(list_input: list[int]) -> list[int]:
    """
    
    """
    if len(list_input) == 1:
        
        return list_input
    
    mid_point: int = len(list_input) // 2
    
    left_list: list[int] = mergeSort(list_input=list_input[:mid_point])
    right_list: list[int] = mergeSort(list_input=list_input[mid_point:])
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

if __name__ == "__main__":
    
    import random
    import time
    import matplotlib.pyplot as plt
    
    merge_sort_times: list[float] = []
    bubble_sort_times: list[float] = []
    cases = [10, 50, 100, 250, 500, 1000, 1500, 2000, 5000, 10000, 20000]
    for n in cases:
        
        list_input: list[int] = [random.randint(0, 100000) for _ in range(n)]
        
        start = time.time()    
        result: list[int] = mergeSort(list_input=list_input)
        end = time.time()
        
        merge_sort_times.append(end-start)
            
        start = time.time()
        result: list[int] = bubble_sort_v2(x=list_input)
        end = time.time()
        
        bubble_sort_times.append(end-start)
        
    print(f"MERGE: {merge_sort_times}\nBUBBLE: {bubble_sort_times}")
    plt.plot(cases, merge_sort_times, label="Merge")
    plt.plot(cases, bubble_sort_times, label="Bubble")
    plt.xscale("log")
    plt.legend()
    plt.show()
# class Esempio:
    
#     def __init__(self, name) -> None:
        
#         self.__name = self.__checkName(name)
#         self.__attr_1 = None
#         self._attr_1 = None
#         self.attr_1 = None
        
        
#     def __checkName(self, name: str):
        
#         #
        
        
#         return name.capitalize()      
        
#     def setName(self, name: str):
                
#         self.attr_1 = self.__checkName(name)
        


# es = Esempio()

# es.attr_1 = "fLAvIo"

# "Flavio"



# # reader = open("files/esempio.txt")
# # print(reader)

# # reader.close()

# # with open(f"files/esempio.txt") as f:
    
# #     print()


# # reader = open("files/esempio.txt")
    
# # try:
    
# #     reader.readline()
# #     print("Sono nella try")
# #     raise Exception("Eccezione!")
    
# # except Exception:
    
# #     print("Sono nella except")
    
# # finally:
    
# #     print(reader)

# #     reader.close()    
        
# #     print("sono nella finally")
    
 
# with open("files/esempio.txt", "a") as reader:
#     l = [f"Ciao sono Flavio\n", f"Ciao sono Maria\n", f"Ciao sono Luca\n"]
#     reader.writelines(l)
    
 
    
# # with open("files/esempio.txt") as reader:
    
# #     line = reader.readline()
# #     line_counter = 0
# #     while line != '':
        
# #         print(f"{line} - number: {line_counter}")
# #         line = reader.readline()
# #         line_counter += 1
    
    
    
# class VotoTroppoBassoError(Exception):
    
#     # def __init__(self, *args: object) -> None:
#     #     super().__init__(*args)
#     pass


# class VotoBruttissimo(VotoTroppoBassoError):
    
#     pass
  
    
# # class ContextManager:
    
# #     def __enter__(self):
        
# #         print("Ciao sono nell'enter")
        
# #         return self
    
# #     def __exit__(self, exc_type, exc_value, traceback):
        
# #         if exc_type is not None:
            
# #             print("Eccezione")
            
# #         return False
        

# try:
    
#     print("Sono nel try")
#     raise VotoTroppoBassoError("Prova")
            
# except ZeroDivisionError as e:
        
#     print("Sono nel ZeroDiv")
    
# except ValueError as e:
    
#     print("Sono nel ValueError")

# except ImportError as e:
    
#     print(f"Warning: {e}")
    
# except VotoTroppoBassoError as e:
    
#     print(f"Warning: {e}")
    
# else:
    
#     print("Sono nell'else")
          
# finally:
    
#     print("Sono nel finally")
    
    
# import time
# from contextlib import contextmanager

# @contextmanager
# def timer():
    
#     start = time.time()
#     print("__enter__")
    
#     yield "Ciao"
    
#     print("__exit__")
#     end = time.time()
#     elapsed_time = end -start
    
#     print(f"time elapsed: {elapsed_time}")
    
    
# if __name__ == "__main__":
    
    
#     with timer() as t:
#         print(t)
#         print("with")
#         time.sleep(1)
        


    