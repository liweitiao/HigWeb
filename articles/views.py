from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from . import models

# Create your views here.


def index(request):
    return render(request, 'article/index4.html', locals())


def detail(request, article_id):
    return render(request, 'article/detail.html', locals())


def qiye(request):
    return render(request, 'article/企业概况3练习.html', locals())


def xinwen(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'article/新闻中心2.html', locals())


def xinwen2(request):
    # 园区动态文章列表
    c01 = models.Category.objects.get(id=1)
    entries_01 = models.Entry.objects.filter(category=c01)
    page_01 = request.GET.get('page', 1)
    entry_list_01, paginator_01 = make_paginator(entries_01, page_01)
    page_data_01 = pagination_data(paginator_01, page_01)
    # 媒体播报文章列表
    c02 = models.Category.objects.get(id=2)
    entries_02 = models.Entry.objects.filter(category=c02)
    page_02 = request.GET.get('page', 1)
    entry_list_02, paginator_02 = make_paginator(entries_02, page_02)
    page_data_02 = pagination_data(paginator_02, page_02)
    return render(request, 'article/新闻中心2.html', locals())


# def category(request, category_id):
#     c = models.Category.objects.get(id=category_id)
#     # c = get_object_or_404(models.Category, id=category_id)
#     entries = models.Entry.objects.filter(category=c)
#     page = request.GET.get('page', 1)
#     entry_list, paginator = make_paginator(entries, page)
#     page_data = pagination_data(paginator, page)
#     return render(request, 'article/新闻中心.html', locals())


def bianmin(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'article/便民信息.html', locals())


def yuanqu(request):
    return render(request, 'article/园区指南.html', locals())


def dangqun(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'article/党群建设.html', locals())


def gonggao(request):
    entries = models.Entry.objects.all()
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'article/公告栏.html', locals())


def make_paginator(objects, page, num=5):
    paginator = Paginator(objects, num)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list, paginator


def pagination_data(paginator, page):
    """
    用于自定义展示分页页码的方法
    :param paginator: Paginator类的对象
    :param page: 当前请求的页码
    :return: 一个包含所有页码和符号的字典
    """
    if paginator.num_pages == 1:
        # 如果无法分页，也就是只有1页不到的内容，则无需显示分页导航条，不用任何分页导航条的数据，因此返回一个空的字典
        return {}
    # 当前页左边连续的页码号，初始值为空
    left = []

    # 当前页右边连续的页码号，初始值为空
    right = []

    # 标示第 1 页页码后是否需要显示省略号
    left_has_more = False

    # 标示最后一页页码前是否需要显示省略号
    right_has_more = False

    # 标示是否需要显示第 1 页的页码号。
    # 因为如果当前页左边的连续页码号中已经含有第 1 页的页码号，此时就无需再显示第 1 页的页码号，
    # 其它情况下第一页的页码是始终需要显示的。
    # 初始值为 False
    first = False

    # 标示是否需要显示最后一页的页码号。
    # 需要此指示变量的理由和上面相同。
    last = False

    # 获得用户当前请求的页码号
    try:
        page_number = int(page)
    except ValueError:
        page_number = 1
    except:
        page_number = 1

    # 获得分页后的总页数
    total_pages = paginator.num_pages

    # 获得整个分页页码列表，比如分了四页，那么就是 [1, 2, 3, 4]
    page_range = paginator.page_range

    if page_number == 1:
        # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）。
        # 此时只要获取当前页右边的连续页码号，
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]。
        # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
        right = page_range[page_number:page_number + 4]

        # 如果最右边的页码号比最后一页的页码号减去 1 还要小，
        # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示。
        if right[-1] < total_pages - 1:
            right_has_more = True

        # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
        # 所以需要显示最后一页的页码号，通过 last 来指示
        if right[-1] < total_pages:
            last = True

    elif page_number == total_pages:
        # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空），
        # 此时只要获取当前页左边的连续页码号。
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
        # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码。
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]

        # 如果最左边的页码号比第 2 页页码号还大，
        # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示。
        if left[0] > 2:
            left_has_more = True

        # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码，
        # 所以需要显示第一页的页码号，通过 first 来指示
        if left[0] > 1:
            first = True
    else:
        # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号，
        # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码。
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        right = page_range[page_number:page_number + 2]

        # 是否需要显示最后一页和最后一页前的省略号
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True

        # 是否需要显示第 1 页和第 1 页后的省略号
        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True

    data = {
        'left': left,
        'right': right,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'first': first,
        'last': last,
    }
    return data


def category(request, category_id):
    c = models.Category.objects.get(id=category_id)
    # c = get_object_or_404(models.Category, id=category_id)
    entries = models.Entry.objects.filter(category=c)
    page = request.GET.get('page', 1)
    entry_list, paginator = make_paginator(entries, page)
    page_data = pagination_data(paginator, page)
    return render(request, 'article/新闻中心.html', locals())


