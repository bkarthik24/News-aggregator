
from django.conf.urls import url
from . import views

app_name = 'aggregator'

urlpatterns = [url(r'^$', views.topstories, name='topstories'),url(r'^worldnews$', views.worldnews, name='worldnews'),url(r'^sportsnews$', views.sportsnews, name='sportsnews'),url(r'^businessnews$',views.businessnews, name='businessnews'),url(r'^technews$',views.technews, name='technews'),url(r'^entertainment$',views.entertainment, name='entertainment'),url(r'^topstories$',views.topstories, name='topstories')]