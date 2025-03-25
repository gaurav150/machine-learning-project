### Multithreading
# Multithreading is a way to run multiple threads concurrently.
# Threads are lightweight sub-processes, a way to achieve multitasking.
# Each thread uses the same memory space.
# Threads are used to perform multiple tasks at the same time.
# Threads are used to perform background tasks.
# Threads are used to handle parallel execution of tasks.
# Threads are used to handle I/O operations.
# Threads are used to handle tasks that require waiting.
# Threads are used to handle tasks that require blocking.
# Threads are used to handle tasks that require sleeping.
# Threads are used to handle tasks that require a delay.
from threading import Thread
# import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
        

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")

## create two threads
t1 = Thread(target=print_numbers)
t2 = Thread(target=print_letters)


t = time.time()
## start the timer
t1.start()
t2.start()

## wait for the threads to finish
t1.join()
t2.join()
finished_time = time.time()-t
print(f"Time taken: {finished_time}")