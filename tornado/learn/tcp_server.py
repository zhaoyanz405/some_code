#! /usr/bin/python

from tornado import ioloop, gen, iostream
from tornado.tcpserver import TCPServer

class MyTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        try:
            while True:
                msg = yield stream.read_bytes(20, partial=True)
                print(msg, 'from', address)
                yield stream.write(msg[::-1])
                if msg == 'over':
                    stream.close()
        except Exception:
            pass

if __name__ == '__main__':
    server=MyTcpServer()
    server.listen(8760)
    server.start()

    ioloop.IOLoop.current().start()
