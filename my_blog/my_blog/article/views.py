from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
        posts = Article.objects.all()  #获取全部的Article对象
        paginator = Paginator(posts, 3)
        page=request.GET.get('page')
        try:
                post_list= paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
                post_list= paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
                post_list= paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'post_list' : post_list})

def detail(request,id):
        try:
                post=Article.objects.get(id=str(id))
        except Article.DoesNotExist:
                raise Http404
        return render(request,'post.html',{'post':post})

def archives(request):
        dates=Article.objects.datetimes('date_time','month',order='DESC')
        return render(request,'home.html',{'dates':dates})


def AboutMe(request):
        return render(request,'AboutMe.html')



