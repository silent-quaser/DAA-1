import random

# Global comparison counter
comparison_count = 0


# ---------------- Divide and Conquer ----------------
def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine results
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


# ---------------- Naive Method ----------------
def min_max_naive(arr):
    minimum = arr[0]
    maximum = arr[0]
    comparisons = 0

    for x in arr[1:]:

        comparisons += 1
        if x < minimum:
            minimum = x

        comparisons += 1
        if x > maximum:
            maximum = x

    return minimum, maximum, comparisons


# ---------------- Main ----------------
def main():
    global comparison_count

    # Example array
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    comparison_count = 0

    minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
    dc_comparisons = comparison_count

    _, _, naive_comparisons = min_max_naive(arr)

    print("Array:", arr)
    print(f"Minimum Value : {minimum}")
    print(f"Maximum Value : {maximum}")
    print(f"Divide & Conquer Comparisons : {dc_comparisons}")
    print(f"Naive Comparisons            : {naive_comparisons}")

    # Performance Analysis
    print("\nPerformance Analysis")
    print("-" * 60)
    print(f"{'Size':>8} {'DC Comps':>12} {'Naive Comps':>15} {'Formula(3n/2-2)':>18}")
    print("-" * 60)

    for size in [10, 100, 1000, 10000]:

        arr = [random.randint(1, 10000) for _ in range(size)]

        comparison_count = 0

        minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = (3 * size) // 2 - 2

        print(f"{size:>8} {dc:>12} {naive:>15} {formula:>18}")


if __name__ == "__main__":
    main()