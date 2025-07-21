# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# simulate a dice
import random

NO_OF_TRIALS = 1_000_000
res = {}


def roll_dice(dice, no_of_trials=NO_OF_TRIALS):
    for i in range(NO_OF_TRIALS):
        s = 0
        for j in range(dice):
            face = random.randint(1, 6)
            s += face
        res[s] = res.get(s, 0) + 1

    for i in res:
        print(f'Face {i} = {res[i]/NO_OF_TRIALS*100:.2f}%')

    return res


roll_dice(4)

