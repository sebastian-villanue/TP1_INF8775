import matplotlib.pyplot as plt
from time import time
import algorithms
import constants
import sys

#---------- Début du code généré par ChatGPT --------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr

    if threshold < 0:
        raise ValueError("Threshold should be a non-negative integer.")

    if len(arr) > 1:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left, threshold) + middle + quicksort(right, threshold)
    else:
        return arr
#---------- Fin du code généré par ChatGPT --------------

def calculate_mean_time(times):
    for key in times.keys():
        times[key] = times[key]/10

def calculate_time():
    for i in range(1,10):
        array = [int(element) for element in algorithms.samples[i].split()]
        for ths in constants.TEST_THRESHOLDS:
            print('threshold is')
            print(ths)
            t0 = time()
            sol = quicksort(array, ths)
            t = (time() - t0)*1000
            times[f'{ths}'] += t

            if display : 
                print(sorted(array) == sol) 
                print(t, 'ms')
    calculate_mean_time(times)
    for key in times.keys():
        if times[key] == min(times.values()):
            print('best threshold is')
            print(key)
            scores[key] += 1

def initialize_dictionary():
    for ths in constants.TEST_THRESHOLDS:
        times[f'{ths}'] = 0

def initialize_scores():
    for ths in constants.TEST_THRESHOLDS:
        scores[f'{ths}'] = 0

if __name__ == "__main__":
    algorithms.access_files()
    sys.setrecursionlimit(2000)

    display = True
    times = {}
    times_plot = []
    scores = {}

    initialize_scores()

    for i in range(20):
        initialize_dictionary()
        calculate_time()
    print(scores)

    plt.plot(constants.TEST_THRESHOLDS, scores.values(), marker='o', linestyle='-')

    plt.xlabel('Thresholds')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Threshold')

    plt.grid(True)
    plt.show()
