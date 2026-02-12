import heapq
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 3},
    "C": {"E": 5},
    "D": {"F": 2, "G": 4},
    "E": {"G": 3},
    "F": {"G": 1},
    "G": {}
}
h = {
    "A": 5,
    "B": 6,
    "C": 4,
    "D": 3,
    "E": 3,
    "F": 1,
    "G": 0
}
def astar(start, goal):
    open = [(h[start], start)]
    g = {start: 0}
    parent = {}

    while open:
        _, node = heapq.heappop(open)
        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            return [start] + path[::-1], g[goal]

        for n, cost in graph[node].items():
            new_g = g[node] + cost
            if n not in g or new_g < g[n]:
                g[n] = new_g
                parent[n] = node
                heapq.heappush(open, (new_g + h[n], n))

    return None, float("inf")

path, cost = astar("A", "G")
print("Path:", path)
print("Cost:", cost)
