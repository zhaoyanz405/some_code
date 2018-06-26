#! /usr/bin/python


from tornado.httpclient import AsyncHTTPClient, HTTPClient

from tornado import gen



async def fetch_coroutine():
    http_client = AsyncHTTPClient()
    response =  await http_client.fetch('http://www.baidu.com')
    return response.body


fetch_coroutine()



