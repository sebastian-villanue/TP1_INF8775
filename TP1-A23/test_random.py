import algorithms
import matplotlib.pyplot as plt
import constants
import time
import random

def quicksort(arr, threshold=10):
    if len(arr) <= threshold:
        # Use insertion sort for small subarrays
        return insertion_sort(arr)
    # Random index generated here
    random_index = random.randint(0, len(arr)-1)
    pivot = arr[random_index]
    lesser = []
    greater = []

    for element in arr[1:]:
        if element < pivot:
            lesser.append(element)
        else:
            greater.append(element)

    return quicksort(lesser, threshold) + [pivot] + quicksort(greater, threshold)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
# original_list = [3, 6, 8, 10, 1, 2, 1]
# sorted_list = quicksort(original_list, threshold=5)
# print(sorted_list)

if __name__ == "__main__":
    algorithms.access_files()
    display = True
    times_plot = []
    array = [int(element) for element in algorithms.samples[0].split()]


    for ths in constants.TEST_THRESHOLDS:
        start = time.time()
        quicksort(array, ths)
        end = time.time()
        times_plot.append(end-start)

    plt.plot(constants.TEST_THRESHOLDS, times_plot, marker='o', linestyle='-')

    plt.xlabel('Thresholds')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time vs. Threshold')

    plt.show()