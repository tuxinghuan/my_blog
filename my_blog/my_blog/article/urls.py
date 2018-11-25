from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('article_content',views.article_content_view.as_view())
]
