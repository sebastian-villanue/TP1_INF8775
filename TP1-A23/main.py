import algorithms
import time
import os




def calculate_mean_time(tests, func):
    times = []
    for test in tests:
        start_time = time.time()
        func(test)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times) * 1000


if __name__ == "__main__":
    sample_files = os.listdir('samples')
    tests = []

    quicksort_1 = algorithms.quicksort_first_first
    quicksort_2 = algorithms.quicksort_experimental_first
    quicksort_3 = algorithms.quicksort_experimental_random

    for sample_file in sample_files:
        with open(f'samples/{sample_file}', 'r') as file:
            tests.append([int(n) for n in file.read().split()])

    mean_time = calculate_mean_time(tests, quicksort_1) 
    print(mean_time)          