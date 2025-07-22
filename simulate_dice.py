# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# simulate a dice

import random
import matplotlib.pyplot as plt

NO_OF_TRIALS = 1_000_000
res = {}


def roll_dice(dice, no_of_trials=NO_OF_TRIALS):
    for i in range(NO_OF_TRIALS):
        s = 0
        for j in range(dice):
            face = random.randint(1, 6)
            s += face
        res[s] = (res.get(s, 0) + 1)

    # for i in res:
    #     print(f'Face {i} = {res[i]/NO_OF_TRIALS*100:.2f}%')

    return res


def draw(data):
    x = list(data.keys())
    y = list(data.values())

    # Plot the graph
    plt.figure(figsize=(8, 5))
    plt.bar(x, y, color='b', width=0.8)
    plt.title("Graph from Dictionary")
    plt.xlabel("Face")
    plt.ylabel("Percentage (%)")
    plt.grid(True)
    plt.show()


if __name__=='__main__':
    draw(roll_dice(6))
