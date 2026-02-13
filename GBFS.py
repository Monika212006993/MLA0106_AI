from queue import PriorityQueue

# ---------------------------
# GRAPH 1 (first big diagram)
# ---------------------------
graph1 = {
    'P': ['A','C','R'],
    'A': ['M'],
    'C': ['M','U','R'],
    'R': ['E'],
    'E': ['S'],
    'M': ['L','U'],
    'L': ['N'],
    'U': ['N','S'],
    'N': ['S'],
    'S': []
}

heuristic1 = {
    'P':7,'A':6,'C':5,'R':4,'E':3,
    'M':5,'L':4,'U':3,'N':2,'S':0
}

# ---------------------------
# GRAPH 2 (second diagram)
# ---------------------------
graph2 = {
    'P': ['A','C','R'],
    'A': [],
    'R': [],
    'C': ['M','U'],
    'M': [],
    'U': ['N','S'],
    'N': [],
    'S': []
}

heuristic2 = {
    'P':7,'A':6,'C':5,'R':6,'M':4,'U':3,'N':2,'S':0
}

# ---------------------------
# GBFS ALGORITHM
# ---------------------------
def gbfs(graph, h, start, goal):
    pq = PriorityQueue()
    pq.put((h[start], start))
    visited = set()
    parent = {start: None}

    while not pq.empty():
        _, node = pq.get()
        print("Expanding:", node)

        if node == goal:
            print("Goal reached!")
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        visited.add(node)
        for nbr in graph[node]:
            if nbr not in visited:
                parent[nbr] = node
                pq.put((h[nbr], nbr))

    return None


# ---------------------------
# RUN BOTH EXAM CASES
# ---------------------------
print("\n===== GRAPH 1 (Exam Question 1) =====")
path1 = gbfs(graph1, heuristic1, 'P', 'S')
print("Path:", path1)

print("\n===== GRAPH 2 (Exam Question 2) =====")
path2 = gbfs(graph2, heuristic2, 'P', 'S')
print("Path:", path2)
