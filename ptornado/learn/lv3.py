# -*- coding:utf-8 -*-
#! /usr/bin/python

from tornado import ioloop
from tornado.gen import coroutine
from tornado.concurrent import Future

@coroutine
def asyn_sum(a):
    print("begin %d calculate" % a)
    future = Future()

    def callback(a):
        print("calculating")
        future.set_result(a*2)
    
    ioloop.IOLoop.instance().add_callback(callback, a)

    result = yield future

    print("after yielded")
    print("the %d ret is %d" % (a, result))


def main():
    for i in range(10):
        asyn_sum(i)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()