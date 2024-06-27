#-----------------------decoration------------------------ 
import time

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