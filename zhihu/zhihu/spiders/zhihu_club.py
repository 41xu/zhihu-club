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

page = 20  # 每次请求返回50个club信息

club_url = "https://www.zhihu.com/api/v4/clubs/categories/{category_id}?limit={page}&offset={offset}"


class ZhihuClubSpider(scrapy.Spider):
    name = 'zhihu-club'
    allowed_domains = ['www.zhihu.com']

    def start_requests(self):
        ids = categories.keys()
        for id in ids:
            url = club_url.format(category_id=id, page=page, offset=0)
            yield Request(url, self.parse_category)

    def parse_category(self, response):
        result = json.loads(response.text)
        temp = result['paging']
        totals = temp['totals']
        cate = CategoryItem()
        cate['id'] = temp['previous'][45:64]
        cate['name'] = categories[cate['id']]
        cate['totals'] = totals
        yield cate
        datas = result['data']
        for data in datas:
            club = ClubItem()
            club['category'] = data['category']['id']
            club['id'] = data['id']
            club['name'] = data['name']
            club['description'] = data['description']
            club['created_at'] = data['created_at']
            club['join_count'] = data['join_count']
            club['post_count'] = data['post_count']
            yield club

        if temp['is_end'] == False:
            # 还得翻页
            for i in range(totals // page + 1):
                url = club_url.format(category_id=cate['id'], page=page, offset=i * page)
                yield Request(url, callback=self.parse_club)


    def parse_club(self, response):
        datas = json.loads(response.text)['data']
        for data in datas:
            club = ClubItem()
            club['category'] = data['category']['id']
            club['id'] = data['id']
            club['name'] = data['name']
            club['description'] = data['description']
            club['created_at'] = data['created_at']
            club['join_count'] = data['join_count']
            club['post_count'] = data['post_count']
            yield club

    def parse(self, response):
        pass
        # self.logger.debug(data,"\n",len(data))


"""一条返回的club信息
{'category': {'name': '兴趣', 'id': '1178345206151356416'}, 
'description': '在这里大家可以分享自己喜欢的头像和壁纸哟，互相交流讨论，可把身边的美景拍下来分享大家一起欣赏', 
'admin': ['qing-feng-xu-lai-17-43'], 
'created_at': 1574594125, 'join_count': 31047, 
'post_count': 1821, 'rules': '', 
'avatar': 'https://pic2.zhimg.com/v2-ea7dc9bffa4d5d35281e695022984aa3_b.jpg', 
'background': 'https://pic2.zhimg.com/v2-84beaae5b93fca03af5c0d2bb69730a5_b.jpg', 
'id': '1182014114103353344', 
'name': '头像壁纸美图圈'}
"""
