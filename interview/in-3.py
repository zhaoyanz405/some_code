# -*- coding: utf-8 -*-
import copy

a = [1,2,3,]
b = copy.deepcopy(a)

print(a is b)
print(a == b)