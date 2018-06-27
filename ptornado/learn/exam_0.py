import tornado.ioloop
from tornado.gen import coroutine
from tornado.concurrent import Future
 
@coroutine
def asyn_sum(a, b):
    print("begin calculate:sum %d+%d"%(a,b))
    future = Future()
 
    def callback(a, b):
        print("calculating the sum of %d+%d:"%(a,b))
        future.set_result(a+b)
    tornado.ioloop.IOLoop.instance().add_callback(callback, a, b)
 
    result = yield future
 
    print("after yielded")
    print("the %d+%d=%d"%(a, b, result))
 
def main():
    asyn_sum(2,3)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()
