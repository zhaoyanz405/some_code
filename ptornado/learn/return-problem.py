#! /usr/bin/python

from tornado import gen, web, ioloop
import time

@gen.coroutine
def work():
    yield 1
    time.sleep(5)
    raise gen.Return('zhaoy')

d = work()

print(d)
time.sleep(6)
print(d)

