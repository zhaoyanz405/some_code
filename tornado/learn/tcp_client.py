#! /usr/bin/python

from tornado import ioloop, gen, iostream
from tornado.tcpclient import TCPClient

@gen.coroutine
def Trans():
    stream = yield TCPClient().connect('localhost', 8760)
    try:
        for msg in (' zzxxc', 'abcde', 'i feel good.' 'over'):
            yield stream.write(msg)
            back = yield stream.read_bytes(20, partial=True)
            print('back: %s' % back)

    except Exception:
        pass

if __name__ == "__main__":
    ioloop.IOLoop.current().run_sync(Trans)


