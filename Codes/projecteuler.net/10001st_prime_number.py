#!/usr/bin/python

'''
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''


def input_range(position):
    List = [2, 3]
    numbers = 5
    while True:
        count = 0
        if len(List) >= position:
            print(List[position-1])
            break

        else:
            for divby in range(2, numbers):
                if numbers % divby == 0:
                    break
                else:
                    count = count + 1
        if numbers == count + 2:
            List.append(numbers)

        numbers = numbers + 1


input_range(2)