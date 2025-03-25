## PRocess that run in parallel
## CPU bound tasks - tASKS THAT REQUIRE HEAVY USAGE OF CPU
## I/O bound tasks
## Multiprocessing is a way to run multiple processes concurrently.
## PARALLEL execution of tasks
## Each process has its own memory space.

# import multiprocessing as mp
from multiprocessing import Process

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")
        

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":

    ## create two processes
    p1 = Process(target=square_numbers)
    p2 = Process(target=cube_numbers)

    t = time.time()
    ## start the timer
    p1.start()
    p2.start()

    ## wait for the processes to finish
    p1.join()
    p2.join()
    finished_time = time.time()-t
    print(f"Time taken: {finished_time}")
