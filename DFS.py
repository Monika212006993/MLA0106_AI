# dfs_graph.py

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []

    visited.add(start)
    order.append(start)

    for nb in graph.get(start, []):
        if nb not in visited:
            dfs(graph, nb, visited, order)

    return order


if __name__ == "__main__":

    # -------------------------------
    # Graph 1 (Numbers, long chain)
    # -------------------------------
    g1 = {
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
    print("DFS graph 1:", dfs(g1, 1))

    # -------------------------------
    # Graph 2 (Numbers, another chain)
    # -------------------------------
    g2 = {
        1: [2],
        2: [3],
        3: [5],
        5: [6],
        6: [7],
        7: [4],
        4: [8],
        8: []
    }
    print("DFS graph 2:", dfs(g2, 1))

    # -------------------------------
    # Graph 3 (Letters A → G)
    # -------------------------------
    g3 = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": ["F"],
        "F": ["G"],
        "G": []
    }
    print("DFS graph 3:", dfs(g3, "A"))
