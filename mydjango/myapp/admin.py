from django.contrib import admin
# from .models import Job
# from .models import News
from .models import Meiju


# Register your models here.
class MeijuAdmin(admin.ModelAdmin):
    # 对字段进行显示
    list_display = ('name', "url", 'grade', 'show_photos')
    # 对字段增加解释之类的
    # fieldsets = [
    #     (None,              {'fields': ['question_text']}),   # 这儿需要填写正确的字段名
    #     ('Date infomation', {'fields': ['pub_date']}),
    #     ("upload file",     {"fields": ['photos', 'show_photos']}),
    #     # ("预览",            {"fields": []})
    # ]
    # inlines = [ChoiceInline, CategoriesInline]
    # 增加过滤字段的设置
    # list_filter = ['pub_date']
    # 增加搜索字段
    # search_fields = ['question_text']
    readonly_fields = ['show_photos']
    
admin.site.register(Meiju, MeijuAdmin)