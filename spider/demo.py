# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup


def get_content(url=None):
    assert url != None, "url must not be None."
    req = requests.get(url)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_='showtxt')
    content = texts[0].text.replace('\xa0'*8, '\n')
    return content

def get_all_url(url=None):
    server = 'http://www.biqukan.com/'
    assert url != None, "url must not be None"
    req = requests.get(url)
    bf = BeautifulSoup(req.text)
    div = bf.find_all('div', class_ ='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    hrefs = a_bf.find_all('a')

    ret = dict()
    for each in hrefs:
        ret[each.string] = server + each.get('href')

    return ret

def write_into_file(name=None):
    chapter_dict = get_all_url("http://www.biqukan.com/1_1094/")
    for k,v in chapter_dict.items():
        content = get_content(url=v)
        with open(name, 'w+') as f :
            f.write(k)
            f.write(content)
        print(k)
    

if __name__ == "__main__":
    write_into_file('D://test.txt')