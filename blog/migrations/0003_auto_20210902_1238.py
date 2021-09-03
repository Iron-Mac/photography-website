# Generated by Django 3.2.7 on 2021-09-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='اسلاگ')),
                ('status', models.BooleanField(verbose_name='نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
                'ordering': ['position'],
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان پست'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته\u200cبندی'),
        ),
    ]
