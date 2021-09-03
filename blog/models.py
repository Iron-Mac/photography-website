from django.db import models
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField
from django.utils import timezone
from extentions.utils import jalali_converter

# Custom Manager

class PostManager(models.Manager):
    def published(self):
        return self.filter(status='p')






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

class Post(models.Model):
    STATUS_CHOISES={
        ('d',"پیش نویس"),
        ('p',"منتشر شده"),
    }
    title = models.CharField( ("عنوان پست"),max_length=100)
    description = models.TextField(("توضیحات"))
    slug = models.SlugField(("اسلاگ"),max_length=100,unique=True)
    thumbnail = models.ImageField(("عکس"), upload_to="images")
    publish = models.DateField(("منتشر شده"), default=timezone.now)
    created = models.DateField(("ساخته شده"), auto_now_add=True)
    updated = models.DateField(("ساخته شده"), auto_now=True)
    category = models.ManyToManyField(Category, verbose_name=("دسته‌بندی"))
    status = models.CharField(("وضعیت"), max_length=1, choices=STATUS_CHOISES)

    class Meta:
        verbose_name="پست"
        verbose_name_plural="پست ها"


    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish) 
    jpublish.short_description = "زمان انتشار"
    

    def category_published(self):
        return self.category.filter(status=True)

    objects = PostManager()
