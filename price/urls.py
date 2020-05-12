from django.conf.urls import url, include
from . import views

app_name = 'price'

urlpatterns = [
    url(r'^price$', views.price, name='article_price'),
    url(r'^price02$', views.price02, name='article_price02'),
]
