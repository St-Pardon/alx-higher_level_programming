#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list2 = my_list[:]
    if idx < 0 or idx > (len(my_list2) - 1):
        return my_list2
    else:
        my_list2[idx] = element
        return my_list2
