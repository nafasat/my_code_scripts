#!/usr/bin/python3

"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits ( 0 - 9 ).
It should only contain alphanumeric characters ( a - z, A - Z & 0 - 9 ).
No character should repeat.
There must be exactly 10 characters in a valid UID.

Sample Input:
2
B1CD102354
B1CDEF2354

Sample Output

Invalid
Valid

"""


def upper_count(string_input):
    return sum(e.isdigit() for e in string_input)


def check_similarword(check):
    count = 1
    for w in check:
        if check.count(w) > 1:
            count += 1
            break
    return count


def check_digit_count(string_check):
    return sum(c.isdigit() for c in string_check)


def check_valid_uid():
    uid_list = []
    for _ in range(int(input())):
        uid_list.append(input())

    for eid in uid_list:
        if len(eid) != 10 or upper_count(eid) < 2 or check_similarword(eid) > 1 or check_digit_count(eid) < 3:
            print("Invalid")
        else:
            print("Valid")


if __name__ == "__main__":
    check_valid_uid()