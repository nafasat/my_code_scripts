#!/usr/bin/python3

"""

CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have 3 or 6 digits.
■ Each digit is in the range of 0 to F. ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E, and F).
■  letters can be lower case. ( a, b, c, d, e and f are also valid digits).


"""

import re


def to_get_all_hexacolor():
    List = []
    for _ in range(int(input())):
        for lines in re.findall(r'(#[A-F0-9a-f]{3}(?=;|,|\)))|(#[A-F0-9a-f]{6}(?=;|,|\)))', input()):
            List.append(lines)

    for i in List:
        for j in i:
            if j != '':
                print(j)


if __name__ == "__main__":
    to_get_all_hexacolor()
