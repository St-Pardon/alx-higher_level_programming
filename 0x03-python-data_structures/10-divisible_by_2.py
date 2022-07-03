#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    arr = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            arr.append(True)
        else:
            arr.append(False)

    return (arr)
