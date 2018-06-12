# -*- coding:utf-8 -*-

from functools import reduce
nums = [1, 2, 3, 4, 5]
after_reduce = reduce((lambda x, y : x * y), nums)
print(after_reduce)