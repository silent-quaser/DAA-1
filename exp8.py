from itertools import permutations

INF = float('inf')


# ---------------- Matrix Reduction (Optional) ----------------
def reduce_matrix(mat):
    """
    Reduce matrix and return reduction cost.
    (Used in Branch and Bound implementations)
    """
    n = len(mat)
    m = [row[:] for row in mat]
    reduction_cost = 0

    # Row Reduction
    for i in range(n):
        row_min = min(m[i])

        if row_min != INF and row_min > 0:
            reduction_cost += row_min

            for j in range(n):
                if m[i][j] != INF:
                    m[i][j] -= row_min

    # Column Reduction
    for j in range(n):
        col_min = min(m[i][j] for i in range(n))

        if col_min != INF and col_min > 0:
            reduction_cost += col_min

            for i in range(n):
                if m[i][j] != INF:
                    m[i][j] -= col_min

    return m, reduction_cost


# ---------------- Brute Force TSP ----------------
def tsp_brute_force(cost, n):

    cities = list(range(1, n))

    best_cost = INF
    best_path = None

    for perm in permutations(cities):

        path = [0] + list(perm) + [0]

        total_cost = 0

        for i in range(n):
            total_cost += cost[path[i]][path[i + 1]]

        if total_cost < best_cost:
            best_cost = total_cost
            best_path = path

    return best_path, best_cost


# ---------------- Main ----------------
def main():

    cost = [
        [INF, 10, 8, 9, 7],
        [10, INF, 10, 5, 6],
        [8, 10, INF, 8, 9],
        [9, 5, 8, INF, 6],
        [7, 6, 9, 6, INF]
    ]

    cities = ["A", "B", "C", "D", "E"]
    n = len(cost)

    best_path, best_cost = tsp_brute_force(cost, n)

    print("5-City TSP - Cost Matrix\n")

    print(f"{'':>4}", end="")
    for city in cities:
        print(f"{city:>6}", end="")
    print()

    for i in range(n):
        print(f"{cities[i]:>4}", end="")

        for value in cost[i]:
            if value == INF:
                print(f"{'INF':>6}", end="")
            else:
                print(f"{value:>6}", end="")

        print()

    print("\nOptimal Tour:")
    print(" -> ".join(cities[i] for i in best_path))

    print(f"\nMinimum Cost: {best_cost}")

    print("\nPath Verification:")

    for i in range(n):
        u = best_path[i]
        v = best_path[i + 1]

        print(f"{cities[u]} -> {cities[v]} : Cost = {cost[u][v]}")


if __name__ == "__main__":
    main()