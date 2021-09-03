# Generated by Django 3.2.7 on 2021-09-01 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='عکس')),
                ('publish', models.DateField(default=django.utils.timezone.now, verbose_name='منتشر شده')),
                ('created', models.DateField(auto_now_add=True, verbose_name='ساخته شده')),
                ('updated', models.DateField(auto_now=True, verbose_name='ساخته شده')),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'published')], max_length=1, verbose_name='وضعیت')),
            ],
        ),
    ]