#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        tup = (length, None)
    else:
        tup = (length, sentence[0])
    return tup
