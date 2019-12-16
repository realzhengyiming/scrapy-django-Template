# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 后面这部分是增加的。    
from myapp.models import Meiju  # settings中设置好了路径，这儿可以直接app导入django模型
from scrapy_djangoitem import DjangoItem

class MeijuItem(DjangoItem):
    django_model = Meiju    
