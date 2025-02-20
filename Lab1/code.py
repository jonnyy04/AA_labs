import time
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, Context, ROUND_HALF_EVEN
 

#1===========================================================

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

#2===========================================================

memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]

#3===========================================================

def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#4===========================================================

def matrix_mult(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

def power(F, n):
    if n == 1:
        return F
    if n % 2 == 0:
        half_power = power(F, n // 2)
        return matrix_mult(half_power, half_power)
    else:
        return matrix_mult(F, power(F, n - 1))

def fib_matrix(n):
    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]
    result = power(F, n - 1)
    return result[0][0]

#5===========================================================

def fib_binet(x):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    getcontext().prec = 60
    phi = Decimal((1 + Decimal(5).sqrt()) / 2)
    phi2 = Decimal((1 - Decimal(5).sqrt()) / 2)
    result = (ctx.power(phi, Decimal(x)) - ctx.power(phi2, Decimal(x))) / (Decimal(5).sqrt())
    return int(result)

#6===========================================================
def fib_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

#6===========================================================

def measure_time(func, n_values, repeats=30):
    times = []
    for n in n_values:
        elapsed_times = []
        for _ in range(repeats):
            start = time.perf_counter()
            func(n)
            end = time.perf_counter()
            elapsed_times.append(end - start)
        times.append(sum(elapsed_times) / repeats)
    return times

n_values_recursive = range(5, 30, 1)

n_values_memo = [
    5, 10, 15, 20, 25, 30, 35, 40,  
    50, 60, 70, 80, 90, 100,        
    200, 300, 400, 500, 600, 700, 1000]

n_values_other = [
    5, 10, 15, 20, 25, 30, 35, 40,  # Valori mici, dense
    50, 60, 70, 80, 90, 100,        # Creștere moderată
    200, 300, 400, 500, 600, 700,   # Creștere mai mare
    1000, 2000, 3000, 4000, 5000,   # Începem să testăm valori mari
    7500, 10000,12500, 15000,17500, 20000, 30000      # Valori rare pentru comportamentul final
]

times_recursive = measure_time(fib_recursive, n_values_recursive)
times_memo = measure_time(fib_memo, n_values_memo)
times_iterative = measure_time(fib_iterative, n_values_other)
times_matrix = measure_time(fib_matrix, n_values_other)
times_binet = measure_time(fib_binet, n_values_other)
times_dp = measure_time(fib_dp, n_values_other)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(n_values_recursive, times_recursive, marker='o', label="O(2^n)")
plt.ylabel("Time (s)")
plt.title("Recursivă simplă")
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(n_values_memo, times_memo, marker='o', label="O(n)")
plt.ylabel("Time (s)")
plt.title("Memoizare")
plt.legend()

plt.subplot(2, 3, 3)
plt.plot(n_values_other, times_iterative, marker='o', label="O(n)")
plt.ylabel("Time (s)")
plt.title("Iterativ")
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(n_values_other, times_matrix, marker='o', label="O(log n)")
plt.ylabel("Time (s)")
plt.title("Matrice 2x2")
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(n_values_other, times_binet, marker='o', label="O(1)")
plt.ylabel("Time (s)")
plt.title("Formula lui Binet")
plt.legend()

plt.subplot(2, 3, 6)
plt.plot(n_values_other, times_dp, marker='o', label="O(n)")
plt.ylabel("Time (s)")
plt.title("Programare Dinamică")
plt.legend()

plt.tight_layout()
plt.show()
