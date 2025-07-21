# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# Save a dictionary
import json
import pickle


# instructor's solutioin
def write(d: dict, file_path: str):
    with open(file_path, 'wb') as file:
        pickle.dump(d, file)


def load(file_path):
    with open(file_path, 'rb') as file:
        pickle.load(file)


# my solution
def write2(d, file_path):
    with open(file_path, 'w') as file:
        file.write(json.dumps(d, indent=4))


write2({'Alex': 30, 'Jen': 22}, 'example.txt')
