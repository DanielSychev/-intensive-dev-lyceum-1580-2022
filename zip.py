def zip(objects):
    answer = {} #хоть не в первоначальном порядке, зато быстро

    for i in range(len(objects)-1, -1, -1):
        for j in objects[i]:
            answer[j] = objects[i][j]

    return answer
