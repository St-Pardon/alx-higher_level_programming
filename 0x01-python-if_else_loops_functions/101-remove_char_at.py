#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    newStr = ""
    for j in str:
        if i != n:
            newStr += j
        i += 1
    return newStr
