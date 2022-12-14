def range__(*a):
    if (len(a) == 1):
        start, end, step = 0, a[0], 1
    elif (len(a)==2):
        start, end, step = a[0], a[1], 1
    else:
        start, end, step = a[0], a[1], a[2]
    if end < 0:
        step = -1
    ans = [i for i in range(start, end, step)]
    return ans

def rangeRight(*a):
    if (len(a) == 1):
        start, end, step, isRight = 0, a[0], 1, True
    elif (len(a) == 2):
        start, end, step, isRight = a[0], a[1], 1, True
    elif (len(a) == 3):
        start, end, step, isRight = a[0], a[1], a[2], True
    else:
        start, end, step, isRight = a[0], a[1], a[2], a[3]
    if end < 0:
        step = -1
    ans = [i for i in range(start, end, step)]
    if isRight:
        ans.reverse()
        return ans
    return ans
