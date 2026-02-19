from collections import deque

goal = "123456780"

def bfs(start):
    visited = {start: None}
    q = deque([start])

    while q:
        state = q.popleft()
        if state == goal:
            return visited

        i = state.index("0")
        moves = []
        if i not in [0,1,2]: moves.append(i-3)
        if i not in [6,7,8]: moves.append(i+3)
        if i not in [0,3,6]: moves.append(i-1)
        if i not in [2,5,8]: moves.append(i+1)

        for m in moves:
            s = list(state)
            s[i], s[m] = s[m], s[i]
            s = "".join(s)
            if s not in visited:
                visited[s] = state
                q.append(s)

start = "123405678"
path = bfs(start)

# Print solution path
state = goal
print("Solution Path:")
while state:
    print(state)
    state = path[state]
