from django.db import models
# from scrapy_djangoitem import DjangoItem
from django.utils.safestring import mark_safe


class Meiju(models.Model):
    name = models.CharField(default="", max_length=50)
    url = models.CharField(default="", max_length=255)  # url
    grade = models.CharField(default="", max_length=50)   # 文本类型存下来数字
    imgurl = models.CharField(default="", max_length=255)

    def show_photos(self):   # 这个方法好，可以显示缩略图了
        return mark_safe('<img src="%s" height="60px";width:auto />' % (self.imgurl,))
