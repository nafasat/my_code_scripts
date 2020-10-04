#!/usr/bin/python

"""

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7, 8 or 9.

Concept

A valid mobile number is a ten digit number starting with a 7, 8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

Input Format

The first line contains an integer ,N the number of inputs.
N lines follow, each containing some string.


"""

import re

for _ in range(int(input())):
    line = input()
    if re.match(r"^[789]{1}\d{9}$", line):
        print("YES")
    else:
        print("NO")