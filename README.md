BREATH FIRST SEARCH


BFS(Graph, start):
    create a queue Q
    mark start as visited
    enqueue start into Q

    while Q is not empty:
        current = dequeue Q
        process current   // e.g., print or record it

        for each neighbor in Graph[current]:
            if neighbor is not visited:
                mark neighbor as visited
                enqueue neighbor into Q

DEPATH FIRST SEARCH 

DFS_iterative(graph, start):
    create an empty stack S
    create a set visited

    push start onto S

    while S is not empty:
        node = pop from S

        if node is not visited:
            mark node as visited
            process node

            for each neighbor in graph[node] in reverse order:
                push neighbor onto S

UNIFORM COST SEARCH 

UCS(start, goal):
    create a priority queue PQ
    PQ.insert(start, priority = 0)

    create a dictionary cost
    cost[start] = 0

    create a dictionary parent
    parent[start] = None

    while PQ is not empty:
        node = PQ.pop()    // node with smallest cost

        if node == goal:
            return reconstruct_path(parent, goal)

        for each (neighbor, edge_cost) in graph[node]:
            new_cost = cost[node] + edge_cost

            if neighbor not in cost OR new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = node
                PQ.insert(neighbor, priority = new_cost)

    return failure   // no path found
