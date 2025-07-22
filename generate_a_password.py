# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# generate a password
import random

FILE = 'diceware.wordlist.txt'


def create_dict():
    d = {}

    with open(FILE, 'r') as file:
        for line in file:
            word = line.split()
            d[word[0]] = word[1]
    return d


def generate(n):
    res = ''
    d = create_dict()

    for i in range(n):
        temp = ''
        for k in range(1, 6):
            temp += str(random.randint(1, 6))
        res += d[temp] + ' '
    return res.strip()


if __name__ == '__main__':
    print(generate(5))
