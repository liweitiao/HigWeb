from django.contrib import admin

# Register your models here.
# users/admin.py:
from articles.models import Category, Entry, Price


admin.site.site_title = 'higreen'
admin.site.site_header = '海吉星官网'
admin.site.index_title = '海吉星官网后台管理系统'


class EntryAdmin(admin.ModelAdmin):
    # 指定要显示的属性
    list_display = ["id", "title",  "created_time"]


class CategoryStackedInline(admin.StackedInline):
    model = Entry  # 关联对象类型


class CategoryTabularInline(admin.TabularInline):
    model = Entry  # 关联对象类型

# class CategoryAdmin(admin.ModelAdmin):
#     # inlines = [DepartmentTabularInline]  # 栈的方式显示
#     inlines = [DepartmentStackedInline]      # 表格样式显示


class CategoryAdmin(admin.ModelAdmin):

    # 指定要显示的属性
    list_display = ["id", "name"]
    # inlines = [CategoryStackedInline]  # 栈的方式显示
    # inlines = [CategoryTabularInline]      # 表格样式显示


class PriceAdmin(admin.ModelAdmin):

    # 指定要显示的属性
    # list_display = ["id", "name",  "create_time"]
    list_display = ["id", "name", "price", "create_time"]
    # inlines = [CategoryStackedInline]  # 栈的方式显示
    # inlines = [CategoryTabularInline]      # 表格样式显示


# 注册Model类
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Price, PriceAdmin)

