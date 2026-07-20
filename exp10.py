import random
import time
import sys

# Increase recursion limit
sys.setrecursionlimit(20000)

# Global comparison counter
comparisons = 0


# ---------------- Partition Function ----------------
def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# ---------------- Deterministic Quick Sort ----------------
def deterministic_quicksort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# ---------------- Randomized Quick Sort ----------------
def randomized_quicksort(arr, low, high):

    if low < high:

        # Select random pivot
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# ---------------- Run Performance Test ----------------
def run_test(sort_function, arr):
    global comparisons

    data = arr.copy()

    comparisons = 0

    start = time.perf_counter()

    sort_function(data, 0, len(data) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


# ---------------- Main ----------------
def main():

    N = 5000

    test_cases = {
        "Random": [random.randint(1, 100000) for _ in range(N)],
        "Sorted": list(range(N)),
        "Reverse": list(range(N, 0, -1)),
        "Nearly Sorted": list(range(N))
    }

    # Slightly shuffle the Nearly Sorted array
    nearly_sorted = test_cases["Nearly Sorted"]

    for _ in range(N // 20):
        i = random.randint(0, N - 1)
        j = random.randint(0, N - 1)

        nearly_sorted[i], nearly_sorted[j] = nearly_sorted[j], nearly_sorted[i]

    # Table Header
    print(
        f"{'Input Type':<16}"
        f"{'DQS Comps':>15}"
        f"{'DQS Time(ms)':>18}"
        f"{'RQS Comps':>15}"
        f"{'RQS Time(ms)':>18}"
    )

    print("-" * 82)

    # Run Tests
    for case, arr in test_cases.items():

        d_comp, d_time = run_test(deterministic_quicksort, arr)
        r_comp, r_time = run_test(randomized_quicksort, arr)

        print(
            f"{case:<16}"
            f"{d_comp:>15}"
            f"{d_time:>18.2f}"
            f"{r_comp:>15}"
            f"{r_time:>18.2f}"
        )


if __name__ == "__main__":
    main()