def last(v_list):
    if not(isinstance(v_list, list)):
        return 'undefined'
    if len(v_list) == 0:
        return 'undefined'
    return v_list[-1]

def first(v_list):
    if not(isinstance(v_list, list)):
        return 'undefined'
    if len(v_list) == 0:
        return 'undefined'
    return v_list[0]
