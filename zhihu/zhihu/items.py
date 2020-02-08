# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.exceptions import DropItem

class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CategoryItem(scrapy.Item):
    table='category'
    id=scrapy.Field()
    name=scrapy.Field()
    totals=scrapy.Field()
    time=scrapy.Field()

class ClubItem(scrapy.Item):
    table='club'
    id=scrapy.Field()
    name=scrapy.Field()
    description=scrapy.Field()
    created_at=scrapy.Field()
    join_count=scrapy.Field()
    post_count=scrapy.Field()
    category=scrapy.Field()