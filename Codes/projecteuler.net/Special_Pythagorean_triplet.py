#!/usr/bin/python3

'''

Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.


There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


'''


def pythagoreantriplets(limits):
    c, m = 0, 2
    while c < limits:
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m+n*n

            if c > limits:
                break
            print(a, b, c)
        m = m+1


if __name__ == '__main__':
    limit = 20
    pythagoreantriplets(limit)