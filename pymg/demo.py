#! /usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.zhaoy
print(db.zhaoy.find_one())