#!/usr/bin/python3

'''
Problem 6

The sum of the squares of the first ten natural numbers is,
        1^2 + 2^2 + 3^2 .. 10^2 = 385
The square of the sum of the first ten natural numbers is,
        (1,2,3..10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''


def range_number(number):
    sum_squares = 0
    square_sum = 0
    for i in range(1, number+1):
        sum_squares = sum_squares + i**2
        square_sum = square_sum + i

    print("sum of the squares", number, "natural numbers is",  sum_squares)
    print("square of the sum the first", number, "natural numbers is", square_sum**2)

    print("Hence the difference between the sum of the squares of the first", number, "natural numbers and the square of the sum is", (square_sum**2)-sum_squares)


range_number(100)