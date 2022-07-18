#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for num in range(x):
        j = my_list[i]
        try:
            print("{:d}".format(j), end="")
            i += 1
        except ValueError:
            continue
    print("")
    return(i)
