#! /usr/bin/python

from tornado.httpclient import HTTPClient


def sync_fetch():
    http_client = HTTPClient()
    response = http_client.fetch("http://www.baidu.com")
    print(response.body)



sync_fetch()
