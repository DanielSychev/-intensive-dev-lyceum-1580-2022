def isEmpty(value):
    if(isinstance(value, int) or isinstance(value, bool) or value == None):
        return True
    elif len(value) == 0:
        return True
    else:
        return False
