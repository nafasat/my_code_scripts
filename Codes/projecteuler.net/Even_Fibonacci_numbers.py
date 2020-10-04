#!/usr/bin/python3

'''

Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

List = [1, 1]
while True:
    print(List[1])
    a = List[1]
    List[1] = List[0] + List[1]
    List[0] = a

    if List[1] > 4000000:
        break
