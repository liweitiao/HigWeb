from django.conf.urls import url, include
from . import views

app_name = 'price'

urlpatterns = [
    url(r'^price', views.price, name='article_price'),
]
