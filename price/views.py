from django.shortcuts import render
from django.db import connections
from django.http import JsonResponse
import json

# Create your views here.


def price(request):
    print(request)
    cursor = connections['oracle01'].cursor()
    # cursor = connection.cursor()
    print(222222222222)
    cursor.execute("select * from \
(select CATEGORY_NAME, AVG_PRICE, TO_CHAR(CREATE_DATE, 'yyyy-mm-dd'), ORIGIN_NAME  from T_PRICE_COLLECTION_202004 \
where AVG_PRICE is NOT NULL and AVG_PRICE>0 and PARENT_CATEGORY_ID='220D46491A462CE5E050A8C043012F5B'\
order by CREATE_DATE desc) \
where rownum<100")
    result02 = cursor.fetchall()
    key = ('name','price','day','area')
    result = []
    for item in result02:
        item02 = dict(zip(key, item))
        print(item02)
        result.append(item02)
    # print(result[1])
    # return render(request, 'index.html')
    print(result)
    return JsonResponse(result, safe=False)


def price02(request):
    print(request)
    cursor = connections['oracle01'].cursor()
    # cursor = connection.cursor()
    print(222222222222)
    cursor.execute("select * from \
(select CATEGORY_NAME, AVG_PRICE, TO_CHAR(CREATE_DATE, 'yyyy-mm-dd'), ORIGIN_NAME  from T_PRICE_COLLECTION_202005 \
where AVG_PRICE is NOT NULL and AVG_PRICE>0 and PARENT_CATEGORY_ID='220D46491A462CE5E050A8C043012F5B'\
order by CREATE_DATE desc) \
where rownum<100")
    result02 = cursor.fetchall()
    key = ('name','price','day','area')
    result = []
    for item in result02:
        item02 = dict(zip(key, item))
        print(item02)
        result.append(item02)
    # print(result[1])
    # return render(request, 'index.html')
    print(result)
    return JsonResponse(result, safe=False)


def price03(request):
    print(request)
    cursor = connections['oracle01'].cursor()
    # cursor = connection.cursor()
    print(222222222222)
    cursor.execute("select * from \
(select CATEGORY_NAME, AVG_PRICE, TO_CHAR(CREATE_DATE, 'yyyy-mm-dd'), ORIGIN_NAME  from T_PRICE_COLLECTION_202005 \
where AVG_PRICE is NOT NULL and AVG_PRICE>0 \
order by CREATE_DATE desc) \
where rownum<100")
    result = cursor.fetchall()
    # print(result[1])
    # return render(request, 'index.html')
    print(result)
    return JsonResponse(result, safe=False)