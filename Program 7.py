import heapq
graph = {
    "A": {"B":5 ,"S": 3, "C":10 },
    "B": {"D":1  , "E":1, "C":2  },
    "C": {"G":4},
    "D": {"E":4},
    "E": {"G":3},
    "S": {"D":2},
}
h = {
    "A":9 ,
    "B": 4,
    "C": 2,
    "D": 5,
    "E": 3,
    "G": 0,
    "S": 7,
}
def astar(start, goal):
    pq = [(h[start], start)]
    g = {start: 0}
    parent = {}
    while pq:
        _, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            return [start] + path[::-1], g[goal]
        for nxt, cost in graph[node].items():
            new_g = g[node] + cost
            if nxt not in g or new_g < g[nxt]:
                g[nxt] = new_g
                parent[nxt] = node
                heapq.heappush(pq, (new_g + h[nxt], nxt))
    return None, float("inf")
path, cost = astar("A", "G")
print("Path:", path)
print("Cost:", cost)
