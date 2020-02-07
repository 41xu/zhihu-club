# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Request
from zhihu.items import CategoryItem, ClubItem

categories = {
    "1178345206151356416": "兴趣",
    "1178345195124490240": "明星",
    "1178345203794063360": "行业",
    "1178345201055260672": "校园",
    "1178345405397508096": "教育",
    "1178345219228225536": "情感",
    "1178345208739205120": "生活",
    "1178345402679595008": "游戏",
    "1178345211176026112": "影视",
    "1178345407711830016": "人文",
    "1178345213473615872": "闲趣",
    "1178345471801753600": "动漫",
    "1178345497302192128": "其他",
}

page = 50  # 每次请求返回50个club信息


class ZhihuClubSpider(scrapy.Spider):
    name = 'zhihu-club'
    allowed_domains = ['www.zhihu.com']

    # allowed_domains = ['www.zhihu.com/club/explore']
    # start_urls = ['https://www.zhihu.com/club/explore']
    # base_url="https://www.zhihu.com/api/v4/clubs/categories/"+club_id
    def start_requests(self):
        base_url = "https://www.zhihu.com/api/v4/clubs/categories/"
        ids = categories.keys()
        for id in ids:
            url = base_url + id + "?limit=" + page + "&offset=0"
            yield Request(url, self.parse)

    def parse_category(self, response):
        result = json.loads(response.text)
        temp = result['paging']
        totals = temp['totals']
        cate = CategoryItem()
        cate['id'] = temp['previous'][45:64]
        cate['name'] = categories[cate['id']]
        cate['totals'] = totals
        yield cate
        if temp['is_end']=="false":
            for i in range(totals):
                pass

    def parse(self, response):
        pass
        # self.logger.debug(data,"\n",len(data))
