# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


url = r"http://www.gaokao.com/baokao/lqfsx/sbfsx/"
req = requests.get(url)
html = req.text

bf = BeautifulSoup(html)
texts = bf.find_all('div', class_='clearfix')
bf_dl = BeautifulSoup(str(texts[0]))
print(bf_dl.find_all('dl', class_='area_mod'))