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
