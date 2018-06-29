# Tornado总结

## 通常同步的写法
```python
#! /usr/bin/python
# -*- coding: utf-8 -*-

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

```

*Tips： 只需要注意Requestandler对应业务，Applicaton对应路由表，最后监听端口，启动ioloop就完成了基本的web服务端*

## 使用异步的方法
需要使用gen模块
```python
from tornado import gen.coroutine
```
对Hanlder使用：
```python
def MainHanlder(web.RequestHandler):
    """假设这是主页面"""
    @gen.coroutine
    def get(self):
        """ 
        假设db.get_data()是一个需要阻塞，耗时很长的操作，
        使用异步时，在操作前使用yield，该操作会被挂起，
        然后程序继续进行其他操作，当耗时步骤结束后，程序返
        回到yield处，继续完成剩下的步骤
        """
        data = yield db.get_data()

    @gen.coroutine
    def work(self):
        """
        同样假设get_task()是一个耗时任务
        """
        task_data = yield get_task()

        # 需要返回一些数据的时候，如下使用
        # 这是由于coroutine实现的原因，所以返回值通过
        # gen.Return抛出来，coroutine中捕获这个异常，
        # 并将值存储在future对象中（future又是另一个概
        # 念了）
        raise gen.Return(task_data)
```


## 参考文档
| 名称 | 链接 |
| ----- | -----:|
| 进程和线程、协程的区别 | http://www.cnblogs.com/lxmhhy/p/6041001.html|
| Python协程：从yield/send到async/await | http://python.jobbole.com/86069/|
| tornado入门 | https://blog.csdn.net/lin06051180/article/details/73480832 | 
| 浅析tornado web框架| http://www.cnblogs.com/aylin/p/5702994.html |
| 构建Tornado网站应用 | http://www.cnblogs.com/liaofeifight/p/4920017.html|
| 一些tornado例子 | http://www.guideep.com/read?guide=5633494390669312#|
| Tornado官方文档 | http://www.tornadoweb.org/en/latest/ |
| 为什么要阅读Tornado的源码？|http://www.nowamagic.net/academy/detail/13321002|
