#-----------------------decoration------------------------ 
import time
from contextlib import contextmanager

def say_hello(name:str) ->None:
    
    print(f"Hello,flavio{name}")

def say_ciao(name) ->None:
    
    print(f"Ciao,flavio{name}")
    
# def saluta(func):
    
#     func("Flavio")
    
# saluta(say_ciao)


# def parent():
#     print("Sono in parent")
#     def first_child():
#         print(f"sono in firstchild")
#     def second_child():
#         print(f"sono in second")

#     return second_child
    
# ok = parent()
# parent()
# print(ok)
# ok()


#-------*arg qualsiasi numero di argomento

def decor(func):
    
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        elapsed_time = end - start 
        print(f"{elapsed_time=}")
        
    return wrapper 

@decor
def ciao ()->None:
    print("ciao")
    
@decor
def random_list ( upper_bound:int):
    import random
    import time
    sleep_time:int = random.randint(0,upper_bound)
    time.sleep(sleep_time)
random_list(8)
# ciao()
# say_hello = decorator(say_hello)
# say_hello("wa")
# say_ciao = decorator(say_ciao)
# say_ciao("wa")

def generatore():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    
# prova = generatore()
# print(next(prova))
# print(next(prova))
# print(next(prova))
# print(next(prova))
# print(next(prova))

@contextmanager
def decor_manager(*args):
    
   
        start = time.time()
        
        yield
        end = time.time()
        elapsed_time = end - start 
        print(f"{elapsed_time=}")
        
  

with decor_manager() as _:
    print("ciao")

def funzione(id:int):
    import time
    import random
    sleep_time : int = random.randint(1,10)
    print(f"{id=} time{time.time()}")
    time.sleep(sleep_time)
    print(f"{id=}time {time.time()}")
    
if __name__ == "__main__":
    
    import threading
    from concurrent.futures import ThreadPoolExecutor
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(funzione, range(10))
    
    
    
    # lista_t:list[threading.Thread] = []
    
    # for id in range(1):
    #     x: threading.Thread= threading.Thread(target=funzione,args=(id,))
    #     lista_t.append(x)
    #     print(f"prima di rannare il thred {time.time()} ")
    #     x.start()
    #     print(f"ho rannato{time.time()}")
    # for t in lista_t:
    #     t.join()
    #     print(f"Terminato")
    
