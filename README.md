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

GREEDY BREATH FIRST SEARCH

GBFS(start, goal):

    openSet = priority queue ordered by h(n)
    openSet.insert(start, priority = h(start))

    parent = dictionary
    parent[start] = None

    visited = empty set

    while openSet is not empty:

        current = openSet.pop()   // node with smallest h(n)

        if current == goal:
            return reconstruct_path(parent, goal)

        visited.add(current)

        for each neighbor in graph[current]:
            if neighbor not in visited:
                parent[neighbor] = current
                openSet.insert(neighbor, priority = h(neighbor))

    return failure

A*

A*(start, goal):

    openSet = priority queue ordered by f(n) = g(n) + h(n)
    openSet.insert(start, priority = h(start))

    g = dictionary with default = ∞
    g[start] = 0

    parent = dictionary
    parent[start] = None

    while openSet is not empty:

        current = openSet.pop()   // node with smallest f(n)

        if current == goal:
            return reconstruct_path(parent, goal)

        for each (neighbor, cost) in graph[current]:
            tentative_g = g[current] + cost

            if tentative_g < g[neighbor]:
                parent[neighbor] = current
                g[neighbor] = tentative_g
                f = tentative_g + h(neighbor)
                openSet.insert(neighbor, priority = f)

    return failure   // no path
