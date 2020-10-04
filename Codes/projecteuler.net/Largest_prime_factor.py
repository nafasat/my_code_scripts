#!/usr/bin/python3

'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

import sys


def largest(primelist):
    k = 1
    for value in primelist:
        if k < value:
            k = value

    print("Largest Prime => ", k)


def prime_factor(input_factor):
    prime_list = []
    for k in input_factor:
        if k == 1 or k == 2:
            pass
        else:
            number = 0
            count = 0
            for nu in range(2, k):
                number = number + 1
                if k % nu == 0:
                    break
                else:
                    count = count + 1
            if count == number:
                prime_list.append(k)
    print("Prime Factor => ", prime_list)
    largest(prime_list)


def factor(number):
    number = int(number)
    if number < 0:
        print("No factor for Negative Number")
        sys.exit(1)
    elif number == 0:
        print("Factor of 0 is 1")
        sys.exit(0)
    else:
        List = [1]
        for i in range(2, number + 1):
            if number % i == 0:
                List.append(i)

        print("Factor => ", List)
        prime_factor(List)


if __name__ == "__main__":
    input_number = input("Pass a number\t")
    factor(input_number)
