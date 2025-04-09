import random
import time

# Variabile pentru a număra comparațiile
comparisons = 0

def merge(arr, left, mid, right):
    global comparisons
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Indicele pentru primul subarray
    j = 0  # Indicele pentru al doilea subarray
    k = left  # Indicele pentru subarray-ul fuzionat

    while i < n1 and j < n2:
        comparisons += 1 
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Funcția de măsurare a performanței
def measure_performance(arr):
    global comparisons
    comparisons = 0

    # Începem măsurarea timpului
    start_time = time.perf_counter()

    # Apelăm funcția mergeSort
    merge_sort(arr, 0, len(arr) - 1)

    # Oprim măsurarea
    end_time = time.perf_counter()

    # Calculăm timpul total de execuție
    execution_time = end_time - start_time

    # Returnăm rezultatele
    return execution_time, comparisons

# Funcția pentru a afișa lista
def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    # Set de date random (240 de numere)
    random_data_240 = [random.randint(1, 1000) for _ in range(240)]

    # Set de date sortat (240 de numere)
    sorted_data_240 = sorted(random_data_240)

    # Set de date invers sortat (240 de numere)
    reverse_sorted_data_240 = sorted(random_data_240, reverse=True)

    random_data_400 = [random.randint(1, 1000) for _ in range(400)]



    print("Test pentru random_data_240:")
    execution_time, comparisons = measure_performance(random_data_240)
    print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}")

    print("\nTest pentru sorted_data_240:")
    execution_time, comparisons = measure_performance(sorted_data_240)
    print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}")

    print("\nTest pentru reverse_sorted_data_240:")
    execution_time, comparisons = measure_performance(reverse_sorted_data_240)
    print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}")

    print("\nTest pentru random_data_400:")
    execution_time, comparisons = measure_performance(random_data_400)
    print(f"Timp de execuție: {execution_time:.20f} secunde, Comparări: {comparisons}")

