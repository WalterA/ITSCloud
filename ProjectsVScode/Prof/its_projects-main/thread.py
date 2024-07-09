import threading
import time
import concurrent.futures


def thread_function(name):
    print(f"Thread {name}: starting at {time.time()}")
    time.sleep(2)
    print(f"Thread {name}: finishing at {time.time()}")

# if __name__ == "__main__":

#     x = threading.Thread(target=thread_function, args=(1,))
#     print(f"Main    : before running thread")
#     x.start()
#     print(f"Main    : wait for the thread to finish")
#     x.join()
#     print(f"Main    : all done")
    
    

# if __name__ == "__main__":

#     threads = list()
#     for index in range(3):
#         print(f"Main    : before running thread")
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         print(f"Main    : wait for the thread to finish")
#         thread.join()
#         print(f"Main    : all done")
        



if __name__ == "__main__":

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(thread_function, range(300))