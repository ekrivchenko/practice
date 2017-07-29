""""Strings"""

str1 = 'test string 1 t t t'
str2 = 'test string 2'

list1 = []
list2 = []

for item in str1:
    list1.append(item)
for item in str2:
    list2.append(item)

a = sorted(list1)
list3 = int()


print(isinstance(3, int))


while(list1):
    print(list1.pop())

if 'test' in str1:
    print(str1[:])

d = {1: 2, 2: 3, 6: 7}

if 6 in d:
    print(d[6])
