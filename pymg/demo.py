#! /usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.zhaoy
print(db.zctl.find_one)