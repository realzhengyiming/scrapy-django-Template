from django.db import models
# from scrapy_djangoitem import DjangoItem
from django.utils.safestring import mark_safe

# todo设置utf8mb4后charField默认长度变成了191，255就超过了长度。一个字符变成了四个字节，而不是utf8中的三个字节

class Classification(models.Model):  # 这个用来记录电影的类型名
    classify_name = models.CharField(max_length=191, unique=True)   

    def __str__(self):
        return self.classify_name

class Meiju(models.Model):
    name = models.CharField(max_length=191)
    url = models.CharField(max_length=191, unique=True)  # url
    grade = models.CharField(default="", max_length=191)   # 文本类型存下来数字
    imgurl = models.CharField(default="", max_length=191)
    classification = models.ManyToManyField(Classification)  # 一堆多外键，但是这样好像增加保存的难度了，不过可以一次性的进行显示等。

    def show_photos(self):   # 这个方法好，可以显示缩略图了
        return mark_safe('<img src="%s" height="60px";width:auto />' % (self.imgurl,))

    def __str__(self):
        return self.name

