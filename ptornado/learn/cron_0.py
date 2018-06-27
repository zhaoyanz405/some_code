#! /usr/bin/python

from tornado import ioloop, gen

@gen.coroutine
def count():
    print('1 second has gone')


if __name__ == '__main__':
    ioloop.PeriodicCallback(count, 1000).start()
    ioloop.IOLoop.current().start()


