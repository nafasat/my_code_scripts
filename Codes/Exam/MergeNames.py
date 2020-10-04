#!/usr/bin/python3

'''
Implement the unique_names method. When passed two lists of names, it will return a list containing the names that appear in either or both lists. The returned list should have no duplicates.

For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava, Emma, Olivia, and Sophia in any order.

'''

def unique_names(List1, List2):
    for i in List1:
        if i not in List2:
            List2.append(i)
    print(List2)


if __name__ == "__main__":
    unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])