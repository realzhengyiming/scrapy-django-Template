# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from myapp.models import Meiju  # settings中设置好了路径，这儿可以直接app导入django模型
from myapp.models import Classification  # 这个和上一个是多对多的操作的类
import pymysql

class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        try: # 可能会出现重复
            item.save()   # 直接先存下这个美剧的类
        except Exception as e:
            pass
        print(item['url'])
        if len(item['tags']) != 0:
            pass    # 这儿就开始逐个增加这个对象，然后再绑定到一起
            print(item['tags'])
            # print(type(item['tags']))
            meiju = Meiju.objects.get(url=item['url'])  # 查询一次就可以
            for tag in item['tags']:
                try:
                    c = Classification.objects.get(classify_name=tag)  # 找到的话就直接加入另一个Meiju对象中
                    meiju.classification.add(c)
                except Classification.DoesNotExist:
                    print("需要创建这个")
                    c = Classification()
                    c.classify_name = tag
                    c.save()
                    meiju.classification.add(c)
                #     pass   # 这儿就使用增加这个orm类来进行操作

        #  并没有多难嘛，就是不知道这儿可不可以直接进行操作models
        # for tag in
        # try:
        #     question = Questions.objects.get(identifier=item["identifier"])  # 没有这个就创建这个（manytomany在另一个上）
        #     print
        #     "Question already exist"
        #     return item
        # except Questions.DoesNotExist:
        #     pass
        #
        #
        # djangoItem = item.save(commit=False)
        # # item.save()   #   管道这儿把yield到的item调用保存就可以（djangoitem)
        # print(item['tags'])
        # print(type(djangoItem))
        # if len(item['tags']) != 0:
        #     pass
        # else:
        #     item_model = item_to_model(item)
        #
        #
        #
        # print("给我康康")
        # print(djangoItem.classification)



        return item
