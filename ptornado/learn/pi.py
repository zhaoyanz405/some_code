# -*- coding: utf-8 -*-
#! /usr/bin/python

import json
import math
import redis
from tornado import web, ioloop


class FactorialService(object):
    def __init__(self, cache):
        self.cache = cache
        self.key = 'Factorials'

    def calc(self, n):
        s = self.cache.hget(self.key, str(n))
        if s :
            return int(s)
        
        s = 1
        for i in range(1, n + 1):
            s *= i
        
        self.cache.hset(self.key, str(n), str(s))
        return s, False


class PiService(object):
    def __init__(self, cache):
        self.cache = cache
        self.key = "pis"

    def calc(self, n):
        s = self.cache.hget(self.key, str(n))
        if s:
            return float(s), True

        s = 0.0
        for i in range(1, n + 1):
            s += 1.0/(2*i + 1)/(2*i + 1)

        s = math.sqrt(s * 8)
        self.cache.hset(self.key, str(n), str(s))

        return s, False


class FactorialHandler(web.RequestHandler):
    def initialize(self, factorial):
        self.factorial = factorial

    def get(self):
        n = int(self.get_argument('n') or 1)
        fact, cached = self.factorial.calc(n)

        result = {
            "n" : n,
            "fact" : fact,
            "cached" : cached
        }
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(result))


class PiHandler(web.RequestHandler):
    def initialize(self, pi):
        self.pi = pi
    
    def get(self):
        n = int(self.get_argument("n") or 1)
        pi, cached = self.pi.calc(n)

        result = {
            "n": n,
            "pi": pi,
            "cache": cached
        }

        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json.dumps(result))


def make_app():
    cached = redis.StrictRedis('localhost', 6379)
    factorial = FactorialService(cached)
    pi = PiService(cached)

    return web.Application([
        (r'/fact', FactorialHandler, {'factorial': factorial}),
        (r'/pi', PiHandler, {"pi": pi}),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)

    ioloop.IOLoop.current().start()