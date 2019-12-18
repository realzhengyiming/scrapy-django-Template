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
from myapp.models import Classification  # 这个和上一个是多对多的操作的类
from scrapy_djangoitem import DjangoItem


class MeijuItem(DjangoItem):
    django_model = Meiju
    tags = scrapy.Field()  # 这儿存字符串把  ，不知道是不是因为增加了这个，然后就出大问题了，自动保存的东西都加上了['']

class ClassificationItem(DjangoItem):  # 这个是分类的类
    django_model = Classification

