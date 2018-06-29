#! /usr/bin/python
# -*- coding: utf-8

from tornado import ioloop, gen, web

class LoginHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.set_secure_cookie('username', 'zhaoy')
        self.write('login ok')
        self.finish()


class LogoutHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.clear_cookie('username')
        self.write('logout ok')
        self.finish()


class WhoHandler(web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username') or 'unknown'

    @gen.coroutine
    def get(self):
        if not isinstance(self.current_user, str):
            self.current_user = self.current_user.decode()
        self.write('you are ' + self.current_user)
        self.finish()
    

if __name__ == '__main__':
    app = web.Application([
        (r'/login', LoginHandler),
        (r'/logout', LogoutHandler),
        (r'/whoami', WhoHandler),
    ],  autoreload=True,
        cookie_secret="feljjfesrh48thfe2qrf3np2zl90bmw",)

    app.listen(8000)

    ioloop.IOLoop.current().start()
