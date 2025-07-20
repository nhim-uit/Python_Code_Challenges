# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Find all list items

# instructor's solution
def solve(ls, key):
    res = []

    for i in range(len(ls)):
        if ls[i] == key:
            res.append([i])
        elif isinstance(ls[i], list):
            for j in solve(ls[i], key):
                res.append([i] + j)
    return res


print(solve([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))