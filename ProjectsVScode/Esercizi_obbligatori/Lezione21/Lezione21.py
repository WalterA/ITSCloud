 #Esercizio 1 - Crea un decorator  che stampa n volte l'output della funzione decorata chiamandola due volte.
def repeat_output(n):
    def decorator(func):
        def wrapper(*args):
            result1 = func(*args)
            result2 = func(*args)
            for _ in range(n):
                print(result1)
                print(result2)
        return wrapper
    return decorator

@repeat_output(3)
def say_hello(name):
    return f"Hello, {name}!"

# Utilizzo
say_hello("Alice")
#Esercizio 2 - Crea un decorator che calcola il tempo di esecuzione della funzione che viene decorata.
import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def some_function(delay_time):
    time.sleep(delay_time)
    return f"Function completed after {delay_time} seconds"

# Utilizzo
some_function(2)
#Esercizio 3 - Crea un decorator che permette di memorizzare informazioni sulla fibonacci in modo tale che non sia necessario ricalcolare i valori gia calcolati
def memoize_fibonacci(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

@memoize_fibonacci
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Utilizzo
print(fibonacci(10))  # 55
print(fibonacci(15))  # 610
print(fibonacci(20))  # 6765
