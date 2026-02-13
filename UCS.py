import heapq

def ucs(graph, start, goal):
    pq = [(0, start)]       # (cost, node)
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor))

    return None


# --------------------------------------------------
# Test Input 1
# --------------------------------------------------
graph1 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 7)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

print("Test 1 UCS Cost:", ucs(graph1, 'A', 'E'))


# --------------------------------------------------
# Test Input 2
# --------------------------------------------------
graph2 = {
    'A': [('B', 2)],
    'B': [('C', 3)],
    'C': []
}

print("Test 2 UCS Cost:", ucs(graph2, 'A', 'C'))


# --------------------------------------------------
# Test Input 3
# --------------------------------------------------
graph3 = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 1)],
    'C': [('D', 10)],
    'D': []
}

print("Test 3 UCS Cost:", ucs(graph3, 'A', 'D'))


# --------------------------------------------------
# Test Input 4
# --------------------------------------------------
graph4 = {
    '1': [('2', 4), ('3', 2)],
    '2': [('4', 7)],
    '3': [('4', 1), ('5', 3)],
    '4': [('6', 2)],
    '5': [('6', 8)],
    '6': []
}

print("Test 4 UCS Cost:", ucs(graph4, '1', '6'))
