import argparse
import time


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

    start = time.time()
    match args.algorithm:
        case "counting":
            pass
            sorted_sample = counting_sort(sample)
        case "quick":
            pass
        case "quickSeuil":
            pass
        case "quickSeuilRandom":
            pass
        case _:
            print("L'algorithme choisi n'existe pas")
            exit(1)
            
    end = time.time()
    execution_time = (end - start) * 1000
    
    if args.print:
        print(sorted_sample)
    
    if args.time:
        print(execution_time)
  
