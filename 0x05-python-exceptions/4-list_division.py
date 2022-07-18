#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    arr = []
    for i in range(list_length):
        ans = 0
        try:
            a, b = (my_list_1[i], my_list_2[i])
            ans = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            arr.append(ans)
    return arr
