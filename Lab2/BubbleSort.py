import random
import time

# Variabile pentru măsurarea numărului de comparații și swapuri
comparisons = 0
swaps = 0

# Funcția de schimbare (swap)
def swap(arr, i, j):
    global swaps  
    arr[i], arr[j] = arr[j], arr[i]
    swaps += 1  

# Funcția Bubble Sort
def bubbleSort(arr):
    global comparisons, swaps
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

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
    
    # Apelăm funcția BubbleSort
    bubbleSort(data)
    
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    
    print(f"Set de date: {name}")
    print(f"Timp de execuție: {execution_time:.6f} secunde")
    print(f"Număr de comparații: {comparisons}")
    print(f"Număr de swapuri: {swaps}")
    print("-" * 40)
