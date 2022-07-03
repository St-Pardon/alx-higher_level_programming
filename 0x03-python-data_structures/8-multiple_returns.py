#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        return tuple(0), None
    else:
        return length, sentence[0]
