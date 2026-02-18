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


Min-Max

MINIMAX(node, depth, isMaximizingPlayer):

    if node is a terminal node OR depth == 0:
        return heuristic_value(node)

    if isMaximizingPlayer:
        bestValue = -∞
        for each child of node:
            value = MINIMAX(child, depth - 1, false)
            bestValue = max(bestValue, value)
        return bestValue

    else:   // Minimizing player
        bestValue = +∞
        for each child of node:
            value = MINIMAX(child, depth - 1, true)
            bestValue = min(bestValue, value)
        return bestValue

ALPHA BETA PRUNING 

ALPHA_BETA(node, depth, alpha, beta, isMax):

    if terminal(node) OR depth == 0:
        return heuristic(node)

    if isMax:
        value = -∞
        for child in children(node):
            value = max(value,
                        ALPHA_BETA(child, depth-1, alpha, beta, false))
            alpha = max(alpha, value)
            if alpha >= beta:
                break       // beta cut-off
        return value

    else:
        value = +∞
        for child in children(node):
            value = min(value,
                        ALPHA_BETA(child, depth-1, alpha, beta, true))
            beta = min(beta, value)
            if beta <= alpha:
                break       // alpha cut-off
        return value

WATER JUG PROBLEM 

WATER_JUG(A, B, G):

    start = (0, 0)
    create queue Q
    enqueue start into Q

    visited = empty set
    visited.add(start)

    parent = dictionary
    parent[start] = None

    while Q is not empty:
        (x, y) = dequeue Q

        // Goal check
        if x == G or y == G:
            return reconstruct_path(parent, (x, y))

        // Generate all possible next states
        for each (nx, ny) in NEXT_STATES(x, y, A, B):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                enqueue (nx, ny) into Q

    return failure

MAP COLOR

START
Define available colors (red, green, blue)
Assign colors to regions A, B, C, D
Check:
    A ≠ B
    A ≠ C
    B ≠ C
    C ≠ D
    B ≠ D
If all conditions satisfied
    Print color combination
STOP

FAMILY TREE PROBLEM

START
Define gender facts (male / female)
Define parent relationships

Mother(X,Y):
    If X is female AND parent of Y

Father(X,Y):
    If X is male AND parent of Y

Grandfather(X,Y):
    If X is male AND parent of Z
    AND Z is parent of Y

Grandmother(X,Y):
    If X is female AND parent of Z
    AND Z is parent of Y

Sister(X,Y):
    If X is female AND share same parent
    AND X ≠ Y

Brother(X,Y):
    If X is male AND share same parent
    AND X ≠ Y
STOP


STUDENT PERFORMANCE

START
Define student attributes

If student is hardworking AND regular
    Performance = Excellent

If student is hardworking AND irregular
    Performance = Good

If student has average trait
    Performance = Average

Display performance
STOP


BIRD FLY PROBLEM

START
Define birds (eagle, sparrow, penguin)

If bird is penguin
    Fail (cannot fly)

Else if bird exists
    Bird can fly

Display result
STOP


FORWARD CHAINING

START
If person is American
AND sells weapon
AND weapon sold to hostile country
Then
    Person is criminal

Check for Robert
Display result
STOP


PLANETS DATABASE

START
Store orbit relationships

If X orbits sun
    X is planet

If Moon orbits Planet
    Moon_of(Moon, Planet)

Display results
STOP

FRUIT AND COLOR PREDICTION

START
Define fruit-color facts

If fruit has defined color
    Return that color

Else
    Return unknown

Allow backtracking for multiple colors
STOP


FAMILY RELATION

START
Define male and female members
Define parent relationships

Define:
    Father
    Mother
    Brother
    Sister
    Grandfather
    Grandmother

Based on parent + gender conditions
Return relationships
STOP


COUNT NUMBER OF VOWLES

START
Store sentence

Convert sentence into characters

For each character in sentence
    If character is vowel
        Increase counter by 1

Display total vowel count
STOP









