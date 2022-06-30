#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    line = 1
    print("{} arguments:".format(len(sys.argv) - 1)
    for arg in range(len(sys.argv) - 1):
        print(f"{}: {}".format(line, sys.argv[line])
        line += 1
