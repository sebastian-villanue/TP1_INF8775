import argparse
import random
import sys
import time

THRESHOLD_ONE = 1
THRESHOLD_EXPERIMENTAL_FIRST = 12 ## See section in the lab report
THRESHOLD_EXPERIMENTAL_RANDOM = 19 ## See section in the lab report
TEST_THRESHOLDS = list(range(1,50))


## Insertion Sort used in the quicksort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


## Quicksort with a recursion threshold of 1 and with the pivot being the first element of the array
def quicksort_first_first(arr):
    if len(arr) <= THRESHOLD_ONE:
        # Use insertion sort for small subarrays
        return insertion_sort(arr)

    pivot = arr[0]
    lesser = []
    greater = []

    for element in arr[1:]:
        if element < pivot:
            lesser.append(element)
        else:
            greater.append(element)

    return quicksort_first_first(lesser) + [pivot] + quicksort_first_first(greater)


## Quicksort with a recursion threshold of 12 and with the pivot being the first element of the array
def quicksort_experimental_first(arr):
    if len(arr) <= THRESHOLD_EXPERIMENTAL_FIRST:
        # Use insertion sort for small subarrays
        return insertion_sort(arr)

    pivot = arr[0]
    lesser = []
    greater = []

    for element in arr[1:]:
        if element < pivot:
            lesser.append(element)
        else:
            greater.append(element)

    return quicksort_experimental_first(lesser) + [pivot] + quicksort_experimental_first(greater)


## Quicksort with a recursion threshold of 19 and with the pivot being generated randomly each time
def quicksort_experimental_random(arr):
    if len(arr) <= THRESHOLD_EXPERIMENTAL_RANDOM:
        # Use insertion sort for small subarrays
        return insertion_sort(arr)
    
    # Random index generated here
    random_index = random.randint(0, len(arr)-1)
    pivot = arr[random_index]
    lesser = []
    greater = []

    for idx, element in enumerate(arr):
        if idx == random_index:
            continue
        if element < pivot:
            lesser.append(element)
        else:
            greater.append(element)

    return quicksort_experimental_random(lesser) + [pivot] + quicksort_experimental_random(greater)


def counting_sort(original_array: list) -> list:
    max_element = max(original_array)
    count_array = [0] * (max_element + 1)
    for element in original_array:
        count_array[element] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    output = [0] * len(original_array)

    for element in original_array:
        correct_position = count_array[element] - 1
        output[correct_position] = element
        count_array[element] -= 1  # Decrease count of current element

    return output


if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm", required=True, type=str,
                        help="Représente l'algorithme à utiliser")
    parser.add_argument("-e", "--sample_path", required=True, type=str,
                        help="Représente le chemin de l'exemplaire à trier")
    parser.add_argument("-p", "--print", required=False, action='store_true',
                        help="Afficher les nombres triés en nombre croissant")
    parser.add_argument("-t", "--time", required=False, action='store_true',
                        help="Afficher le temps d'exécution en ms")
    
    args = parser.parse_args()

    with open(args.sample_path, 'r') as file:
        sample = [int(n) for n in file.read().split()]
    
    sorted_sample = []
    sys.setrecursionlimit(5000)

    start = time.time()
    match args.algorithm:
        case "counting":
            sorted_sample = counting_sort(sample)
        case "quick":
            sorted_sample = quicksort_first_first(sample)
        case "quickSeuil":
            sorted_sample = quicksort_experimental_first(sample)
        case "quickSeuilRandom":
            sorted_sample = quicksort_experimental_random(sample)
        case _:
            print("L'algorithme choisi n'existe pas")
            exit(1)

    end = time.time()
    execution_time = (end - start) * 1000
    
    if args.print:
        print(sorted_sample)
    
    if args.time:
        print(execution_time)
  