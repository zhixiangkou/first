# Generated by Django 2.2.3 on 2020-05-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200517_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='text1',
            field=models.TextField(blank=True, verbose_name='封面简介'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='text2',
            field=models.TextField(blank=True, verbose_name='博客简介'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='text3',
            field=models.TextField(blank=True, verbose_name='关于简介'),
        ),
    ]
