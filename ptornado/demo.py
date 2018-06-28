#! /usr/bin/python
# -*- coding: utf-8 -*-

from tornado import ioloop, web
from tornado.options import define
from pymongo import MongoClient


global_message_buffer = []

class HomeHandler(web.RequestHandler):
    """
    Home page

    """
    def get(self):
        self.render('home.html')

class MessageHandler(web.RequestHandler):
    """
    get message
    """
    def post(self, **kwargs):
        message={
            "msg1": self.get_argument('fname'),
            'msg2': self.get_argument('lname'),
        }
        self.write(message)


def single(cls):
    instances = {}
    def wrap(*args, **kwargs):
        if instances == {}:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]
    return wrap

@single
class DB(object):
    db = client = MongoClient().ppdb
    
    def __str__(self):
        print(self.db)

def start_app():
    app = web.Application([
        (r"/", HomeHandler),
        (r"/message/new", MessageHandler),
    ])

    app.listen(8000)
    ioloop.IOLoop.current().start()

if __name__ == "__main__":
    a=DB()
    b=DB()

    print(a)