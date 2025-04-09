import random
import time

# Variabile pentru a număra comparațiile și swapurile
comparisons = 0
swaps = 0

# Funcția de heapify (ajustare pentru heap)
def heapify(arr, n, i):
    global comparisons, swaps
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Verificăm dacă fiul din stânga este mai mare decât rădăcina
    comparisons += 1  # Comparăm
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificăm dacă fiul din dreapta este mai mare decât rădăcina
    comparisons += 1  # Comparăm
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Dacă cel mai mare element nu este rădăcina
    if largest != i:
        swap(arr, i, largest)  # Efectuăm swapul
        global swaps
        swaps += 1

        # Recursiv heapify pentru subarborele afectat
        heapify(arr, n, largest)

# Funcția de swap
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Funcția HeapSort
def heapSort(arr):
    global comparisons, swaps
    n = len(arr)

    # Construim heap-ul (rearanjăm elementele pentru a respecta proprietățile heap-ului)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extragem elementele unul câte unul din heap
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)  # Mutăm rădăcina la sfârșitul listei
        swaps += 1  # Swap între rădăcină și ultimul element
        heapify(arr, i, 0)  # Ajustăm heap-ul pentru a menține proprietățile sale

# Set de date random (240 de numere)
random_data_240 = [random.randint(1, 1000) for _ in range(240)]

# Set de date sortat (240 de numere)
sorted_data_240 = sorted(random_data_240)

# Set de date invers sortat (240 de numere)
reverse_sorted_data_240 = sorted(random_data_240, reverse=True)

# Set de date random (400 de numere)
random_data_400 = [random.randint(1, 1000) for _ in range(400)]

# Test pentru un set de date mic
test = [1, 9, 4, 7, 1, 10]

# Funcția care măsoară timpul, comparațiile și swapurile
def measure_performance(arr):
    global comparisons, swaps
    comparisons = 0
    swaps = 0

    n = len(arr)
    
    # Începem măsurarea timpului
    start_time = time.perf_counter()

    # Apelăm funcția heapSort
    heapSort(arr)

    # Oprim măsurarea
    end_time = time.perf_counter()

    # Calculăm timpul total de execuție
    execution_time = end_time - start_time

    # Returnăm rezultatele
    return execution_time, comparisons, swaps

# Testăm pentru fiecare set de date
print("Test pentru random_data_240:")
execution_time, comparisons, swaps = measure_performance(random_data_240)
print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}, Swapuri: {swaps}")

print("\nTest pentru sorted_data_240:")
execution_time, comparisons, swaps = measure_performance(sorted_data_240)
print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}, Swapuri: {swaps}")

print("\nTest pentru reverse_sorted_data_240:")
execution_time, comparisons, swaps = measure_performance(reverse_sorted_data_240)
print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}, Swapuri: {swaps}")

print("\nTest pentru random_data_400:")
execution_time, comparisons, swaps = measure_performance(random_data_400)
print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}, Swapuri: {swaps}")
