def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)

def euclid(*args):
    if(len(args) == 0):
        return -1
    answer = args[0]

    for i in range(1, len(args)):
        if(int(args[i]) != args[i]):
            return -1

        answer = gcd(answer, args[i])

    return answer
