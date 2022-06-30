#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    line = len(sys.argv) - 1

    if line == 0:
        print("{} arguments.".format(line))
    elif line == 1:
        print("{} argument:".format(line))
    else:
        print("{} arguments:".format(line))

    if line >= 1:
        line = 0
        for arg in sys.argv:
            if line != 0:
                print("{}: {}".format(line, arg))
            line += 1
