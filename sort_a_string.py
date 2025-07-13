# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Sort a string

# my solution
def solve(s: str):
    s = s.split()
    return ' '.join(sorted(s, key=lambda x: x.lower()[0]))


# instructor's solution
def solve2(s):
    return ' '.join(sorted(s.split(), key=str.casefold))


print(solve2('mango ORANGE apple pearl corn'))
