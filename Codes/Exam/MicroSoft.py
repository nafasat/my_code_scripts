#!/usr/bin/python3
def inputarray(arr):
    new_list = []
    for i in arr:
        value = 1
        for j in arr:
            if i == j:
                pass
            else:
                value = value * j
        new_list.append(value)
    return new_list


if __name__ == "__main__":
    List = [1, 2, 3, 4, 5]
    print(inputarray(List))
