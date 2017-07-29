a1 = 1
a2 = 3
b1 = '134343'
b2 = 'dog'
c1 = [1, 2, 3]
c2 = [4, 5, 6]
d1 = {'1': 'cat', '2': 'dog'}
d2 = {1: 'cat', 2: 'dog'}

all = [a1, a2, b1, b2, c1, c2, d1, d2]
all_dict = {1: b1, b1: 2}

a1 += 1
a1 *= 2

a3 = a1 + a2

try:
    int(b1)
except Exception:
    print('NON INT')

if b1.isdigit():
    b3 = int(b1)
    print(b3)
else:
    print('Non int')



#print(all)
#print(all_dict)

"--------------------------------------------------------------------------------------------------------------"
falses = [0, '', False, None, [], {}, ()]

for item in falses:
    if not item:
        print('Found false')

for i in range(0, len(falses)):
    if not falses[i]:
        print('Found false')
"--------------------------------------------------------------------------------------------------------------"
