# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        item.save()   #   管道这儿把yield到的item调用保存就可以（djangoitem)
        return item
