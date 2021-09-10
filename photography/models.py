from django.db import models
from django.contrib.auth.models import User
# Create your models here

class Photo(models.Model):
    title = models.CharField(("عنوان عکس"), max_length=200)
    photo = models.ImageField(("عکس"), upload_to="images")
    photographer = models.ForeignKey(User, verbose_name=("عکاس"), on_delete=models.SET_NULL,null=True)
    caption = models.TextField(("توضیحات"))
    time = models.DateTimeField(("تاریخ ثبت"), blank=True , null=True)

def __str__(self):
    return self.title
