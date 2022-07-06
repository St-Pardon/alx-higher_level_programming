#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    arr = list(dic.keys())
    for i in arr:
        dic[i] = dic[i] * 2
    return dic
