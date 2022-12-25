def flatten(cur_list):
    answer = []
    for i in cur_list:
        if(isinstance(i, list)):
            for j in i:
                if(isinstance(j, list)):
                    answer = answer + flatten(j)
                else:
                    answer.append(j)
        else:
            answer.append(i)
    return answer
