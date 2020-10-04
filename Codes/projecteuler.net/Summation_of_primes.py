#!/usr/bin/python3

"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


class Solutions:
    def __init__(self, limt):
        self.limit = limt

    def get_primes_list(self):
        List = [2]
        c = 3
        while c < self.limit:
            count = 0
            loop = 0
            for i in range(2, c):
                loop += 1
                if c % i == 0:
                    break
                else:
                    count += 1
            if loop == count:
                List.append(c)
            c += 1

        print(sum(List))


a = Solutions(2000)
a.get_primes_list()