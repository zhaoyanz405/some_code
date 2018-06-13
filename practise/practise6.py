import copy

a1 = [[1], [2], [3]]
b1 = copy.copy(a1)
c1 = copy.deepcopy(a1)

print(b1)
print(c1)

a1[0][0] = 0
a1[1] = None

print(b1)
print(c1)
print(a1[10:])