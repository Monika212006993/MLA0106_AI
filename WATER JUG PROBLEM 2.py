from collections import deque

# capacities
X, Y = 5, 3
goal = 4

def water_jug():
    visited = set()
    q = deque([ (0,0) ])   # (jug5, jug3)

    while q:
        x, y = q.popleft()
        if (x, y) in visited: 
            continue
        visited.add((x, y))

        print((x, y))

        if x == goal or y == goal:
            print("Goal reached:", (x, y))
            return

        # All possible moves
        next_states = [
            (X, y),      # fill 5-L
            (x, Y),      # fill 3-L
            (0, y),      # empty 5-L
            (x, 0),      # empty 3-L
            (x - min(x, Y - y), y + min(x, Y - y)),  # pour 5→3
            (x + min(y, X - x), y - min(y, X - x))   # pour 3→5
        ]
        q.extend(next_states)

water_jug()
