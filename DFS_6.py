def dfs(a, b, path, visited):
    if (a, b) == (2, 0):
        print(path)
        return True

    if (a, b) in visited:
        return False

    visited.add((a, b))

    moves = [
        (4, b),          # Fill jug A
        (a, 3),          # Fill jug B
        (0, b),          # Empty jug A
        (a, 0),          # Empty jug B
        (max(0, a-(3-b)), min(3, a+b)),  # Pour A to B
        (min(4, a+b), max(0, b-(4-a)))   # Pour B to A
    ]

    for x, y in moves:
        if dfs(x, y, path + [(x, y)], visited):
            return True

    return False


dfs(0, 0, [(0, 0)], set())
