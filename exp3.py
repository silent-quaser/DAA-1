import heapq


# ---------------- Union-Find Class ----------------
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        self.parent[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        return True


# ---------------- Kruskal's Algorithm ----------------
def kruskal(n, edges):
    edges = sorted(edges)

    uf = UnionFind(n)

    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == n - 1:
                break

    return mst, total_cost


# ---------------- Prim's Algorithm ----------------
def prim(n, adj, start=0):
    visited = [False] * n
    pq = [(0, start, -1)]      # (weight, vertex, parent)

    mst = []
    total_cost = 0

    while pq:
        weight, u, parent = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True

        if parent != -1:
            mst.append((parent, u, weight))
            total_cost += weight

        for v, wt in adj.get(u, []):
            if not visited[v]:
                heapq.heappush(pq, (wt, v, u))

    return mst, total_cost


# ---------------- Main Program ----------------
def main():

    n = 7

    edges = [
        (7, 0, 1),
        (5, 0, 3),
        (8, 1, 2),
        (9, 1, 3),
        (7, 1, 4),
        (5, 2, 4),
        (15, 3, 4),
        (6, 3, 5),
        (8, 4, 5),
        (9, 4, 6),
        (11, 5, 6)
    ]

    # Build adjacency list
    adj = {}

    for weight, u, v in edges:
        adj.setdefault(u, []).append((v, weight))
        adj.setdefault(v, []).append((u, weight))

    # Run algorithms
    kruskal_mst, kruskal_cost = kruskal(n, edges)
    prim_mst, prim_cost = prim(n, adj)

    # Display Kruskal Result
    print("=== Kruskal's MST ===")
    for u, v, w in kruskal_mst:
        print(f"Edge ({u} - {v}) Weight: {w}")

    print(f"Total MST Cost: {kruskal_cost}")

    # Display Prim Result
    print("\n=== Prim's MST ===")
    for u, v, w in prim_mst:
        print(f"Edge ({u} - {v}) Weight: {w}")

    print(f"Total MST Cost: {prim_cost}")


if __name__ == "__main__":
    main()