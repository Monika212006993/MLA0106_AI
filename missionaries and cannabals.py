from collections import deque

def is_valid(state):
    M_left, C_left, M_right, C_right, _ = state

    # Check for negative numbers
    if min(M_left, C_left, M_right, C_right) < 0:
        return False

    # If missionaries exist, they should not be outnumbered
    if (M_left > 0 and C_left > M_left) or (M_right > 0 and C_right > M_right):
        return False

    return True

def successors(state):
    M_left, C_left, M_right, C_right, boat = state
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]  # possible boat moves
    next_states = []

    for M, C in moves:
        if boat == 'left':
            new_state = (M_left - M, C_left - C,
                         M_right + M, C_right + C, 'right')
        else:
            new_state = (M_left + M, C_left + C,
                         M_right - M, C_right - C, 'left')

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def bfs(start, goal):
    q = deque([start])
    visited = {start: None}

    while q:
        state = q.popleft()
        if state == goal:
            break

        for next_state in successors(state):
            if next_state not in visited:
                visited[next_state] = state
                q.append(next_state)

    return visited

# Initial and goal states
start = (3, 3, 0, 0, 'left')
goal = (0, 0, 3, 3, 'right')

parent = bfs(start, goal)

# Print solution path
print("\nSolution Path:")
state = goal
path = []
while state:
    path.append(state)
    state = parent[state]

for s in reversed(path):
    print(s)
