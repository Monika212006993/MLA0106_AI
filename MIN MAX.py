import math

# Build full binary tree: 7 internal nodes + 8 leaf nodes
tree = [None]*7 + [2, 3, 5, 9, 0, 1, 7, 5]   # total = 15 nodes

def alphabeta(node, alpha, beta, maximizing):
    # If node is a leaf → return its value
    if node >= len(tree) or tree[node] is not None:
        return tree[node]

    left = node * 2 + 1
    right = node * 2 + 2

    if maximizing:
        best = -math.inf
        best = max(best, alphabeta(left, alpha, beta, False))
        alpha = max(alpha, best)

        if beta <= alpha:
            return best  # prune

        best = max(best, alphabeta(right, alpha, beta, False))
        return best

    else:
        best = math.inf
        best = min(best, alphabeta(left, alpha, beta, True))
        beta = min(beta, best)

        if beta <= alpha:
            return best  # prune

        best = min(best, alphabeta(right, alpha, beta, True))
        return best


# Run from root node index = 0
result = alphabeta(0, -math.inf, math.inf, True)
print("Best achievable score:", result)
