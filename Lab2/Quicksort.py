import random
import time

# Variabile pentru măsurarea numărului de comparații și swapuri
comparisons = 0
swaps = 0

# Funcția de partajare (partition)
def partition(arr, low, high):
    global comparisons, swaps 
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1  
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    global swaps  
    arr[i], arr[j] = arr[j], arr[i]
    swaps += 1  

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


random_data_240 = [random.randint(1, 1000) for _ in range(240)]

# Set de date sortat (240 de numere)
sorted_data_240 = sorted(random_data_240)

# Set de date invers sortat (240 de numere)
reverse_sorted_data_240 = sorted(random_data_240, reverse=True)

# Set de date random (400 de numere)
random_data_400 = [random.randint(1, 1000) for _ in range(400)]

# Listă cu seturile de date de testat
data_sets = [
    ("Random Data 240", random_data_240),
    ("Sorted Data 240", sorted_data_240),
    ("Reverse Sorted Data 240", reverse_sorted_data_240),
    ("Random Data 400", random_data_400)
]

# Rulăm analiza pentru fiecare set de date
for name, data in data_sets:
    comparisons = 0  # Resetăm contorii
    swaps = 0
    start_time = time.perf_counter()
    
    # Apelăm funcția QuickSort
    quickSort(data, 0, len(data) - 1)
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    print(f"Set de date: {name}")
    print(f"Timp de execuție: {execution_time:.6f} secunde")
    print(f"Număr de comparații: {comparisons}")
    print(f"Număr de swapuri: {swaps}")
    print("-" * 40)
