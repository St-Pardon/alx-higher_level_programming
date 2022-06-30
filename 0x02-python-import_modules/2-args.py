#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    line = 1
    print(f"{len(sys.argv) - 1} arguments:")
    for arg in range(len(sys.argv) - 1):
        print(f"{line}: {sys.argv[line]}")
        line += 1
