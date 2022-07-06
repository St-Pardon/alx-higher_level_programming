#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max_num = max(list_num)

    for n in list_num:
        if max_num > n:
            sub += n

    return (max_num - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    key = list(roman.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for i in roman_string:
        for j in key:
            if j == i:
                if roman.get(i) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [roman.get(i)]
                else:
                    list_num.append(roman.get(i))

                last_rom = roman.get(i)

    num += to_subtract(list_num)

    return (num)
