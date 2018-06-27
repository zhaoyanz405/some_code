#! -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class MeHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('haha me')

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/me", MeHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
