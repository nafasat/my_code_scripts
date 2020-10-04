#!/usr/bin/python3

'''

Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

'''

from collections import defaultdict

# Initialize dictionary
test_dict = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

# printing original dictionary
print("The original dictionary : ", test_dict)

# Using sorted() + items() + defaultdict()
# Grouping dictionary keys by value
res = defaultdict(list)
print(sorted(test_dict.items()))
for key, val in sorted(test_dict.items()):
    res[val].append(key)

# printing result
print("Grouped dictionary is : " + str(dict(res)))