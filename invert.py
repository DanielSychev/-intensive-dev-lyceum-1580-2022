def invert(obj):
    ans = {}
    for i in obj:
        ans[obj[i]] = i
    return ans
