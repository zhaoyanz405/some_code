# -*- coding: utf-8 -*-
#! /usr/bin/python

from tornado import web
from tornado import ioloop


class MainHandler(web.RequestHandler):
    """
    Main page

    handler类，代表着业务逻辑，服务端开发就是编写一堆堆的
    handler来服务客户端请求
    """
    def get(self):
        """
        对应http GET方法
        """
        self.write("Hello world !")
    
    def post():
        pass


def make_app():
    """
    app实例，代表一个完成的后端app，它会挂接一个服务器套接字
    端口对外提供服务。一个可以有多个app实例（一般不会用到）

    returnb application
    """

    # 路由表，将制定的url规则和handler对应起来
    return web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    """
    当一个请求到来时，ioloop读取这个请求解包成一个http请求对象，
    找到该套接字对应的app路由表，通过请求对象的url查询路由表中
    挂接的handler，然后执行handler。执行后返回一个对象，ioloop
    将对象包装成http响应对象序列化发送给客户端。
    """
    app = make_app()
    app.listen(8000)

    # ioloop实例，掌管全局tornado事件，服务器的引擎核心
    ioloop.IOLoop.current().start()