#! /usr/bin/python

from tornado.httpclient import AsyncHTTPClient, HTTPClient
from tornado.concurrent import Future


http_client = AsyncHTTPClient()

m_future = Future()

fetch_future = http_client.fetch("http://www.baidu.com")

fetch_future.add_done_callback(lambda f: m_future.set_result(f.result()))


