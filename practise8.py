# -*- coding: utf-8 -*-

def cc(num=0):
    for i in range(num):
        yield i

def fib(n):
    before1 = 0
    before2 = 1
    for i in range(n):
        now = before1 + before2
        yield now
        before1, before2 = before2, now

if __name__ == "__main__":
    for i in fib(10):
        print(i)