# 种类id 页码 排序方式
# restful api -> 请求一种资源
# /list?type_id=种类id&page=页码&sort=排序方式
# /list/种类id/页码/排序方式
# /list/种类id/页码?sort=排序方式
class ListView(View):
    '''列表页'''
    def get(self, request, type_id, page):
        '''显示列表页'''
        # 获取种类信息
        # try:
        #     type = GoodsType.objects.get(id=type_id)
        # except GoodsType.DoesNotExist:
        #     # 种类不存在
        #     return redirect(reverse('goods:index'))
        #
        # # 获取商品的分类信息
        # types = GoodsType.objects.all()

        category = models.Category.objects.get(id=type_id)
        entry_list = models.Entry.objects.filter(category=category)

        # 获取排序的方式 # 获取分类商品的信息
        # sort=default 按照默认id排序
        # sort=price 按照商品价格排序
        # sort=hot 按照商品销量排序
        sort = request.GET.get('sort')
        if not sort:
            sort = 'default'
        print(sort)
        #
        # if sort == 'price':
        #     skus = GoodsSKU.objects.filter(type=type).order_by('price')
        # elif sort == 'hot':
        #     skus = GoodsSKU.objects.filter(type=type).order_by('-sales')
        # else:
        #     sort = 'default'
        #     skus = GoodsSKU.objects.filter(type=type).order_by('-id')

        # 对数据进行分页
        paginator = Paginator(entry_list, 4)

        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        # 获取第page页的Page实例对象
        # skus_page = paginator.page(page)
        entry_list_page = paginator.page(page)


        # 1.总页数小于5页，页面上显示所有页码
        # 2.如果当前页是前3页，显示1-5页
        # 3.如果当前页是后3页，显示后5页
        # 4.其他情况，显示当前页的前2页，当前页，当前页的后2页
        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages+1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4, num_pages+1)
        else:
            pages = range(page-2, page+3)

        # 获取新品信息
        # new_skus = GoodsSKU.objects.filter(type=type).order_by('-create_time')[:2]


        # 组织模板上下文
        context = {'entry_list_page': entry_list_page,
                   'pages': pages,
                   'sort': sort,
                   'category':category}

        # 使用模板
        return render(request, 'article/新闻中心3.html', context)


class BianminListView(View):
    '''列表页'''
    def get(self, request, type_id, page):
        category = models.Category.objects.get(id=type_id)
        entry_list = models.Entry.objects.filter(category=category)
        sort = request.GET.get('sort')
        if not sort:
            sort = 'default'
        print(sort)

        # 对数据进行分页
        paginator = Paginator(entry_list, 4)

        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        entry_list_page = paginator.page(page)

        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages+1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4, num_pages+1)
        else:
            pages = range(page-2, page+3)

        # 组织模板上下文
        context = {'entry_list_page': entry_list_page,
                   'pages': pages,
                   'sort': sort,
                   'category':category}

        # 使用模板
        return render(request, 'article/便民信息2.html', context)


class DangqunListView(View):
    '''列表页'''
    def get(self, request, type_id, page):
        category = models.Category.objects.get(id=type_id)
        entry_list = models.Entry.objects.filter(category=category)
        sort = request.GET.get('sort')
        if not sort:
            sort = 'default'
        print(sort)

        # 对数据进行分页
        paginator = Paginator(entry_list, 4)

        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        entry_list_page = paginator.page(page)

        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages+1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages-4, num_pages+1)
        else:
            pages = range(page-2, page+3)

        # 组织模板上下文
        context = {'entry_list_page': entry_list_page,
                   'pages': pages,
                   'sort': sort,
                   'category':category}

        # 使用模板
        return render(request, 'article/党群建设2.html', context)


class GonggaoListView(View):
    '''列表页'''

    def get(self, request, type_id, page):
        category = models.Category.objects.get(id=type_id)
        entry_list = models.Entry.objects.filter(category=category)
        sort = request.GET.get('sort')
        if not sort:
            sort = 'default'
        print(sort)

        # 对数据进行分页
        paginator = Paginator(entry_list, 4)

        # 获取第page页的内容
        try:
            page = int(page)
        except Exception as e:
            page = 1

        if page > paginator.num_pages:
            page = 1

        entry_list_page = paginator.page(page)

        num_pages = paginator.num_pages
        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        # 组织模板上下文
        context = {'entry_list_page': entry_list_page,
                   'pages': pages,
                   'sort': sort,
                   'category': category}

        # 使用模板
        return render(request, 'article/公告栏2.html', context)