import algorithms
import time
import os
import sys



def calculate_mean_time_qs(tests, func):
    times = []
    for test in tests:
        start_time = time.time()
        func(test)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times) * 1000


def calculate_mean_time_cs(tests, func):
    times = []
    for test in tests:
        start_time = time.time()
        func(test, len(test))
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times) * 1000


if __name__ == "__main__":
    sys.setrecursionlimit(5000)

    sample_files = os.listdir('samples')
    tests = []

    quicksort_1 = algorithms.quicksort_first_first
    quicksort_2 = algorithms.quicksort_experimental_first
    quicksort_3 = algorithms.quicksort_experimental_random
    counting_sort = algorithms.counting_sort


    for sample_file in sample_files:
        with open(f'samples/{sample_file}', 'r') as file:
            tests.append([int(n) for n in file.read().split()])

    #mean_time_1 = calculate_mean_time_qs(tests, quicksort_1)
    #mean_time_2 = calculate_mean_time_qs(tests, quicksort_2) 
    #mean_time_3 = calculate_mean_time_qs(tests, quicksort_3)
    mean_time_cs = calculate_mean_time_cs(tests, counting_sort)
    print("Counting Sort: ", round(mean_time_cs , 3))
    #print("Quicksort_1: ", round(mean_time_1 , 3))
    #print("Quicksort_2: ", round(mean_time_2 , 3))
    #print("Quicksort_3: ", round(mean_time_3 , 3))                             