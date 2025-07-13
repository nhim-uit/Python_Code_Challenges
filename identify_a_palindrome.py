# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Identify a palindrome

import re


# my solution
def alpha(s):
    return ''.join([i for i in s if i.isalpha()])


def solve(s):
    return alpha(s[::-1]).lower() == alpha(s).lower()


# instructor's solution
def solve2(s):
    forwards = ''.join(re.findall(r'[a-z]+', s.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


print(solve('abba'))
print(solve('abcba'))
print(solve('d'))
print(solve2('da'))
print(solve2('race car')) # true
print(solve2('Go hang a salami - I\'m a lasagna hog.')) # true