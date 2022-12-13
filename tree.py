def tree(n):
    try:
        n = int(n)
    except:
        raise TypeError
    if n < 3 :
        return 'null'
    k = 2 * n - 3
    res=""
    for i in range(1, k + 1, 2):
        res += ' ' * ((k - i)//2) + '*' * i + ' ' * ((k - i)//2) + '\n'
    res+=' ' * (n-2) + '|' + ' ' * (n-2) + '\n'
    return res
