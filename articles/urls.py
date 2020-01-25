from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$', views.index, name='article_index'),
    url(r'^qiye$', views.qiye, name='article_qiye'),
    url(r'^xinwen$', views.xinwen, name='article_xinwen'),
    url(r'^bianmin$', views.bianmin, name='article_bianmin'),
    url(r'^yuanqu$', views.yuanqu, name='article_yuanqu'),
    url(r'^dangqun$', views.dangqun, name='article_dangqun'),
    url(r'^gonggao$', views.gonggao, name='article_gonggao'),
]
