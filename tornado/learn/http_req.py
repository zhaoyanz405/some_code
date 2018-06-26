from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpclient import AsyncHTTPClient

url = 'http://hq.sinajs.cn/list=sz000001'

class GetPageHandler(web.RequestHandler):
    @gen.coroutine
    def get(self):
        client=AsyncHTTPClient()
        response = yield client.fetch(url, method='GET')
        self.write(response.body.decode('gbk'))
        self.finish()

if __name__ == '__main__':
    app = web.Application([(r"/getpage",GetPageHandler),], autoreload=True)
    app.listen(8765)

    IOLoop.current().start()
