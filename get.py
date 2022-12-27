def get(object, path):
    array = path.split('.')
    for i in array:
        try:
            if (i == 'length'):
                object = len(object)
                continue
            if (i.isdigit()):
                i = int(i)
            object = object[i]
        except:
            print("undefined")
            exit(0)
    return object
