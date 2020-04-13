from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=128, verbose_name='文章分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = '文章分类'


# class Tag(models.Model):
#
#     name = models.CharField(max_length=128, verbose_name='文章标签')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "文章标签"
#         verbose_name_plural = '文章标签'


class Entry(models.Model):

    title = models.CharField(max_length=128, verbose_name='文章标题')

    author = models.ForeignKey(User, verbose_name='文章作者')

    img = models.ImageField(upload_to='blog_images', null=True, blank=True, verbose_name='文章配图')

    body = RichTextUploadingField(verbose_name='文章正文')

    abstract = models.TextField(max_length=256, blank=True, null=True, verbose_name='文章摘要')

    visiting = models.PositiveIntegerField(default=0, verbose_name='文章访问量')

    category = models.ManyToManyField('Category', verbose_name='文章分类')

    # tags = models.ManyToManyField('Tag', verbose_name='文章+标签')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', kwargs={'article_id': self.id})  # http://127.0.0.1/article/3

    def increase_visiting(self):
        self.visiting += 1
        self.save(update_fields=['visiting'])

    class Meta:
        ordering = ['-created_time']
        verbose_name = "文章"
        verbose_name_plural = "文章"


class Price(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, verbose_name='品名')
    price = models.CharField(max_length=8, null=False, verbose_name='价格')
    unit = models.CharField(max_length=4, null=False, verbose_name='单位')
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        # 指定表名
        db_table = 'news_price'

        verbose_name = '价格表'
        verbose_name_plural = verbose_name