""""Strings"""


def f(l, s, i):
    if l[i] == s:
        return s[:0:1]


l1 = ['cat', 'dog', 'oleg']
s1 = 'dog'

print(f(l1, s1, 1))


l = [1, 2, 3, 4, 5]

print(l[3:1:2])

print('cat'[-3])


