def namespace(s):
    a=reversed(s.split('.'))
    b={}
    for i in a:
        b={i:b}
    print(b)
