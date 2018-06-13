# -*- coding: utf-8 -*-
"""
将一个字符串逆序（不能使用反转函数）
"""

def reverse(str_input):
    if str_input is None or not isinstance(str_input, str):
        print("the parampters is not legal!")
        return None
    return str_input[::-1]


def test_reverse(str_input, result):
    if reverse(str_input)==result:
        print("input(%s) ,and it works ok." % ([str_input, result]))
    else:
        raise Exception("the value (%s) is not passed" % ([str_input, result]))


if __name__ == "__main__":
    test_data=[
        ['', ''],
        [1, None],
        [True, None],
        [list, None],
        ['a', 'a'],
        ['abcd', 'dcba'],
        ['00avd', 'dva00'],
    ]
    for data in test_data:
        test_reverse(data[0], data[1])