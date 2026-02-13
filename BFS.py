# bfs_graph.py
from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        v = q.popleft()
        order.append(v)
        for nb in graph.get(v, []):
            if nb not in visited:
                visited.add(nb)
                q.append(nb)

    return order


if __name__ == "__main__":
    
    # -------------------------------
    # Example 1: Graph with letters
    # -------------------------------
    g1 = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": ["F"],
        "F": ["G"],
        "G": []
    }
    print("BFS (letter graph):", bfs(g1, "A"))

    # -------------------------------
    # Example 2: Your second graph
    # -------------------------------
    g2 = {
        1: [2],
        2: [7],
        7: [3],
        3: [6],
        6: [8],
        8: [10],
        10: [4],
        4: [5],
        5: [9],
        9: []
    }
    print("BFS (number graph 1):", bfs(g2, 1))

    # -------------------------------
    # Example 3: Your third graph
    # -------------------------------
    g3 = {
        1: [2],
        2: [3],
        3: [5],
        5: [6],
        6: [7],
        7: [4],
        4: [8],
        8: []
    }
    print("BFS (number graph 2):", bfs(g3, 1))
