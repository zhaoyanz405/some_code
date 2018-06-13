# -*- coding: utf-8 -*-
import time

def deco(func):
    """打印函数所执行的时间

    :param func: 被装饰的函数
    :return:
    """
    def _any_name_is_ok(*args, **kwargs):
        time_begin = time.time()
        func(*args, **kwargs)
        print("func({0}) has spent {1} senconds.".format(func.__name__, time.time() - time_begin))
        return func

    return _any_name_is_ok
@deco
def add(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
