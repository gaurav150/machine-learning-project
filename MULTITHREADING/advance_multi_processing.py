### Multiprocessing with ProcessPoolExecutor
# ## The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously.

from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(number):
    time.sleep(4)
    return f"Square: {number*number}"

# def cube_numbers(number):
#     time.sleep(1.5)
#     return f"Cube: {number*number*number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15, 16, 17, 18, 19, 20]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_numbers, numbers)

        for result in results:
            print(result)
