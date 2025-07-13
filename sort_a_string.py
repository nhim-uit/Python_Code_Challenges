# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Sort a string

# my solution
def solve(s: str):
    s = s.split()
    return sorted(s, key=lambda x: x.lower()[0])


print(solve('mango ORANGE apple pearl corn'))
