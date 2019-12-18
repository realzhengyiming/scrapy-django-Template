# -*- coding: utf-8 -*-
import scrapy
from ..items import MeijuItem
from ..items import ClassificationItem
import json


# 这儿只提一页做示范

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['*']
    start_urls = ["https://91mjw.com/all"]
    # cookie = '__c=1575274045; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DQFoa1Qh%252FkL1AbS78fb4h0p3K%252BtQfSrJETaUbO1O2ZW4%253D%26name%3De47d9634%26ts%3D1575274042877%26callbackUrl%3D%252Fjob_detail%252F%253Fquery%253D%2525E6%252595%2525B0%2525E6%25258D%2525AE%2525E5%252588%252586%2525E6%25259E%252590%2526city%253D101280100%2526industry%253D%2526position%253D%26srcReferer%3D&r=&friend_source=0&friend_source=0; JSESSIONID=""; lastCity=101010100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1573438350,1575011966,1575031141,1575341479; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1575385864; __zp_stoken__=0fdalTXSJlRuyvdLXJDNu5I6KOLExidFRHvLB2TOxMT93wBJBmVNsG1vP9sd%2Bvz%2Bbbees4%2F8JzWKnp6dnYtSOYaoCwjk6%2Ff8iVOm4A9RPi30LTwjvsu8zPWrfwuX6vXt1F79; __a=77011797.1575274045..1575274045.35.1.35.35'
    
    
    custom_settings = {  # 每个爬虫使用各自的自定义的设置
        "ITEM_PIPELINES":{
            'myscrapy.pipelines.MyscrapyPipeline': 300,   #  启用这个管道来保存数据
        },
        # "DOWNLOADER_MIDDLEWARES":{   # 这样就可以单独每个使用不同的配置
            # 'JobCrawl.middlewares.proxyMiddleware': 100,   # 使用代理
           # 'tutorial.middlewares.ProxyMiddleware':301
        # },
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer':'https://www.zhipin.com/',
            'X-Requested-With':"XMLHttpRequest",
            # "cookie":"lastCity=101020100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532401467,1532435274,1532511047,1532534098; __c=1532534098; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101020100-p100103%2F; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532581213; __a=4090516.1532500938.1532516360.1532534098.11.3.7.11"
                #'Accept': 'application/json',
            'User-Agent':'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
            # 'cookie':cookie

        }
    }


    def parse(self, response):
        # print(response.xpath("//article"))
        for article in response.xpath("//article"):
            item = MeijuItem()

            name = article.xpath("a").xpath('string(.)').extract()[0]
            grade = article.xpath("div[@class='pingfen']").xpath("string(.)").extract()[0]
            url = article.xpath("a/@href").extract()[0]
            imgurl = article.xpath("a/div/img/@data-original").extract()[0]
            # state = article.xpath("div[@class='zhuangtai']").xpath("string(.)").extract()
            # print(name)
            # print(grade)
            # print(url)
            # print(imgurl)
            # 提取tags
            tags = []
            for a in article.xpath("div[@class='meta']/span[@class='tags']/a"):
            # for a in article
                tempa = a.xpath("text()").extract()
                    # print(tempa)
                tags += tempa
            # print(tags)
            # print()

            # 这儿需要注意的是，要保存的数据不要带['xxx'] ，而要直接'xx'
            item['name'] = name
            item['grade'] = grade
            item['url'] = url
            item['imgurl'] = imgurl
            item['tags'] = tags

            yield item

