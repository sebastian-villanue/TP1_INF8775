import matplotlib.pyplot as plt
from time import time
import algorithms
import constants
import random

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
        #Pivot choisi de manière aléatoire à chaque fois && Modification faite au code de ChatGPT
        index = random.randint(0, len(arr) - 1)
        #----------------------------------------------------------------------------------------
        pivot = arr[index]
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


# import algorithms
# import constants
# import time
# import timeit
# import random
# import matplotlib.pyplot as plt

# ##------------------------------------------------------------------------------------------------
# ## Function to calculate the time of execution
# # test_indexes = {}

# times = {}
# def initialize_dictionary():
#     for threshold in constants.TEST_THRESHOLDS:
#         times[f'{threshold}'] = 0

# def calculate_mean_time():
#     for key in times:
#         times[key] = times[key]/1000

# def calculate_time(array: list):
#     for threshold in constants.TEST_THRESHOLDS :
#         start_time = time.time()
#         quicksort(array, 0, len(array)-1, threshold)
#         end_time = time.time()
#         times[f'{threshold}'] += end_time - start_time

# def determine_best_threshold_and_index(array: list) -> str:
#     # calculate_time(array)
#     for key in times.keys():
#         if times[key] == min(times.values()):
#             return key
# ##------------------------------------------------------------------------------------------------

# ##------------------------------------------------------------------------------------------------
# ## Quicksort with the recursion threshold given as a parameter and with the pivot being the first element of the array
# ## used to experimentally determine the best value for the threshold
# # def quicksort(arr: list, low: int, high: int, threshold: int):
# #     if low + threshold <= high:
# #         pivot_index = partition(arr, low, high)
# #         quicksort(arr, low, pivot_index - 1, threshold)
# #         quicksort(arr, pivot_index + 1, high, threshold)
# #     else:
# #         insertion_sort(arr)


# # def partition(arr: list, low: int, high: int) -> int:  # 0, 2 [1, 2, 3]
#     # index = random.randint(low, high)
#     # print("index is")
# #     # print(index)
# #     pivot = arr[index]
# #     k = high
# #     for i in range(high, low, -1):
# #         # move elements that are greater than the pivot at the right-hand side
# #         if arr[i] > pivot:
# #             arr[i], arr[k] = arr[k], arr[i]
# #             k -= 1
# #     arr[k], arr[low] = arr[low], arr[k]  # place the pivot at its correct position
# #     return k  # pivot index

# # # # # def insertionSort(a, left, right):

# # # # #     for p in range(left+1, right):

# # # # #         j = p
# # # # #         tmp = a[p]

# # # # #         while(j > left and tmp < a[j-1]):
# # # # #             a[j] = a[j-1]
# # # # #             j-=1

# # # # #         a[j] = tmp


# # # # # def quicksort_general(original_array, threshold):
# # # # #     quicksort(original_array, 0, len(original_array)-1, threshold)
    

# # # # # def quicksort(a, left, right, threshold):

# # # # #     if(left + threshold <= right):
# # # # #         index = random.randint(left, right)
# # # # #         pivot = a[index]
# # # # #         i = left
# # # # #         j = right+1

# # # # #         while(True):
# # # # #             while(True):
# # # # #                 if(i+1 <= right):
# # # # #                     i+=1
# # # # #                 else:
# # # # #                     break
# # # # #                 if(a[i] < pivot):
# # # # #                     continue
# # # # #                 else:
# # # # #                     break
# # # # #             while(True):
# # # # #                 if(j-1 >= left):
# # # # #                     j-=1
# # # # #                 else:
# # # # #                     break
# # # # #                 if(a[j] > pivot):
# # # # #                     continue
# # # # #                 else:
# # # # #                     break

# # # # #             if (i < j):
# # # # #                 a[i], a[j] = a[j], a[i]
# # # # #             else:
# # # # #                 break

# # # # #         a[j], a[left] = a[left], a[j]

# # # # #         quicksort(a, left, j-1, threshold)
# # # # #         quicksort(a, j+1, right, threshold)

# # # # #     else:
# # # # #         insertionSort(a, left, right+1)


