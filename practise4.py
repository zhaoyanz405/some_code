# -*- coding: utf-8 -*-
import time


def fib(n):
    """斐波那契数列

    :param n:
    :return:
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    tmp = fib(10)
    for n in tmp:
        print(n)

    time.sleep(1)

    tmp = fib(10)
    while True:
        print(next(tmp))