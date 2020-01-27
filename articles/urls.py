from django.conf.urls import url
from . import views
from articles.views import ListView

app_name = 'article'

urlpatterns = [
    url(r'^$', views.index, name='article_index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='article_detail'),
    url(r'^qiye$', views.qiye, name='article_qiye'),
    url(r'^xinwen$', views.xinwen, name='article_xinwen'),
    url(r'^xinwen2$', views.xinwen2, name='article_xinwen2'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
    url(r'^bianmin$', views.bianmin, name='article_bianmin'),
    url(r'^yuanqu$', views.yuanqu, name='article_yuanqu'),
    url(r'^dangqun$', views.dangqun, name='article_dangqun'),
    url(r'^gonggao$', views.gonggao, name='article_gonggao'),
    # url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='article_category'),

]
