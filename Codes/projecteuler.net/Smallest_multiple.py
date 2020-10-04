#!/usr/bin/python3

'''
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''


def input_maxnumber(x):
    for i in range(10, x):
        count = 0
        for j in range(1, 11):
            if i % j == 0:
                count = count + 1

            if count == 10:
                print("Vaue is", i)
                return True


input_maxnumber(10000000)