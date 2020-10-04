#!/usr/bin/python3

def maxminvalue(List):
    max=List[0]
    min=List[0]
    for i in List:
        if max < i:
            max = i
        elif min > i:
            min = i
        else:
            pass
    print(max)
    print(min)


maxminvalue([1,2,3,4,11,6,-3,111])