from django import template
from ..models import Entry,Category

register = template.Library()


@register.simple_tag
def get_recent_entries(num=5):
    return Entry.objects.all().order_by('-created_time')[:num]


# 园区动态最新６条文章
@register.simple_tag
def get_recent_entries_01(num=6):
    c01 = Category.objects.get(id=1)
    return Entry.objects.filter(category=c01).order_by('-created_time')[:num]


# 媒体播报最新６条文章
@register.simple_tag
def get_recent_entries_02(num=6):
    c02 = Category.objects.get(id=2)
    return Entry.objects.filter(category=c02).order_by('-created_time')[:num]


# 政策法规最新６条文章
@register.simple_tag
def get_recent_entries_03(num=9):
    c03 = Category.objects.get(id=3)
    return Entry.objects.filter(category=c03).order_by('-created_time')[:num]


# 食品舆情最新６条文章
@register.simple_tag
def get_recent_entries_04(num=9):
    c04 = Category.objects.get(id=4)
    return Entry.objects.filter(category=c04).order_by('-created_time')[:num]


# 企业公告最新６条文章
@register.simple_tag
def get_recent_entries_09(num=6):
    c09 = Category.objects.get(id=9)
    c10 = Category.objects.get(id=10)
    c11 = Category.objects.get(id=11)
    c12 = Category.objects.get(id=12)
    return Entry.objects.filter(category__in=[c09, c10, c11, c12]).order_by('-created_time')[:num]


# 党群信息最新６条文章
@register.simple_tag
def get_recent_entries_06(num=6):
    c06 = Category.objects.get(id=6)
    c07 = Category.objects.get(id=7)
    c08 = Category.objects.get(id=8)
    return Entry.objects.filter(category__in=[c06, c07, c08]).order_by('-created_time')[:num]


# 食品知识最新６条文章
@register.simple_tag
def get_recent_entries_05(num=6):
    c05 = Category.objects.get(id=5)
    return Entry.objects.filter(category=c05).order_by('-created_time')[:num]


@register.simple_tag
def get_popular_entries(num=5):
    return Entry.objects.all().order_by('-visiting')[:num]


@register.simple_tag
def get_categories():
    return Category.objects.all()


@register.simple_tag
def get_entry_count_of_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()


@register.simple_tag
def archives():
    return Entry.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_entry_count_of_date(year, month):
    return Entry.objects.filter(created_time__year=year, created_time__month=month).count()
