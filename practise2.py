# -*- coding -*-

def func_x(*a, **b):
    """

    :param a:
    :param b:
    :return:
    """
    print(a)
    print(b)


if __name__ == '__main__':
    x = [1, 2, 3, 4]
    y = {'a': 1, 'b': 2}
    func_x(*x, **y)
