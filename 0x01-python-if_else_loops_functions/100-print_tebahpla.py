#!/usr/bin/python3
for char in reversed(range(97, 123)):
    print("{:c}".format(char if (char % 2 == 0) else (char - 32)), end='')
