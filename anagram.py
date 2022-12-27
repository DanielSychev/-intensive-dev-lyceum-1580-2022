"""
алгоритм работает за счёт сортировки слова ( это и будет общим ключём у всех анаграм в словаре)
ассимптотика:
О(сумма всех MlogM, где M - длина слова) ну или О(n*MlogM,где M - длина наибольшего слова)
"""
def anagram(a):
    dictionary = {}
    for i in a:
        temp = i
        i = "".join(sorted(i))
        if(dictionary.get(i)):
            dictionary[i].append(temp)
        else:
            dictionary[i] = [temp]

    answer = []
    for i in dictionary:
        if(len(dictionary[i]) != 1):
            answer.append(sorted(dictionary[i]))
    return answer
