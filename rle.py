def rle(st):
    kolvo = 1
    answer = ""
    for i in range(1, len(st)):
        if(st[i] == st[i - 1]):
            kolvo += 1
        else:
            answer += st[i - 1] + (str(kolvo) if(kolvo != 1) else "")
            kolvo = 1
    if(kolvo != 0):
        answer += st[-1] + (str(kolvo) if(kolvo != 1) else "")
    return answer
