from django.db import models
# from scrapy_djangoitem import DjangoItem
from django.utils.safestring import mark_safe


class KeyWordItem(models.Model):  
    ''' 这个模型类只是用来存关键词的 '''
    name = models.CharField(max_length=50)


# 反过来，关键词拍前的
