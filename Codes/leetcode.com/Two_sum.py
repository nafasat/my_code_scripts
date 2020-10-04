#!/usr/bin/python3

"""

Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""

"""
b=[]

a = [2,7,11,15]
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            pass
        else:
            if a[i] + a[j] == 9:
                if i not in b:
                    b.append(i)
                elif j not in b:
                    b.append(j)
                else:
                    pass

print(b)

"""


class Solution:
    def __init__(self, num_list):
        self.num_list = num_list

    def check_sum(self):
        out_list = set()
        input_length = len(self.num_list)
        for i in range(input_length):
            for j in range(input_length):
                if i != j:
                    if self.num_list[i] + self.num_list[j] == 9:
                        out_list.add(i)
                        out_list.add(j)
                        return list(out_list)


b = Solution([2, 7, 11, 15, 1, 8])
print(b.check_sum())
