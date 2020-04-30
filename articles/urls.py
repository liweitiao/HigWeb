from django.conf.urls import url, include
from . import views
from articles.views import ListView, MediaListView, BianminListView, DangqunListView, GonggaoListView

app_name = 'article'

urlpatterns = [
    url(r'^$', views.index, name='article_index'),
    url(r'^article/price', views.price, name='article_price'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='article_detail'),
    url(r'^qiye$', views.qiye, name='article_qiye'),
    url(r'^xinwen$', views.xinwen, name='article_xinwen'),
    url(r'^xinwen2$', views.xinwen2, name='article_xinwen2'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 新闻列表页
    # url(r'^medialist/(?P<page>\d+)$', MediaListView.as_view(), name='medialist'), # 媒体播报列表页
    url(r'^bianminlist/(?P<type_id>\d+)/(?P<page>\d+)$', BianminListView.as_view(), name='bianminlist'),
    url(r'^dangqunlist/(?P<type_id>\d+)/(?P<page>\d+)$', DangqunListView.as_view(), name='dangqunlist'),
    url(r'^gonggaolist/(?P<type_id>\d+)/(?P<page>\d+)$', GonggaoListView.as_view(), name='gonggaolist'),
    url(r'^bianmin$', views.bianmin, name='article_bianmin'),
    url(r'^yuanqu$', views.yuanqu, name='article_yuanqu'),
    url(r'^dangqun$', views.dangqun, name='article_dangqun'),
    url(r'^gonggao$', views.gonggao, name='article_gonggao'),
    url(r'^fupin$', views.fupin, name='article_fupin'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='article_category'),
    url(r'^yuanqu/gouwu$', views.gouwu, name='article_gouwu'),
    url(r'^yuanqu/yewu$', views.yewu, name='article_yewu'),
    url(r'^yuanqu/cheka$', views.cheka, name='article_cheka'),
    url(r'^yuanqu/jiesuan$', views.jiesuan, name='article_jiesuan'),
    url(r'^yuanqu/kefu$', views.kefu, name='article_kefu'),
]
