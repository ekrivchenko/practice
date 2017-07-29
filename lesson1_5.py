""""Strings"""


d = {'cat': 6, 1: 2, 3: 4, 5: 6}

values = d.keys()

print(values)

for item in d:
    print('Value is {0}, key is {1}'.format(type(d[item]), type(item)))

