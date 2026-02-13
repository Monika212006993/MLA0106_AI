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
