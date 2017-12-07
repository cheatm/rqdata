# encoding:utf-8
from pymongo import MongoClient
from fxdayu_data.data_api import mongo

client = MongoClient("mongodb://192.168.0.101,192.168.0.102")

bonus = mongo.bonus(client, "bonus")

candle = mongo.candle(client, bonus, H="Stock_H", D="Stock_D")

factor = mongo.factor(client, "factor")

info = mongo.info(client, "info")
