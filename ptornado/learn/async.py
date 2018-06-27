#! /usr/bin/python
import time
from tornado.httpclient import AsyncHTTPClient, HTTPClient

def handle_response(res):
    print(res.body)


http_client = AsyncHTTPClient()
http_client.fetch("http://www.baidu.com", handle_response)

time.sleep(5)
http_client.close()
