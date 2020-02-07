# -*- coding: utf-8 -*-
import scrapy
import json

categories={
"兴趣":"1178345206151356416",
"明星":"1178345195124490240",
"行业":"1178345203794063360",
"校园":"1178345201055260672",
"教育":"1178345405397508096",
"情感":"1178345219228225536",
"生活":"1178345208739205120",
"游戏":"1178345402679595008",
"影视":"1178345211176026112",
"人文":"1178345407711830016",
"闲趣":"1178345213473615872",
"动漫":"1178345471801753600",
"其他":"1178345497302192128",
}

class ZhihuClubSpider(scrapy.Spider):
    name = 'zhihu-club'
    allowed_domains=['www.zhihu.com']
    start_urls=['https://www.zhihu.com/api/v4/clubs/categories/1178345206151356416']
    # allowed_domains = ['www.zhihu.com/club/explore']
    # start_urls = ['https://www.zhihu.com/club/explore']
    # base_url="https://www.zhihu.com/api/v4/clubs/categories/"+club_id
    def parse(self, response):
        result=json.loads(response.text)
        temp=result['paging']
        totals=temp['totals']
        for i in range(len(totals)//20):
            pass
        data=result['data']
        self.logger.debug(totals)
        # self.logger.debug(data,"\n",len(data))

