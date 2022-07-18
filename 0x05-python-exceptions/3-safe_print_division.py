#!/usr/bin/python3
def safe_print_division(a, b):
    ans = 0
    try:
        ans = a / b
    except Exception:
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return ans
