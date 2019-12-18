from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from myapp.models import Meiju  # 这样直接导入另一个app内编写好的models就可以使用了，分散开来
# Create your views here.

def index(request):
    latest_question_list = Meiju.objects.all()  # [:5]  # 最新的5条输出
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'index.html', context)
