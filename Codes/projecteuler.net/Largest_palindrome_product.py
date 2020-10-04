#!/usr/bin/python3

'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


class Palindrome:
    def __init__(self):
        pass

    def ispalindrome(self, x):
        self.x = x
        d = str(self.x)
        l = len(d)
        if l % 2 == 0:
            string_len = int((l / 2)) + 1
        else:
            string_len = int(l / 2)

        for i in range(string_len):
            if d[i] == d[(i * -1) - 1]:
                pass
            else:
                return False

        return self.x

    def max_valve(self, List):
        self.List = List
        max_number = self.List[0]
        for j in range(1, len(self.List)):
            if max_number > self.List[j]:
                pass
            else:
                max_number = self.List[j]
        return max_number


a = Palindrome()
List = []
for first_number in range(100, 1000):
    for second_number in range(100, 1000):
        output = first_number * second_number
        if a.ispalindrome(output):
            List.append(output)

print(List)
print(a.max_valve(List))