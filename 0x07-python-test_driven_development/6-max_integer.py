#!/usr/bin/python3
'''Contains a max_integer function'''


def max_integer(list=[]):
    if len(list) == 0:
        return None
    ans = list[0]
    i = 1
    while i < len(list):
        if list[i] > ans:
            ans = list[i]
        i += 1
    return ans
