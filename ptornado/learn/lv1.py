# -*- coding: utf-8 -*-
#! /usr/bin/python

from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    """
    Main page
    """
    def get(self):
        """
        对应http GET方法
        """
        self.write("Hello world !")


def make_app():
    """
    app实例，代表一个完成的后端app，它会挂接一个服务器套接字
    端口对外提供服务。一个可以有多个app实例（一般不会用到）

    returnb application
    """
    return web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)

    # ioloop实例，掌管全局tornado事件，服务器的引擎核心
    ioloop.IOLoop.current().start()