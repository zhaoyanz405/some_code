# -*- coding: utf-8 -*-
#! /usr/bin/python

from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    """
    Main page
    """
    def get(self):
        self.write("Hello world !")


def make_app():
    """

    returnb application
    """
    return web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    ioloop.IOLoop.current().start()