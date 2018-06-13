# -*- encoding: utf-8 -*-
"""
有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。
"""


def func(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    c = list(a) + list(b)
    c.sort()
    print(reduce(lambda x, y: x + y, a) - reduce(lambda x, y: x + y, b))
    return c[0::2], c[1::2]


if __name__ == "__main__":
    a, b = [1, 4, 5, 800], [2, 3, 6, 700]
    print(func(a, b))

    a, b = [50, 90, 10000], [1, 100, 10001]
    print(func(a, b))

    a, b = [2, 3, 6, 7, 10], [1, 4, 5, 8, 9]
    print(func(a, b))

    a, b = [1, 3, 29, 232, 12311], [1, 2, 30, 210, 12312]
    print(func(a, b))