# def insertion_sort(arr: list):
#     j = 0
#     for p in range(1, len(arr)):
#         temp = arr[p]
#         j = p
#         while j > 0 and temp < arr[j - 1]:
#             arr[j] = arr[j - 1]
#             j -= 1
#         arr[j] = temp
# ##------------------------------------------------------------------------------------------------


# ##------------------------------------------------------------------------------------------------
# ## Quicksort with a recursion threshold of 1 and with the pivot being the first element of the array
# def quicksort(arr: list, low: int, high: int):
#     if low + constants.THRESHOLD_ONE < high:
#         pivot_index = partition_first(arr, low, high)
#         quicksort(arr, low, pivot_index - 1)
#         quicksort(arr, pivot_index + 1, high)
#     else:
#         insertion_sort(arr)


# def partition_first(arr: list, low: int, high: int) -> int:  # 0, 2 [1, 2, 3]
#     pivot = arr[low]
#     k = high
#     for i in range(high, low, -1):
#         # move elements that are greater than the pivot at the right-hand side
#         if arr[i] > pivot:
#             arr[i], arr[k] = arr[k], arr[i]
#             k -= 1
#     arr[k], arr[low] = arr[low], arr[k]  # place the pivot at its correct position
#     return k  # pivot index

# # CUTOFF=1


# # def insertionSort(a, left, right):

# #     for p in range(left+1, right):

# #         j = p
# #         tmp = a[p]

# #         while(j > left and tmp < a[j-1]):
# #             a[j] = a[j-1]
# #             j-=1

# #         a[j] = tmp


# # def quicksort_general(original_array, test):
# #     quicksort(original_array, 0, len(original_array)-1, test)
    

# # def quicksort(a, left, right, test):

# #     if(left + test <= right):

# #         pivot = a[left]
# #         i = left
# #         j = right+1

# #         while(True):
# #             while(True):
# #                 if(i+1 <= right):
# #                     i+=1
# #                 else:
# #                     break
# #                 if(a[i] < pivot):
# #                     continue
# #                 else:
# #                     break
# #             while(True):
# #                 if(j-1 >= left):
# #                     j-=1
# #                 else:
# #                     break
# #                 if(a[j] > pivot):
# #                     continue
# #                 else:
# #                     break

# #             if (i < j):
# #                 a[i], a[j] = a[j], a[i]
# #             else:
# #                 break

# #         a[j], a[left] = a[left], a[j]
# #         quicksort(a, left, j-1, test)
# #         quicksort(a, j+1, right, test)

# #     else:
# #         insertionSort(a, left, right+1)
# ##------------------------------------------------------------------------------------------------

# ##------------------------------------------------------------------------------------------------
# ## Insertion Sort used in the quicksort algorithm
# # def insertion_sort(arr: list):
# #     j = 0
# #     for p in range(1, len(arr)):
# #         temp = arr[p]
# #         j = p
# #         while j > 0 and temp < arr[j - 1]:
# #             arr[j] = arr[j - 1]
# #             j -= 1
# #         arr[j] = temp
# ##------------------------------------------------------------------------------------------------
# if __name__ == '__main__':
#     algorithms.access_files()
#     array = [int(element) for element in algorithms.samples[0].split()]
#     # print(array)
#     quicksort(array, 0, len(array)-1)
#     print(array == sorted(array))
#     # initialize_dictionary()
#     # for i in range(1) :
#     #     calculate_time(array)
#     # calculate_mean_time()
#     # # print(array)
#     # # quicksort(array, 0, len(array)-1, 1)
#     # # calculate_mean_time()
#     # print(times)
#     # # print(array)


        
#     # print(determine_best_threshold_and_index(array))
#     # print("best threshold is up there")

#     # # Create a figure and axis
#     # fig, ax = plt.subplots()

#     # # Plot the data
#     # ax.plot(times.keys(), times.values())

#     # # Add labels and a title
#     # ax.set_xlabel('X-axis')
#     # ax.set_ylabel('Y-axis')
    
#     # # Display the plot
#     # plt.show()


#     # print("sorted")
#     # print(sorted(array))
#     # print("array avant quicksort")
#     # arr = [int(element) for element in algorithms.samples[0].split()]
#     # print(arr)
#     # quicksort_general(arr, 1)
#     # print("arr after quicksort")
#     # print(arr)