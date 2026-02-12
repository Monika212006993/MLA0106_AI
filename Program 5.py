import heapq

graph = {
    "S": {"A": 3, "D": 4},
    "A": {"B": 4, "D": 5},
    "B": {"C": 4, "E": 5},
    "C": {"B": 4},
    "D": {"E": 2},
    "E": {"F": 4},
    "F": {"G": 3.5}
}

h = {"S": 11.5, "A": 10.1, "B": 5.8, "C": 3.4, "D": 9.2, "E": 7.1, "F": 3.5, "G": 0}

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


path, cost = astar("S", "G")
print("Path:", path)
print("Cost:", cost)
