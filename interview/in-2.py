# -*- coding: utf-8 -*-

"""
求从10到100中能被3或5整除的数的和
"""

def solve():
    n1 = 10
    n2 = 100
    ret = list()
    for n in range(10, 100):
        if n % 3 == 0 or n % 5 == 0:
            ret.append(n)
    print(ret)


if __name__ == "__main__":
    solve()