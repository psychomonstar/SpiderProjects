# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UserItem(scrapy.Item):
    uid = scrapy.Field()
    name = scrapy.Field()  # 昵称
    sign = scrapy.Field()  # 签名
    addr = scrapy.Field()   # 地址
    reg_time = scrapy.Field()  # 注册时间
    intro = scrapy.Field()  # 个人介绍
    follows = scrapy.Field()  # 关注数
    followers = scrapy.Field()  # 粉丝数


class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    rating_num = scrapy.Field()
    rating_people = scrapy.Field()
