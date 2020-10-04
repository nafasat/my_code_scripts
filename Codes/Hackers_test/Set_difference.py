#!/usr/bin/python3

"""
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

4
Explanation

The roll numbers of students who only have English newspaper subscriptions are:
4,5,7 and 9.
Hence, the total is 4 students.

"""
_,a,_,b = ({*input().split()}for _ in range(4))
print(len(a.symmetric_difference(b)))