import random

def shuffle(array):
    n = len(array)
    pos = [i for i in range(n)]
    answer = []
    for i in range(n):
        iterator = random.randrange(0, len(pos))
        answer.append(array[pos[iterator]])
        pos.pop(iterator)
    return answer
