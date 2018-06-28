# -*- coding: utf-8 -*-
#! /usr/bin/python

from tornado import web
from tornado import ioloop


class FactorialService(object):
    """

    定义一个阶乘服务对象
    """
    def __init__(self):
        self.cache = {}

    def calc(self, n):
        if n in self.cache:
            return self.cache[n]
        
        s = 1
        for i in range(1, n + 1):
            s *= i
        self.cache[n] = s
        return s


class FactorialHanlder(web.RequestHandler):
    """
    """
    service = FactorialService()

    def get(self):
        n = int(self.get_argument("n"))
        self.write(str(self.service.calc(n)))


def make_app():
    return web.Application([
        (r'/fact', FactorialHanlder)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)

    ioloop.IOLoop.current().start()