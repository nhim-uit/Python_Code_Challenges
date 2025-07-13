# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Identify a palindrome

# my solution
def solve(s):
    return s[::-1].lower().replace(' ', '') == s.lower().replace(' ', '')


print(solve('abba'))
print(solve('abcba'))
print(solve('d'))
print(solve('da'))
print(solve('race car')) # true