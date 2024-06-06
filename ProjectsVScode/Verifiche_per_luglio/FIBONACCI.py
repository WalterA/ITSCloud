def fibonacci(i:int):
    a = 1
    b = 1
    for _ in range(i):
        c = a + b
        a = b 
        b = c 
    return b

print(fibonacci(2))