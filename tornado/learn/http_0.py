#! /usr/bin/python

from tornado.ioloop import IOLoop
from tornado import gen, web

class ExampleHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        delay=self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status":1, "msg":"success"})
        self.finish()


if __name__ == "__main__":
    app = web.Application([
                  (r"/example", ExampleHandler),], autoreload=True)

    app.listen(8765)
    IOLoop.current().start()
