import itertools

# Distance matrix between cities
#    A  B  C  D
dist = [
    [0, 10, 15, 20],   # A
    [10, 0, 35, 25],   # B
    [15, 35, 0, 30],   # C
    [20, 25, 30, 0]    # D
]

cities = [0, 1, 2, 3]  # Represent A, B, C, D

min_cost = float('inf')
best_path = None

for perm in itertools.permutations(cities):
    cost = 0
    for i in range(len(perm)-1):
        cost += dist[perm[i]][perm[i+1]]
    cost += dist[perm[-1]][perm[0]]   # return to start

    if cost < min_cost:
        min_cost = cost
        best_path = perm

print("Best Path:", best_path)
print("Minimum Cost:", min_cost)
