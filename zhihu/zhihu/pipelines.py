# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from zhihu.items import CategoryItem
from zhihu.items import ClubItem
import time,datetime

class ZhihuPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        now=datetime.datetime.now()
        date=now.strftime("%Y-%m-%d %H:%M:%S")
        # 这里写得好粗暴，但是sql自动执行的那条语句在我的电脑里mysql环境下运行会报错Orz 就是那个秘制``和''的问题...窒息
        # 此处代码有待改进！
        if isinstance(item,CategoryItem):
            sql="insert into `category` (`id`, `name`,`totals`,`time`) values (%s,%s,%s,%s)"
            self.cursor.execute(sql,(item['id'],item['name'],item['totals'],date))
            self.db.commit()
        if isinstance(item,ClubItem):
            sql="insert into `club` (`id`, `name`, `category`, `description`, `created_at`, `join_count`, `post_count`,`time`) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(item['id'],item['name'],item['category'],item['description'],item['created_at'],item['join_count'],item['post_count'],date))
            self.db.commit()
        return item
