import parameters
import constants
import random

##------------------------------------------------------------------------------------------------
## Initialization of the samples array
samples = []
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## Function to access all the samples and put them in an array
def access_files():
    for i in range(0, parameters.nb_samples):
        file_name = f'samples/sample_{parameters.array_size}_{parameters.magnitude}_{i+1}.txt'
        with open(file_name, 'r') as file:
            samples.append(file.read())
            file.close()
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## Counting sort
def counting_sort(original_array: list, size: int) -> list:
    max_element = max(original_array)
    count_array = [0] * (max_element + 1)
    for element in original_array:
        count_array[element] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    output = [0] * size

    for element in original_array:
        correct_position = count_array[element] - 1
        output[correct_position] = element
        count_array[element] -= 1  # Decrease count of current element

    return output
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## Insertion Sort used in the quicksort algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## Quicksort with a recursion threshold of 1 and with the pivot being the first element of the array
def quicksort_first_first(arr):
    if len(arr) <= constants.THRESHOLD_ONE:
        insertion_sort(arr)
        return arr

    if len(arr) > 1:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort_first_first(left, constants.THRESHOLD_ONE) + middle + quicksort_first_first(right, constants.THRESHOLD_ONE)
    else:
        return arr
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## A REFAIRE IMBECILE
## Quicksort with a recursion threshold of 22 and with the pivot being the first element of the array
def quicksort_experimental_first(arr):
    if len(arr) <= constants.THRESHOLD_EXPERIMENTAL_FIRST:
        insertion_sort(arr)
        return arr

    if len(arr) > 1:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort_experimental_first(left, constants.THRESHOLD_EXPERIMENTAL_FIRST) + middle + quicksort_experimental_first(right, constants.THRESHOLD_EXPERIMENTAL_FIRST)
    else:
        return arr
##------------------------------------------------------------------------------------------------

##------------------------------------------------------------------------------------------------
## Quicksort with a recursion threshold of 42 and with the pivot being chosen randomly every time
def quicksort_experimental_random(arr):
    if len(arr) <= constants.THRESHOLD_EXPERIMENTAL_EXPERIMENTAL:
        insertion_sort(arr)
        return arr

    if len(arr) > 1:
        #Pivot choisi de manière aléatoire à chaque fois && Modification faite au code de ChatGPT
        index = random.randint(0, len(arr) - 1)
        #----------------------------------------------------------------------------------------
        pivot = arr[index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort_experimental_random(left, constants.THRESHOLD_EXPERIMENTAL_EXPERIMENTAL) + middle + quicksort_experimental_random(right, constants.THRESHOLD_EXPERIMENTAL_EXPERIMENTAL)
    else:
        return arr
##------------------------------------------------------------------------------------------------