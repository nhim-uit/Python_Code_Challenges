# Linked Learning - Python Code Challenges
# 20 Jul, 2025
# Waiting game
import random
import time


def count():
    t = random.randint(2, 4)

    input('Enter to begin')
    start = time.perf_counter()

    input(f'Enter again after {t} seconds')
    elapsed = time.perf_counter() - start

    print(f'Elapsed time: {elapsed:.3f} seconds')
    if elapsed == t:
        print('Perfect')
    elif elapsed < t:
        print(f'{t - elapsed:.3f} seconds too fast')
    else:
        print(f'{elapsed - t:.3f} seconds too slow')


if __name__ == '__main__':
    count()
