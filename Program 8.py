from collections import deque

cap = (3, 8, 5)
start = (3, 8, 0)
goal = 4

q = deque([start])
vis = {start}

def pour(a,b,ca,cb):
    t = min(a, cb - b)
    return a - t, b + t

while q:
    x, y, z = q.popleft()
    print(x, y, z)
    if goal in (x, y, z):
        print("Goal:", (x, y, z))
        break

    # fill + empty
    moves = [
        (cap[0], y, z), (x, cap[1], z), (x, y, cap[2]),
        (0, y, z), (x, 0, z), (x, y, 0)
    ]

    # pour between jugs
    # X→Y, X→Z
    a,b = pour(x,y,cap[0],cap[1]); moves.append((a,b,z))
    a,b = pour(x,z,cap[0],cap[2]); moves.append((a,y,b))

    # Y→X, Y→Z
    a,b = pour(y,x,cap[1],cap[0]); moves.append((b,a,z))
    a,b = pour(y,z,cap[1],cap[2]); moves.append((x,b,a))

    # Z→X, Z→Y
    a,b = pour(z,x,cap[2],cap[0]); moves.append((b,y,a))
    a,b = pour(z,y,cap[2],cap[1]); moves.append((x,b,a))

    for m in moves:
        if m not in vis:
            vis.add(m)
            q.append(m)
