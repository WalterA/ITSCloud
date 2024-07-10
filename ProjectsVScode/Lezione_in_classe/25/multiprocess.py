from multiprocessing import  Process
import time

def bubble_sort():
    from  random import randint
    x=[randint(0,10000)for _ in range(5000)]
    ho_fatto=True
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                ho_fatto=False
                temp=x[j]
                x[j] = x[j+1]
                x[j+1]=temp
        if ho_fatto:
            break
            
def sleep():
    print('non ho voglia')
    time.sleep(60)
    print("vabbè")

if  __name__== "__main__":
    tic:float=time.time()
    
    t1= Process(target=bubble_sort)
    t2= Process(target=bubble_sort)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    toc:float=time.time()
    time_elapsed: float =toc-tic
    print(f'{time_elapsed=}')