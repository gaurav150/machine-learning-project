### Multithreading With Thread Pool Executor 
# Thread pool executor is a way to manage threads in a pool.

from concurrent.futures import ThreadPoolExecutor
import time


def print_numbers(number):
    time.sleep(2)
    return f"Number: {number}"

# def print_letters(letter):
#     time.sleep(2)
#     return f"Letter: {letter}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

    for result in results:
        print(result)