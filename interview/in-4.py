# -*- coding: utf-8 -*-
"""
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样
的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
import pdb


def get_value(li, horiz, vtcl):
    print([horiz, vtcl])
    return li[horiz][vtcl]


def solve(data, ret_num):
    horiz_n = len(data[0]) - 1
    vtcl_m = len(data) - 1

    horiz, vtcl = horiz_n, 0

    while horiz > 0 and vtcl <= vtcl_m:
        val = get_value(data, vtcl, horiz)
        if val < ret_num:
            vtcl = vtcl + 1
        elif val > ret_num:
            horiz = horiz - 1
        elif val == ret_num:
            return True, "(%s, %s)" % (vtcl, horiz)

    print('%s is not found in %s' % (ret_num, data))
    return False


def test_solve():
    test_data = [
        [1, 3, 7, 9, 11],
        [2, 6, 8, 10, 14],
        [3, 11, 15, 18, 25],
        [4, 14, 26, 37, 48],
    ]

    print(solve(test_data, 8))
    print(solve(test_data, 14))
    print(solve(test_data, 19))


if __name__ == "__main__":
    test_data = [
        [1, 3, 7, 9, 11],
        [2, 6, 8, 10, 14],
        [3, 11, 15, 18, 25],
        [4, 14, 26, 37, 48],
    ]
    print(solve(test_data, 37))
