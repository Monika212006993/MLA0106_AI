from collections import deque

cap = (12, 8, 5)
start = (12, 0, 0)
goal = 6

q = deque([start])
vis = {start}

while q:
    x, y, z = q.popleft()
    print(x, y, z)
    if goal in (x, y, z):
        print("Goal:", (x, y, z))
        break

    for a, b, c in [
        (cap[0], y, z), (x, cap[1], z), (x, y, cap[2]),   # fill
        (0, y, z), (x, 0, z), (x, y, 0)                    # empty
    ]:
        if (a, b, c) not in vis:
            vis.add((a, b, c))
            q.append((a, b, c))

    # pour operations
    for (X,Y,Z),(i,j,k) in [
        ((x,y,z),(0,1,1)), # x→y, x→z
        ((y,x,z),(1,0,1)), # y→x, y→z
        ((z,x,y),(1,1,0))  # z→x, z→y
    ]:
        for to_cap, idx in [(cap[j], j), (cap[k], k)]:
            if idx == j: t = min(X, to_cap - Y)
            else:        t = min(X, to_cap - Z)
            nx, ny, nz = x, y, z
            if idx == j: nx, ny = X - t, Y + t
            else:        nx, nz = X - t, Z + t
            if (nx, ny, nz) not in vis:
                vis.add((nx, ny, nz))
                q.append((nx, ny, nz))
