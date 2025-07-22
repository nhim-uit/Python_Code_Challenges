# Linked Learning - Python Code Challenges
# 22 Jul, 2025
# Count unique words

def count_words(file):
    res = {}

    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isalpha():
                    res[word] = res.get(word, 0) + 1

    # print(res)
    res = sorted(res, key=lambda x: res[x], reverse=True)
    return res[:20]


if __name__=='__main__':
    print(count_words('pg100.txt'))
