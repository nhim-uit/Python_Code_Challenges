# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Identify a palindrome

# my solution
def alpha(s):
    return ''.join([i for i in s if i.isalpha()])


def solve(s):
    return alpha(s[::-1]).lower() == alpha(s).lower()


print(solve('abba'))
print(solve('abcba'))
print(solve('d'))
print(solve('da'))
print(solve('race car')) # true
print(solve('Go hang a salami - I\'m a lasagna hog.')) # true