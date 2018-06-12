# -*- coding:utf-8 -*-

import requests


def o_get(url=None):
    assert url != None, "url must not be None."
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    print(o_get('http://gitbook.cn'))
