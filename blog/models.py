from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import format_html
from extentions.utils import jalali_converter

# Custom Manager

class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)




# Create your models here.

class Category(models.Model):
    title = models.CharField(("عنوان دسته‌بندی"),max_length=100)
    slug = models.SlugField(("اسلاگ"),max_length=100,unique=True)
    status = models.BooleanField(("نمایش داده شود؟"))
    position =models.IntegerField(("وضعیت"))

    class Meta:
        verbose_name="دسته‌بندی"
        verbose_name_plural="دسته‌بندی‌ها"
        ordering = ['position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Post(models.Model):
    STATUS_CHOISES={
        ('d',"پیش نویس"),
        ('p',"منتشر شده"),
    }
    author = models.ForeignKey(User, verbose_name=("نویسنده"), on_delete=models.SET_NULL, null=True , related_name="posts")
    title = models.CharField( ("عنوان پست"),max_length=100)
    description = models.TextField(("توضیحات"))
    slug = models.SlugField(("اسلاگ"),max_length=100,unique=True)
    thumbnail = models.ImageField(("عکس"), upload_to="images")
    publish = models.DateTimeField(("منتشر شده"), default=timezone.now)
    created = models.DateTimeField(("ساخته شده"), auto_now_add=True)
    updated = models.DateTimeField(("ساخته شده"), auto_now=True)
    category = models.ManyToManyField(Category, verbose_name=("دسته‌بندی"), related_name="posts")
    status = models.CharField(("وضعیت"), max_length=1, choices=STATUS_CHOISES)
    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست ها"


    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish) 
    jpublish.short_description = "زمان انتشار"
    
    def thumbnail_tag(self):
        return format_html(f"<img width=100 style='border-radius:5px;' src='{self.thumbnail.url}'")
    thumbnail_tag.short_description ="عکس"

    def category_published(self):
        return self.category.filter(status=True)

    objects = PostManager()
